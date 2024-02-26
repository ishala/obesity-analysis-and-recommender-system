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

# Data Understanding
Pada bagian ini. akan memberikan informasi terkait data yang digunakan untuk analisis. Berikut detailnya:

## Informasi Data
   Terdapat dua jenis data yang digunakan pada analisis ini, yaitu:
   1. Data sumber-terbuka (*open source*) dengan judul **Diet, Recipes And Their Nutrients** yang memuat informasi jenis masakan sehat yang sesuai dengan jenis diet yang beragam. Terdapat informasi nilai gizi yang terkandung pada setiap jenis masakan yang ada pada data. Data ini dikumpulkan oleh **The Devastator**. Dari sumbernya, terbagi menjadi beberapa dataset per kategori diet. Yang digunakan hanya pada dataset *all diets*. Kondisi awal data sudah cukup bersih, dengan beberapa nilai *outliers* yang masih kurang baik. Butuh beberapa langkah penanangan hingga data benar-benar bersih.

      Informasi Lanjutan:

      - Jumlah Baris: 7806
      - Jumlah Kolom: 8

      Dengan penjelasan fitur dan variabel di dalam datset ditunjukkan pada **Tabel 1.a**.

      **Tabel 1.a Penjelasan Fitur dan Variabel Pada Dataset Diet**

      | No. | Nama Kolom | Deskripsi|
      |:--:|:--:|:-|
      | 1. | Diet_type | Tipe diet yang bersangkutan dengan satu baris data|
      | 2. | Recipe_name | Nama resep makanan |
      | 3. | Cuisine_type | Asal daerah resep makanan |
      | 4. | Protein(g) | Banyak protein yang terkandung pada masakan dalam satuan *gram* |
      | 5. | Carbs(g) | Banyak karbohidrat yang terkandung pada masakan dalam satuan *gram* |
      | 6. | Fat(g) | Banyak lemak yang terkandung pada masakan dalam satuan *gram* |
      | 7. | Extraction_day | Tanggal resep dibuat |
      | 8. | Extraction_time | Waktu resep dibuat |

      [Link Dataset Diets, Recipes And Their Nutrients](https://www.kaggle.com/datasets/thedevastator/healthy-diet-recipes-a-comprehensive-dataset?select=All_Diets.csv)

      Fitur-fitur yang digunakan untuk sistem rekomendasi adalah **Diet_type, Recipe_name, Cuisine_type, Protein(g), Carbs(g)**, dan **Fat(g)**. Fitur **Diet_type, Recipe_name,** dan **Cuisine_type** digunakan sebagai fitur utama untuk merekomendasikan pengguna dalam memilih jenis masakan berdasarkan tipe dietnya untuk rekomendasi *Content-based Filtering*.

   2. Data sumber-terbuka (*open source*) dengan judul **Obesity Dataset Cleaned and Data Sinthetic** yang memuat tentang informasi gaya hidup penduduk di Mexico, Peru, dan Colombia. Data ini dikumpulkan oleh **ScienceDirect** dibawah lisensi Creative Commons. Kondisi awal data sudah cukup bersih, dengan sedikit nilai *outliers* yang dapat dengan mudah dibersihkan.
   
      Informasi lanjutan:
      - Jumlah Baris: 2111
      - Jumlah kolom: 19

      Dengan penjelasan fitur dan variabel didalam dataset ditunjukkan pada **Tabel 1.b**.

      **Tabel 1.b Penjelasan Fitur dan Variabel Pada Dataset**

      | No. | Nama Kolom | Deskripsi |
      |:--:|:-:|:-|
      | 1. | Id | Kolom index pada setiap baris data |
      | 2. | BMI | Indeks masa tubuh ideal |
      | 3. | Gender | Jenis Kelamin target yang diobservasi  |
      | 4. | Age | Usia target yang diobservasi  |
      | 5. | Height | Tinggi badan dalam satuan *inch* target yang diobservasi |
      | 6. | Weight | Tinggi badan dalam satuan *inch* target yang diobservasi |
      | 7. | family_history_with_overweight | Riwayat keluarga dengan berat badan berlebih (obesitas) |
      | 8. | FAVC | Frekuensi mengkonsumsi makanan tinggi kalori target yang diobservasi |
      | 9. | FCVC | Frekuensi mengkonsumsi sayur-mayur target yang diobservasi |
      | 10. | NCP | Jumlah makan pokok perhari target yang diobservasi |
      | 11. | CAEC | Frekuensi makan cemilan target yang diobservasi |
      | 12. | SMOKE | Kebiasaan merokok target yang diobservasi |
      | 13. | CH2O | Jumlah minum air target yang diobservasi |
      | 14. | SCC | Kebiasaan monitoring konsumsi kalori target yang diobservasi |
      | 15. | FAF | Frekuensi kegiatan fisik target yang diobservasi |
      | 16. | TUE | Waktu penggunaan perangkat dalam satuan *jam* target yang diobservasi |
      | 17. | CALC | Frekuensi mengkonsumsi alkohol target yang diobservasi |
      | 18. | MTRANS | Kategori transportasi yang digunakan target yang diobservasi |
      | 19. | NObeyesdad | Kategori berat badan |

      [Link Dataset Obesity Dataset Cleaned and Data Sinthetic](https://www.kaggle.com/datasets/mandysia/obesity-dataset-cleaned-and-data-sinthetic)

      Fitur-fitur yang digunakan adalah **Id, BMI, Weight, Gender, Age, NObeyesdad,** dan **family_history_with_overweight** sebagai data demografis pengguna untuk rekomendasi *User-based Filtering*.

   ## Pembersihan dan Persiapan Data
   Pada prosesnya, pembersihan dan persiapan data terbagi menjadi beberapa tahapan. Berikut detailnya:

   ### Data Loading
   Pada proses ini, dilakukan proses pemuatan data ke dalam *workspace* yang digunakan, pada kasus ini adalah *notebook*.

   ### Data Assessing 

   Pada proses ini, dilakukan penilaian pada kelayakan data. Hal ini terdiri dari beberapa aspek pengecekan. Berikut detailnya:

   1. Penilaian Dataset Awal

      Pada tahap ini, yang dilakukan adalah melihat informasi keseluruhan dari dataset seperti nama kolom, jumlah data per kolom, tipe data kolom, dan lain-lain. 

      **Data Diet** 

      Informasi penting pada data ini sudah disajikan pada **Tabel 2.a**.

      **Tabel 2.a Informasi Tipe Data dan Jumlah Kolom Data Diet**

      | Tipe Data Kolom | Jumlah Kolom |
      |:----------:|:----------:|
      | Object |    5    |
      | Float |    3    |

      **Data *Users***

      Informasi penting pada data ini sudah disajikan pada **Tabel 2.b**

      **Tabel 2.b Informasi Tipe Data dan Jumlah Kolom Data *Users***
      | Tipe Data Kolom | Jumlah Kolom |
      |:----------:|:----------:|
      | Object |    14    |
      | Float |    3    |
      | Integer |    2    |

   2. Pengecekan Data *Null*

      Pada tahap ini, dilakukan peninjauan terhadap nilai-nilai baris yang ada di setiap kolom pada setiap dataset. Tujuannya adalah untuk melihat banyak nilai *null* disetiap kolomnya. Setelah dilakukan pengecekan, data sudah bersih dari data *null*.

   3. Pengecekan Data Duplikat

      Pada tahap ini, dilakukan peninjauan pada nilai-nilai yang terduplikasi secara *unique* pada setiap dataset. Tujuannya adalah untuk mengurangi distorsi pada data akibat adanya data duplikat. Hasil pemeriksaan sudah tidak ditemukan nilai duplikat dari keseluruhan kolom.

   4. Deskripsi Nilai Statistik Dataset

      Pada tahap ini, dilakukan identifikasi awal nilai-nilai statisktik pada kolom numerik di setiap dataset.

      **Data Diet**

      Informasi nilai statistik pada data ini ditunjukkan pada **Tabel 3.a**

      **Tabel 3.a Informasi Nilai Statistik Data Diet**
      |  | Protein(g) | Carbs(g) | Fat(g) |
      |:-|:-:|:-:|:-:|
      | count | 7806 | 7806 | 7806 |
      | mean  | 83.231498  | 152.123189 | 117.328542 |
      | std   | 89.797282  | 185.907322 | 122.098117 |
      | min   | 0.000000  | 0.060000 | 0.000000 |
      | 25%   | 24.415000  | 36.162500 | 41.067500 | 
      | 50%   | 56.280000 | 93.415000 | 84.865000 |
      | 75%   | 112.357500 | 205.915000 | 158.290000 |
      | max   | 1273.610000 | 3405.550000 | 1930.240000 |

      Dari hasil pengecekan data-data tak lazim pada data diet menggunakan beberapa langkah pengecekan, terdeteksi masih terdapat data duplikat yang perlu dibersihkan.

      **Data *Users***

      Informasi nilai statistik pada data ini ditunjukkan pada **Tabel 3.b**

      **Tabel 3.b Informasi Nilai Statistik Data Diet**
      |  | Age | Height | Weight | NCP | BMI |
      |:-|:-:|:-:|:-:|:-:|:-:|
      | count | 2111 | 2111 | 2111 | 2111 | 2111 |
      | mean  | 24.315964  | 1.701677 | 86.588820 | 2.687826 | 29.700159 |
      | std   | 6.357078  | 0.093305 | 26.188572 | 0.809680 | 8.011337 |
      | min   | 14.000000  | 1.450000 | 39.000000 | 1.000000 | 12.998685 |
      | 25%   | 20.000000  | 1.630000 | 65.500000 | 3.000000 | 24.325802 |
      | 50%   | 23.000000 | 1.700499 | 83.000000 | 3.000000 | 28.719089 |
      | 75%   | 26.000000 | 1.768464 | 107.000000 | 3.000000 | 36.016501 |
      | max   | 61.000000 | 1.980000 | 173.000000 | 4.000000 | 50.811753 |

      Dari hasil pengecekan data-data tak lazim pada data *users* menggunakan beberapa langkah pengecekan, terdeteksi masih terdapat kesalahan tipe data pada kolom **Weight**.
   
   ### Data Cleaning

   Pada tahap ini, terdapat dua langkah yang dilakukan, yaitu:
   1. Menghapus data duplikat pada dataset diet.
   2. Mengubah tipe data kolom **Weight** pada dataset *users*.
   
   ### Exploratory Data Analysis (EDA)

   Pada proses ini, terdapat beberapa langkah yang dilakukan. Tujuannya adalah memudahkan untuk mengenali dataset dengan pengelompokan dan penyajian secara visual. Berikut detailnya:

   1. Menghapus Kolom yang Tidak Perlu
      
      Tahap ini bertujuan untuk mengurangi dimensi dataset tidak terlalu besar, dengan begitu dataset dapat dimuat lebih cepat dan ringan.

      Setelah dilakukan pengurangan jumlah kolom, saat ini datset terdiri dari:

      1. Dataset Diet

         Saat ini, dataset diet hanya terdiri dari 6 kolom yaitu:
         - Diet_type
         - Recipe_name
         - Cuisine_type
         - Protein(g)
         - Carbs(g)
         - Fat(g)
      2. Dataset *Users*

         Saat ini, dataset *Users* hanya terdiri dari 7 kolom yaitu:
         - Id
         - BMI
         - Weight
         - Gender
         - Age
         - NObeyesdad
         - family_history_with_overweight
  
   2. Pencarian Invalid dan Missing Value Lanjutan

      Pada tahap ini dilakukan pemeriksaan nilai-nilai yang tidak sesuai dengan tujuan analisis. 

      - Dataset Diet
      
         Pada **dataset diet**, pemeriksaan nilai tidak valid dengan melihat nilai *unique* di setiap kolom kategorikal. Hasilnya tidak ditemukan nilai yang aneh dan semua data sesuai.
      
         Lalu pada kolom numerik, dilakukan pengecekan pada angka kurang dari atau sama dengan 0. Ditemukan terdapat nilai tersebut pada kolom **Protein(g)** dan **Fat(g)**. Yang dilakukan adalah menghapus nilai-nilai itu pada kolom **Protein(g)** dan mempertahankan nilai-nilai yang ada pada kolom **Fat(g)**, sebab menyesuaikan tujuan analisis yaitu merekomendasikan masakan-masakan sehat dan rendah nilai gizi yang menyebabkan obesitas bagi pengguna yang ingin diet.

         Setelah langkah-langkah di atas, dapat disimpulkan bahwa **dataset diet** sudah bersih dan siap diproses pada langkah selanjutnya.

      - Dataset *Users*
      
         Pada **dataset *users***, pemeriksaan nilai tidak valid dengan melihat nilai *unique* di setiap kolom kategorikal. Hasilnya tidak ditemukan nilai yang aneh dan semua data sesuai.

         Lalu pada kolom numerik, dilakukan pengecekan angka kurang dari atau sama dengan 0. Juga tidak ditemukan nilai kurang dari atau sama dengan 0. 

         Setelah langkah-langkah di atas, dapat disimpulkan bahwa **dataset *users*** sudah bersih dan siap diproses pada langkah selanjutnya.
   
   3. Pencarian Nilai *Outliers*

      Pada proses ini, terdapat beberapa langkah untuk mengidentifikasi nilai *outliers* pada setiap kolom numerik yang akan digunakan untuk fitur-fitur *modelling*. Sebab, jika tidak dibersihkan akan memberikan kualitas data dan model yang tidak maksimal.

      Dalam mengidentifikasi nilai *outliers*, dilakukan pengecekan dengan visualisasi data. Visualisasi menggunakan ***box plot***. Jenis plot ini umum digunakan untuk menampilkan distribusi data. 

      -  Dataset Diet
         
         Tampilan visualisasi data ditunjukkan pada **Gambar 1.a, 2.a, dan 3.a**.

         **Gambar 1.a Pencarian *Outliers* Kolom Protein(g)**

         ![Hasil Protein(g) 1](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/e0f97a5c-8c41-405a-806a-333cf10c0ba5)


         **Gambar 2.a Pencarian *Outliers* Kolom Carbs(g)**

         ![Hasil Carbs(g) 1](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/e080a8de-4e06-481a-b522-4ab523a5de15)


         **Gambar 3.a Pencarian *Outliers* Kolom Fat(g)**

         ![Hasil Fat(g) 1](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/601ee799-1980-4ad2-9236-20ea8ab4d883)


         Dari hasil di atas, terdapat banyak sekali nilai *outliers* dari semua kolom yang ada. Maka selanjutnya, perlu untuk menanganinya dengan cara dihapus menggunakan metode **IQR (Inter Quartile Range)**.

      -  Dataset *Users*

         Tampilan visualisasi data ditunjukkan pada **Gambar 1.b, 2.b, dan 3.b**.

         **Gambar 1.b Pencarian *Outliers* Kolom BMI**

         ![Hasil BMI 1](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/a21b7ec9-9eda-4903-bf9f-c1cc7430b526)

         
         **Gambar 2.b Pencarian *Outliers* Kolom Weight**

         ![Hasil Weight 1](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/fcb8ee56-11b0-4fcc-9ce9-1c757fcc39ad)


         **Gambar 3.b Pencarian *Outliers* Kolom Age**

         ![Hasil Age 1](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/99f00b35-71ab-4b89-93c3-5de20a335511)


         Dari hasil di atas, terdapat 1 nilai *outlier* pada kolom **Weight** dan beberapa nilai *outliers* pada kolom **Age**. Maka selanjutnya, perlu untuk menanganinya dengan cara dihapus menggunakan metode **IQR (Inter Quartile Range)**.
   
   4. Penanganan *Outliers*

      Pada proses ini, dilakukan identifikasi dan eliminasi nilai-nilai *outlier* yang ada di dalam fitur-fitur yang akan digunakan dalam *modeling*. Terdapat banyak cara atau rumus dalam mengeliminasinya. Namun, disini akan menggunakan metode IQR atau *Inter Quartile Range*.

      Rumus IQR:

      $IQR = Q3 - Q1$

      Penjelasan:

      $Q1$ = Kuartil pertama dari data (25%)

      $Q3$ = Kuartil ketiga dari data (75%)

      $IQR$ = Inter Quartile Range, jarak antara kuartil 1 dan 3
   
   5. Pencarian Nilai *Outliers* Lanjut.

      Setelah dilakukan penghapusan nilai *outliers* pada tahap sebelumnya, lalu diperiksa lagi dengan visualisasi data menggunakan *box plot*. 

      - Dataset Diet
         
         Tampilan visualisasi data ditunjukkan pada **Gambar 4.a, 5.a, dan 6.a**.

         **Gambar 4.a Pencarian Ulang *Outliers* Kolom Protein(g)**

         ![Hasil Protein(g) 2](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/c966088e-1ccf-4e67-812c-dda71e87d76b)


         **Gambar 5.a Pencarian Ulang *Outliers* Kolom Carbs(g)**

         ![Hasil Carbs(g) 2](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/efa68532-53da-4191-82fc-2735777bc43d)


         **Gambar 6.a Pencarian Ulang *Outliers* Kolom Fat(g)**

         ![Hasil Fat(g) 2](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/f717b31e-a75f-48c0-a373-fa0efd3ad437)


         Dari hasil di atas, ternyata masih tetap ada banyak nilai *outliers* ditemukan. Maka perlu dilakukan penerapan rumus IQR lagi.

      - Dataset *Users*

         Tampilan visualisasi data ditunjukkan pada **Gambar 4.b, 5.b, dan 6.b**.

         **Gambar 4.b Pencarian Ulang *Outliers* Kolom BMI**

         ![Hasil BMI 2](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/abf53549-74f5-4c72-a0d1-eedc2273b187)


         **Gambar 5.b Pencarian Ulang *Outliers* Kolom Weight**

         ![Hasil Weight 2](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/687b5981-7615-4e14-8a66-b71adda8f6dc)


         **Gambar 6.b Pencarian Ulang *Outliers* Kolom Age**

         ![Hasil Age 2](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/fd8d1281-035a-4da4-b8f1-f86306d09710)


         Dari hasil di atas, sudah tidak ditemukan nilai *outliers* pada setiap kolom yang ada. Maka dapat disimpulkan bahwa dataset *users* sudah dapat digunakan pada tahap selanjutnya.
   
   6. Penanganan Sisa Nilai *Outliers* pada Dataset Diet
      
      Pada nilai *outliers* di dataset diet, perlu dilakukan penerapan rumus IQR secara berulang. Disini sudah dilakukan pengecekan banyak iterasi perulangan sehingga nilai *outliers* tidak ditemukan lagi. Banyak perulangannya yaitu **8 kali**. Hasilnya ditunjukkan pada **Gambar 7, 8, dan 9**.

      **Gambar 7 Pencarian *Outliers* Khusus Dataset Diet Kolom Protein(g)**

      ![Hasil Protein(g) 3](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/b51f825a-965e-493a-bf17-ab3c5d98a004)


      **Gambar 8 Pencarian *Outliers* Khusus Dataset Diet Kolom Carbs(g)**

      ![Hasil Carbs(g) 3](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/d4aea19a-c60c-4b2b-98df-d3404a38a918)


      **Gambar 9 Pencarian *Outliers* Khusus Dataset Diet Kolom Fat(g)**

      ![Hasil Fat(g) 3](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/2984616f-2c25-44d3-b06e-897860b53145)


      Dari hasil di atas, terlihat bahwa sudah tidak ditemukan nilai *outliers* lagi pada dataset diet. Dapat disimpulkan bahwa dataset diet sudah dapat digunakan pada tahap selanjutnya.

   7. Pencarian *Insight* Pada Data

      Setelah dilakukan pencarian nilai *outliers*, langkah selanjutnya adalah mencari tahu gambaran umum pada data. Dengan mengetahui rasio besaran setiap data pada setiap kolomnya. Dengan begitu, akan menampilkan informasi mengenai frekuensi banyak setiap nilai *unique* pada setiap kolomnya. Proses yang dilakukan adalah ekstraksi fitur menggunakan *Univariate Analysis*.

      **Kolom Kategorikal**
      - Dataset Diet
         
         **Kolom Diet_type**

         Tujuan dari analisis pada kolom ini untuk mengetahui besar presentase pada setiap jenis diet yang ada. Untuk Informasi besar presentase dan visualisasi datanya ditunjukkan pada **Tabel 4** dan **Gambar 10**.

         **Tabel 4. Besar Presentase dan Jumlah Data *Unique* Kolom Diet_type Dataset Diet**

         | Tipe Diet | Jumlah Sampel | Presentase |
         |:--:|:--:|:--:|
         | mediterranean | 1370 | 23% |  
         | dash | 1354 | 22.7% |  
         | vegan | 1148 | 19.3% |  
         | keto | 1104 | 18.5% |  
         | paleo | 984 | 16.5% | 

         **Gambar 10. Visualisasi Rasio Besar Tiap Data *Unique* Kolom Diet_type Dataset Diet** 

         ![Uni Diet_type](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/b40a757c-0f36-454f-994f-9b6ae748cb67)


         Dari hasil di atas, tipe diet **mediterranean** memiliki besar presentase tertinggi dibandingkan data lainnya. Dengan jenis **paleo** memiliki presentase paling sedikit.

         **Kolom Cuisine_type**

         Tujuan dari analisis pada kolom ini untuk mengetahui besar presentase pada setiap jenis masakan yang ada berdasarkan daerahnya. Untuk informasi besar presentase dan visualisasi datanya ditunjukkan pada **Tabel 5** dan **Gambar 11**.

         **Tabel 5. Besar Presentase dan Jumlah Data *Unique* Kolom Cuisine_type Dataset Diet**

         | Tipe Masakan | Jumlah Sampel | Presentase |
         |:--:|:--:|:--:|
         | american | 2057 | 34.5% |  
         | mediterranean | 1414 | 23.7% |  
         | italian | 592 | 9.9% |  
         | french | 466 | 7.8% |  
         | others | 1431 | 24.0% |

         **Gambar 11. Visualisasi Rasio Besar Tiap Data *Unique* Kolom Cuisine_type Dataset Diet** 

         ![Uni Cuisine_type](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/370736f1-8050-42db-bd45-3eb1f86456c0)


         Dari hasil di atas, jenis makanan **american** memiliki besar presentase tertinggi dibandingkan dengan data lainnya. Dengan jenis **others** menjadi urutan paling akhir. Jenis **others** merupakan hasil penjumlahan presentase jenis-jenis makanan yang memiliki presentase kurang dari 5%.

      - Dataset *Users*

         **Kolom Gender**
         
         Tujuan dari analisis kolom ini untuk mengetahui besar presentase pada setiap jenis kelamin pada dataset ini. Untuk informasi besar presentase dan visualisasi datanya ditunjukkan pada **Tabel 6** dan **Gambar 12**.

         **Tabel 6. Besar Presentase dan Jumlah Data *Unique* Kolom Gender Dataset *Users***

         | Jenis Kelamin | Jumlah Sampel | Presentase |
         |:--:|:--:|:--:|
         | male | 1003 | 51.4% |  
         | female | 947 | 48.6% |  
         
         **Gambar 12. Visualisasi Rasio Besar Tiap Data *Unique* Kolom Gender Dataset Diet**

         ![Uni Gender](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/dd51c16b-f5f7-468c-85b9-0fc06c6ad886)


         Dari hasil di atas, jenis kelamin **Laki-laki** memiliki besar presentase lebih tinggi dibandingkan dengan jenis kelamin **Perempuan**. 

         **Kolom NObeyesdad**

         Tujuan dari analisis kolom ini untuk mengetahui besar presentase pada setiap jenis kategori berat badan pengguna yang sudah ada pada dataset ini. Untuk informasi besar presentase dan visualisasi datanya ditunjukkan pada **Tabel 7** dan **Gambar 13**.

         **Tabel 7. Besar Presentase dan Jumlah Data *Unique* Kolom NObeyesdad Dataset *Users***

         | Jenis Berat Badan | Jumlah Sampel | Presentase |
         |:--:|:--:|:--:|
         | obesity_type_iii | 323 | 16.6% |  
         | obesity_type_i | 283 | 14.5% |
         | normal_weight | 280 | 14.4% |
         | overweight_level_i | 271 | 13.9% |
         | insufficient_weight | 271 | 13.9% |
         | obesity_type_ii | 268 | 13.7% |
         | overweight_level_ii | 254 | 13.0% |

         **Gambar 13. Visualisasi Rasio Besar Tiap Data *Unique* Kolom NObeyesdad Dataset Diet**

         ![Uni NObeyesdad](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/aab9b422-cdf5-4a62-b56b-c3661ec074dc)


         Dari hasil di atas, jenis berat badan **tipe obesitas 3** memiliki presentase tertinggi dengan disusul jenis berat badan lainnya. Presentase paling rendah ada pada **tipe obesitas 2**.

         **Kolom family_history_with_overweight**

         Tujuan dari analisis kolom ini untuk mengetahui besar presentase pada setiap kategori pengguna dengan keturunan obesitas dan yang tidak memiliki keturunan obesitas. Untuk informasi besar presentase dan visualisasi datanya ditunjukkan pada **Tabel 8** dan **Gambar 14**.

         | Pengguna Dengan Keturunan Obesitas | Jumlah Sampel | Presentase |
         |:--:|:--:|:--:|
         | Ya | 1578 | 80.9% |  
         | Tidak | 372 | 19.1% |  

         **Gambar 14. Visualisasi Rasio Besar Tiap Data *Unique* Kolom family_history_with_overweight Dataset Diet**

         ![Uni family_history_with_overweight](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/4f11bac0-e7ff-4cdd-a37c-99df78b7c56f)


         Dari hasil di atas, **pengguna dengan keturunan obesitas** memiliki presentase lebih tinggi daripada **pengguna tidak memiliki keturunan obesitas**.

      **Kolom Numerikal**
       
       Tujuan dari analisis ini untuk melihat distribusi umum data yang ada pada dataset ini setelah melalui proses **Univariate Analysis**. Dataset sudah dilakukan pembersihan *missing value*, *invalid value*, dan juga *outliers value*.

         - Dataset Diet

            **Gambar 14. Visualisasi Distribusi Data Kolom Numerikal Dataset Diet**

            ![Uni Numerical](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/9436e8b3-103a-425f-abf2-33c38a4c9e73)


            Dari hasil pemetaan dengan visualisasi data pada **Gambar 14**, dapat disimpulkan bahwa:
            1. Kolom Protein(g)
               - Persebaran data cenderung ke kanan (*Right-Skewed*)
               - Banyak data terbanyak ada di angka 10
               - Banyak data terendah ada di kisaran angka 150 - 175

            2. Kolom Carbs(g)
               - Persebaran data cenderung ke kanan (*Right-Skewed*)
               - Banyak data terbanyak ada di angka 20
               - Banyak data terendah ada di kisaran angka 300 - 350

            3. Kolom Fat(g)
               - Persebaran data cenderung ke kanan (*Right-Skewed*)
               - Banyak data terbanyak ada di angka 10
               - Banyak data terendah ada di kisaran angka 200 - 250
        
         - Dataset *Users*

            **Gambar 15. Visualisasi Distribusi Data Kolom Numerikal Dataset *Users***
            
            ![Uni Numerical](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/975a987c-3b38-43dc-a5cd-36f08c8c4a0e)


            Dari hasil pemetaan dengan visualisasi data pada **Gambar 15**, dapat disimpulkan bahwa:

            1. Kolom BMI
               - Pada kolom BMI persebaran banyak data cenderung rata. Dengan perolehan banyak data terbanyak ada di kisaran angka 18.
               - Banyak BMI terendah ada di angka 50.
            2. Kolom Weight
               - Pada kolom Weight persebaran banyak data cenderung miring ke kanan (*right-skewed*). Dengan perolehan banyak data terbanyak ada di kisaran angka 50 dan 80.
                - Banyak angka terendah ada di kisaran angka 140 - 160.
            3. Kolom Age
               - Pada kolom Age persebaran banyak data cenderung miring ke kanan (*right-skewed*). 
               - Banyak data terbanyak ada pada angka 21.
               - Banyak data terendah ada di kisaran angka 28 - 35.
