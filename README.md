# ✨ RPS Vision: Klasifikasi Otomatis Batu, Kertas, dan Gunting dengan CNN dan InceptionV3 ✨

## Overview Project
Proyek ini bertujuan untuk mengembangkan sebuah sistem klasifikasi gambar yang dapat mengenali dan membedakan gambar-gambar yang termasuk dalam kategori *"Rock"*, *"Paper"*, dan *"Scissors"* Sistem ini dapat berguna sebagai bagian dari implementasi permainan batu-gunting-kertas **(Rock, Paper, Scissors)** atau sebagai komponen dalam aplikasi yang memerlukan kemampuan klasifikasi gambar.

**Link Dataset yang digunakan:** [RPS Dataset](https://drive.google.com/drive/folders/1FhH72OaOBqVZchjYa4KLqFerBupNckEb?usp=sharing). Preprocessing yang digunakan antara lain Resizing, Normalization, Augmentation.

Model yang digunakan: ***Convolutional Neural Network*** (CNN) dengan 3 Layer dan Pre Trained Model ***Inception-V3*** dengan Architecture Model kurang lebih seperti gambar berikut.

**CNN Architecture** ✨

![image](https://github.com/RahinaBintang/Data-Science/blob/abd3fcafd310a5680bd6e78b0551a478b26481e0/assets/model/CNN%20Flow.png)

**Inception-V3 Architecture** ✨

![image](https://github.com/RahinaBintang/Data-Science/blob/2333b523b8e4b38055b04cda021be1b790b9b978/assets/model/InceptionV3%20Flow.png)

## Overview Dataset
Dataset yang digunakan adalah RPS Dataset dengan link sebagai [berikut](https://drive.google.com/drive/folders/1FhH72OaOBqVZchjYa4KLqFerBupNckEb?usp=sharing). Dataset terdiri atas 2.520 data yang terbagi menjadi 70% sebagai *Training Set*, 15% sebagai *Validation Set*, dan 15% sebagai *Testing Set*, dimana pada setiap Set, terdapat 3 Label Class yaitu *Paper'*, *'Rock'*, dan *'Scissors'*. 

## Preprocessing & Modelling

### CNN Model ✨
**Preprocessing**

Preprocessing yang dilakukan antara lain adalah *resizing* **(128,128)**, lalu *rescale / normalization* dengan rentang **1./255**, dilanjut dengan melakukan *splitting* dataset menjadi 3 *(Training, Validation, dan Testing)* sesuai dengan penjelasan pada Dataset.

**Modelling**

Hasil dari CNN Model yang telah dibangun adalah sebagai berikut :

![image](https://github.com/RahinaBintang/RPS-Classification/blob/38badf24f75925826aa7e54a3568889d39ca1330/assets/summary_cnn_model.png)

**Model Evaluation**

Berikut adalah hasil dari fitting CNN Model yang telah dibangun :

![image](https://github.com/RahinaBintang/RPS-Classification/blob/3e40ed59be32456eb4de90c79ed0c9f1ab31f84e/assets/CNN_acc.png)

Plot diatas menunjukkan bahwa training acc dapat stabil diatas **95%**, namun validation acc nya mengalami fluktuatif acc pada rentang **70 hingga 90%**.

![image](https://github.com/RahinaBintang/RPS-Classification/blob/3e40ed59be32456eb4de90c79ed0c9f1ab31f84e/assets/CNN_loss.png)

Plot diatas menunjukkan bahwa loss dari training set stabil di **1.0**, sedangkan val_loss nya mengalami fluktuatif dengan rentang loss antara **0.4 hingga 1.0**.

![image](https://github.com/RahinaBintang/RPS-Classification/blob/6f64fbd6c815604bade74c3638a03cffdf60de8d/assets/cnn_model_classification_report.png)

Gambar diatas merupakan *Classification Report* dari Model setelah dilakukan *predict* terhadap *Testing Set*. Dapat dilihat bahwa Akurasinya mencapai **95%** dengan hasil prediksi pada label *'Rock'* dapat sempurna di **100% acc**.

### Inception-V3 Model ✨
**Preprocessing**

Preprocessing yang dilakukan antara lain adalah resizing **(299,299)** sesuai rekomendasi Inception-V3, lalu rescale / normalization dengan rentang 1./255, lalu melakukan augmentasi dengan parameter seperti *sheer_range* yang diatur ke **0.2**, *zoom_range* diatur ke **0.2**, dan *horizontal_flip*. Setelah augmentasi selesai dilakukan, langkah terakhir adalah *splitting* dataset menjadi 3 *(Training, Validation, dan Testing)* sesuai dengan penjelasan pada Dataset.

**Modelling & Evaluation**

Berikut hasil dari Model setelah dilakukan *Fine-Tuning* menggunakan dataset RPS :

![image](https://github.com/RahinaBintang/RPS-Classification/blob/558bab4e15a2eb63b924d00953009864e88059be/assets/Inception_acc.png)

Plot diatas menunjukkan bahwa *training_acc* stabil mendekati **100%**, namun *val_acc* nya cuma mencapai **94%**, hal ini menjadi indikasi bahwa model mengalami *overfitting*.

![image](https://github.com/RahinaBintang/RPS-Classification/blob/558bab4e15a2eb63b924d00953009864e88059be/assets/Inception_loss.png)

Dapat dilihat pada plot loss diatas. *Training dan Val Loss* sama - sama turun, namun val_loss cenderung lebih tinggi dibanding training_loss nya. Hal ini mungkin saja disebabkan karena terjadi *Overfitting* pada Model dan perlu dilakukan *tuning* lebih lanjut untuk menghilangkan *Overfit*.

![image](https://github.com/RahinaBintang/RPS-Classification/blob/558bab4e15a2eb63b924d00953009864e88059be/assets/inception_model_classification_report.png)

Gambar diatas menunjukkan *Classification Report* dari Model setelah dilakukan predict terhadap *Testing Set*. Terlihat bahwa Model sangat akurat dan lebih baik dari CNN Model dalam generalisasi data dengan Akurasi tepat **100%**.

## Local Web Deployment

### Tampilan HomePage

![image](https://github.com/RahinaBintang/RPS-Classification/blob/acad73dca7d4d8ca7e0a29add50b4cbb6addc189/assets/Home.png)

### Tampilan HomePage Setelah Upload Image

![image](https://github.com/RahinaBintang/RPS-Classification/blob/acad73dca7d4d8ca7e0a29add50b4cbb6addc189/assets/Upload%20Image.png)

### Tampilan Prediction Result

![image](https://github.com/RahinaBintang/RPS-Classification/blob/acad73dca7d4d8ca7e0a29add50b4cbb6addc189/assets/Prediction%20Result.png)

## Author 👨‍💻

- [@RahinaBintang](https://github.com/RahinaBintang)
