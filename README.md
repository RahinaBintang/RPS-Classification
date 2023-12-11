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

Preprocessing yang dilakukan antara lain adalah resizing (128,128), lalu rescale / normalization dengan rentang 1./255, dilanjut dengan melakukan splitting dataset menjadi 3 *(Training, Validation, dan Testing)* sesuai dengan penjelasan pada Dataset.

**Modelling**

Hasil dari CNN Model yang telah dibangun adalah sebagai berikut :

![image](https://github.com/RahinaBintang/RPS-Classification/blob/38badf24f75925826aa7e54a3568889d39ca1330/assets/summary_cnn_model.png)

**Model Evaluation**

Berikut adalah hasil dari fitting CNN Model yang telah dibangun :

![image](https://github.com/RahinaBintang/RPS-Classification/blob/3e40ed59be32456eb4de90c79ed0c9f1ab31f84e/assets/CNN_acc.png)

Plot diatas menunjukkan bahwa training acc dapat stabil diatas 95%, namun validation acc nya mengalami fluktuatif acc pada rentang 70 hingga 90%.

![image](https://github.com/RahinaBintang/RPS-Classification/blob/3e40ed59be32456eb4de90c79ed0c9f1ab31f84e/assets/CNN_loss.png)

Plot diatas menunjukkan bahwa loss dari training set stabil di 1.0, sedangkan val_loss nya mengalami fluktuatif dengan rentang loss antara 0.4 hingga 1.0

![image](https://github.com/RahinaBintang/RPS-Classification/blob/6f64fbd6c815604bade74c3638a03cffdf60de8d/assets/cnn_model_classification_report.png)

Gambar diatas merupakan *Classification Report* dari Model setelah dilakukan *predict* terhadap *Testing Set*. Dapat dilihat bahwa Akurasinya mencapai 95% dengan hasil prediksi pada label *'Rock'* dapat sempurna di 100% acc.

### Inception-V3 Model ✨
Preprocessing
Modelling

## Local Web Deployment
