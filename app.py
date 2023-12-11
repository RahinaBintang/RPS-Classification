from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load models
model_cnn = load_model('models/cnn_model.h5')
model_inceptionv3 = load_model('models/inceptionv3_model.h5')

# Set the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}

# Define class labels
labels = ['Kertas', 'Batu', 'Gunting']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        return render_template('upload.html', filename=filename)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        filename = request.form['filename']
        selected_model = request.form['selected_model']
    else:
        filename = request.args.get('filename')
        selected_model = request.args.get('selected_model')

    # Image Path
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    preprocessing_number = 0

    # Load the image & selected model
    if selected_model == 'cnn':
        selected_model = model_cnn
        img = image.load_img(file_path, target_size=(128, 128))
    elif selected_model == 'inceptionv3':
        selected_model = model_inceptionv3
        img = image.load_img(file_path, target_size=(299, 299))
        preprocessing_number = 1
    else:
        # Handle the case where no model is selected
        return render_template('error.html', message='Invalid model selection')

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = selected_model.predict(img_array)
    predicted_class = ''

    if preprocessing_number == 0: 
        # Get the predicted class index
        predicted_class_index = np.argmax(prediction)

        # Get the predicted class label
        predicted_class = labels[predicted_class_index]

    elif preprocessing_number == 1:
        # Get the predicted class indices for each class
        predicted_class_indices = np.where(prediction > 0.5)[1]

        # Check if any class is predicted
        if len(predicted_class_indices) > 0:
            # Get the first predicted class label (you may need to modify this logic based on your specific requirements)
            predicted_class = labels[predicted_class_indices[0]]
        else:
            predicted_class = 'No Class Predicted'

    return render_template('predict.html', filename=filename, prediction=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
