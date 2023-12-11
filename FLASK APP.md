# Flask App Documentation
Dokumentasi ini memberikan penjelasan rinci tentang kode aplikasi web Flask yang digunakan untuk klasifikasi gambar. Ini mencakup struktur, dependensi, konfigurasi, dan fungsionalitas aplikasi.

## Overview
Aplikasi web Flask memungkinkan pengguna mengunggah gambar dan menerima prediksi dari model Convolutional Neural Networks (CNN) dan InceptionV3 yang telah dilatih sebelumnya. Model-model ini digunakan untuk mengklasifikasikan gambar yang diunggah ke dalam kategori: 'Kertas', 'Batu', dan 'Gunting'.

## Dependensi
Aplikasi bergantung pada perpustakaan Python berikut:
- **Flask**: Kerangka kerja web untuk membangun aplikasi web.
- **TensorFlow** dan **Keras**: Perpustakaan untuk pembelajaran mesin dan jaringan saraf.
- **Werkzeug**: Perpustakaan utilitas untuk aplikasi WSGI (Web Server Gateway Interface).
- **Pillow**: Perpustakaan Python yang digunakan untuk pemrosesan gambar

## Konfigurasi
Aplikasi memiliki konfigurasi berikut:

- **UPLOAD_FOLDER**: Direktori tempat gambar yang diunggah disimpan (static/uploads).
- **ALLOWED_EXTENSIONS**: Ekstensi file yang diperbolehkan untuk unggahan gambar ({'jpg', 'jpeg', 'png'}).

Model-model ***CNN*** dan ***InceptionV3*** dimuat selama awal startup aplikasi.

## Struktur File
- **app.py**: Berkas aplikasi utama yang berisi rute dan fungsi.
- **models/**: Direktori yang berisi model-model CNN dan InceptionV3 yang telah dilatih.
- **static/uploads/**: Direktori tempat gambar yang diunggah disimpan.
- **templates/**: Direktori yang berisi templat HTML untuk merender halaman web.

## Route dan Function

### '/' - Halaman Utama (upload_page function)
- Merender halaman utama (upload.html) untuk mengunggah gambar.

### '/upload' - Unggah Gambar (upload_file function)
- Menerima permintaan POST dengan gambar yang diunggah.
- Memvalidasi tipe file dan menyimpan gambar ke direktori unggahan.
- Merender halaman unggah dengan gambar yang diunggah.

### '/predict' - Prediksi (predict function)
- Menerima permintaan GET dan POST.
- Mendapatkan gambar yang diunggah dan model yang dipilih.
- Melakukan praproses gambar berdasarkan model yang dipilih.
- Menggunakan model yang dipilih untuk klasifikasi gambar.
- Merender halaman prediksi (predict.html) dengan nama file dan kelas yang diprediksi.

### Catatan
- Aplikasi mendukung dua model yang telah dilatih: CNN dan InceptionV3.
- Praproses gambar disesuaikan berdasarkan model yang dipilih.
- Prediksi ditampilkan berdasarkan skor kepercayaan tertinggi atau ambang batas untuk setiap kelas.

## Menjalankan App
- Jalankan skrip dengan python app.py.
- Akses aplikasi di peramban Web dengan alamat http://127.0.0.1:5000/.

## Author 👨‍💻
- [@RahinaBintang](https://github.com/RahinaBintang)
