# Laporan Proyek Machine Learning: Rekomendasi Jenis Diet dan Resep Makanan 

# Nama : Muhammad Faishal Ali Dhiaulhaq

# Project Overview
## Latar Belakang
Kebutuhan makanan sangat penting untuk diperhatikan. Terdapat banyak bahan-bahan yang digunakan dalam meracik sebuah masakan. Dalam memilih bahan makanan perlu untuk memperhatikan beberapa hal yang dapat mempengaruhi lemak, kalori, dan hal-hal lainnya yang dapat mempengaruhi berat badan. Sebab jika tidak diperhatikan, akan menimbulkan kecemasan teridapnya kondisi obesitas. 

Saat ini banyak orang yang mengkonsumsi makanan secara berlebihan. Alasan dibalik mengkonsumsi makanan berlebihan ini diantaranya seperti emosi negatif, paparan makanan lezat dan sedap, ketidakmampuan dalam menahan asupan makanan, tidak merasa kenyang, keinginan akan makanan dan bahkan kecanduan makanan secara langsung (Vainik et al, 2019). Pola makan seperti itu ditambah juga tidak memperhatikan gizi yang terkandung pada makanan yang dikonsumsi dapat menyebabkan kegemukan dan obesitas.

Fakta menunjukkan bahwa obesitas di dunia meningkat tiga kali lipat sejak tahun 1975. Pada tahun 2016 lebih dari 1.9 miliar orang dewasa berumur 18 tahun lebih mengalami kegemukan dan 650 juta mengalami obesitas (Apriyanti et al, 2018).

Maka dari itu, perlu penyeimbang dalam setiap makanan yang kita konsumsi dengan kegiatan-kegiatan seperti olahraga, diet, dan lain sebagainya. Diet adalah pengobatan pertama dan paling penting karena sejarah diet persis dimulai sejak orang mulai memasak makanan. Kebanyakan orang memilih diet untuk menyembuhkan penyakitnya sebab:

1. Diet tidak menakutkan seperti operasi.
2. Diet memiliki fungsi sebagai langkah preventif selain kuratif.

Maka dari itu, perlu untuk menelaah tipe diet yang sesuai pada kondisi tubuh berdasarkan jenis makanan yang sesuai. 

## Ringkasan Tujuan Proyek
Dari pemaparan informasi di atas, maka perlu pengadaan suatu alat atau media untuk menyarankan masyarakat agar mengerti apa saja jenis makanan dengan resep-resep yang benar. Proses penyaranan ini menggunakan **teknik atau sistem rekomendasi** yang merekomendasikan jenis-jenis diet beserta contoh resep makanan. 

Dari dataset ini, akan dilakukan pengolahan serta pembuatan **algoritma rekomendasi hibrida *Mixed***  (*Content-Based Filtering*, dan *User-Based Filtering*) menggunakan *Machine Learning* yang akan memaksimalkan interaksi jenis diet dengan jenis-jenis diet lainnya. Hasil akhir akan memunculkan sekumpulan *Top-N Recommended Items*. Pada prosesnya, akan memaksimalkan penggunaan setiap fitur yang ada pada dataset yang ada.

