# Import modul Flask dan modul yang diperlukan
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Load model machine learning yang telah dilatih sebelumnya
model_cnn = load_model('models/cnn_model.h5')
model_inceptionv3 = load_model('models/inceptionv3_model.h5')

# Konfigurasi folder untuk menyimpan file yang diunggah dan ekstensi yang diizinkan
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}

# Tentukan label kelas untuk hasil prediksi
labels = ['Kertas', 'Batu', 'Gunting']

# Fungsi untuk memeriksa apakah file memiliki ekstensi yang diizinkan
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Rute untuk menampilkan halaman unggah awal
@app.route('/')
def upload_page():
    return render_template('upload.html')

# Rute untuk menangani unggahan file
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

# Rute untuk menangani prediksi gambar
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        filename = request.form['filename']
        selected_model = request.form['selected_model']
    else:
        filename = request.args.get('filename')
        selected_model = request.args.get('selected_model')

    # Path gambar
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    preprocessing_number = 0

    # Muat gambar dan model yang dipilih
    if selected_model == 'cnn':
        selected_model = model_cnn
        img = image.load_img(file_path, target_size=(128, 128))
    elif selected_model == 'inceptionv3':
        selected_model = model_inceptionv3
        img = image.load_img(file_path, target_size=(299, 299))
        preprocessing_number = 1
    else:
        # Tangani kasus ketika tidak ada model yang dipilih
        return render_template('error.html', message='Pemilihan model tidak valid')

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = selected_model.predict(img_array)
    predicted_class = ''

    # Proses prediksi berdasarkan preprocessing_number
    if preprocessing_number == 0: 
        # Dapatkan indeks kelas yang diprediksi
        predicted_class_index = np.argmax(prediction)

        # Dapatkan label kelas yang diprediksi
        predicted_class = labels[predicted_class_index]

    elif preprocessing_number == 1:
        # Dapatkan indeks kelas yang diprediksi untuk setiap kelas
        predicted_class_indices = np.where(prediction > 0.5)[1]

        # Periksa apakah ada kelas yang diprediksi
        if len(predicted_class_indices) > 0:
            # Dapatkan label kelas yang diprediksi pertama (Anda mungkin perlu memodifikasi logika ini berdasarkan kebutuhan spesifik Anda)
            predicted_class = labels[predicted_class_indices[0]]
        else:
            predicted_class = 'Tidak Ada Kelas yang Diprediksi'

    return render_template('predict.html', filename=filename, prediction=predicted_class)

# Jalankan aplikasi jika script dijalankan
if __name__ == '__main__':
    app.run(debug=True)