Referensi:

  <u>[Pemilihan Menu Makanan untuk Diet dengan Pendekatan Algoritma Genetika](https://jptam.org/index.php/jptam/article/view/13393/10289)</u>

  <u>[Deteksi Objek pada Citra Makanan Sebagai Rekomendasi Diet Menggunakan Metode Mask R-CNN](https://journal.sinov.id/index.php/juitik/article/view/733/675)</u>
  
  <u>[Diet Sebagai Keseimbangan Hidup](https://jurnaldekonstruksi.id/index.php/dekonstruksi/article/view/195/148)</u>

# Business Understanding
Proyek ini dibuat untuk memberikan media berbasis sistem rekomendasi untuk masyarakat dalam memilih jenis makanan berdasarkan tipe diet yang dipilih dengan pertimbangan profil demografis masyarakat.

## Problem Statements

1. Fitur unik apa saja yang dapat digunakan sebagai pertimbangan sistem rekomendasi?
   
   Masalah ini mencakup peninjauan dataset yang ada untuk melihat deskripsi, tujuan, dan informasi lainnya pada setiap kolomnya untuk dipilih menjadi pertimbangan data untuk model *Machine Learning* yang akan dibuat.

2. Bagaimana algoritma *Content-Based Filtering* dan *User-Based Filtering* dapat menyimpulkan sebuah rekomendasi?
  
  Masalah ini mencakup cara penyajian akhir dari proses sistem itu sendiri ketika mengolah dari data mentah, data *model-friendly*, hingga data jadi untuk dikonsumsi masyarakat pengguna.

## Goals

1. Memaknai setiap fitur yang ada untuk diambil fitur paling masuk akal jika masyarakat mencari rekomendasi tipe diet dengan detail-detail lainnya.
   
   Pemaknaan fitur menggunakan langkah-langkah eksplorasi, penggabungan beberapa kolom yang berpotensi, serta vektorisasi untuk mencari korelasi umum yang dapat menjadi nilai pertimbangan rekomendasi. Ditambah dengan data-data demografis dari masyarakat pengguna.

2. Membuat model untuk sistem rekomendasi dengan algoritma *Content-Based Filtering* dan *User-Based Filtering* yang baik dalam merekomendasikan tipe diet yang sesuai.
   
   Pembuatan model dengan *Content-Based Filtering* dan *User-Based Filtering* menggunakan data-data yang sudah ditelaah sebelumnya. Dengan tambahan melakukan *setting* pada model *deep learning*-nya agar menghasilkan akurasi yang tinggi.

## Solution Approach

1. Melakukan pemisahan data fitur yang digunakan dengan yang tidak pada **dataset diet dan *users***. Pada **dataset diet**, pemilihan fitur akan ditujukan pada pencarian korelasi antar fitur, serta mengambil fitur dengan potensi nilai pertimbangan terbaik untuk dilakukan proses rekomendasi. Sedangkan pada **dataset *users***, pemilihan fitur ditujukan untuk memberikan data tambahan agar hasil rekomendasi lebih meyakinkan. Disebabkan data-data tersebut dapat mendukung hasil rekomendasi (Data yang dimaksud adalah data demografis masyarakat pengguna). 
2. Membuat analisis data dengan visualisasi data hasil dari tinjauan fitur-fitur sebelumnya, untuk memperoleh *insight* pada data. Dan juga melakukan pengecekan korelasi dan vektorisasi pada setiap fitur yang dipilih.
3. Membuat model sistem rekomendasi sebagai berikut:

   - *Content-Based Filtering*
      
      Pada model ini, data yang digunakan berasal dari **dataset diet** yang sudah terstruktur dan *model-friendly*. Hasil dari model ini yaitu rekomendasi tipe-tipe diet dengan informasi lainnya. Tujuan hasil dari model ini untuk mengatasi kondisi *Cold Start* di awal sistem dimulai.

   - *User-Based Filtering* 

      Pada model ini, data yang digunakan berasal dari **dataset *users*** yang sudah terstruktur dan *model-friendly*. Hasil dari model ini yaitu data pendukung atau juga pengganti model *Content-Based Filtering*. Pergantiannya ditandai dengan algoritma yang condong merekomendasikan tipe diet berdasarkan tipe diet yang dipilih oleh orang lain dengan data demografis yang mirip.
4. Mengintegrasikan kedua algoritma yang sudah dibuat dengan dataset-dataset yang ada, agar dapat bekerja secara bergantian sesuai dengan kondisi yang ada. Pengintegrasian menjadikan kedua algoritma di atas menjadi *Collaborative Filtering* ditambah dengan metode *matrix factorization* dan *deep learning*.
5. Menggunakan metrik akurasi pada *library* **Tensorflow** hasil proses *training* dan *testing* pada data yang ada. Kisaran besar akurasi yang dituju adalah yang paling maksimal, dengan pertimbangan hasil rekomendasi yang muncul.