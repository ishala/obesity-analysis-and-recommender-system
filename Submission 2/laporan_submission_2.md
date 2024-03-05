# Laporan Proyek Machine Learning: Rekomendasi Resep Makanan Untuk Diet Berdasarkan Data Demografis Masyarakat

# Nama : Muhammad Faishal Ali Dhiaulhaq

# Project Overview
## Latar Belakang
Kebutuhan makanan sangat penting untuk diperhatikan. Terdapat banyak bahan-bahan yang digunakan dalam meracik sebuah masakan. Dalam memilih bahan makanan perlu untuk memperhatikan beberapa hal yang dapat mempengaruhi lemak, kalori, dan hal-hal lainnya yang dapat mempengaruhi berat badan. Sebab jika tidak diperhatikan, akan menimbulkan kecemasan teridapnya kondisi obesitas. 

Saat ini banyak orang yang mengkonsumsi makanan secara berlebihan. Alasan dibalik mengkonsumsi makanan berlebihan ini diantaranya seperti emosi negatif, paparan makanan lezat dan sedap, ketidakmampuan dalam menahan asupan makanan, tidak merasa kenyang, keinginan akan makanan dan bahkan kecanduan makanan secara langsung (Vainik et al, 2019). Pola makan seperti itu ditambah juga tidak memperhatikan gizi yang terkandung pada makanan yang dikonsumsi dapat menyebabkan kegemukan dan obesitas.

Fakta menunjukkan bahwa obesitas di dunia meningkat tiga kali lipat sejak tahun 1975. Pada tahun 2016 lebih dari 1.9 miliar orang dewasa berumur 18 tahun lebih mengalami kegemukan dan 650 juta mengalami obesitas (Apriyanti et al, 2018).

Maka dari itu, perlu penyeimbang dalam setiap makanan yang kita konsumsi dengan kegiatan-kegiatan seperti olahraga, diet, dan lain sebagainya. Diet adalah pengobatan pertama dan paling penting karena sejarah diet persis dimulai sejak orang mulai memasak makanan. Kebanyakan orang memilih diet untuk menyembuhkan penyakitnya sebab:

1. Diet tidak menakutkan seperti operasi.
2. Diet memiliki fungsi sebagai langkah preventif selain kuratif.

Maka dari itu, perlu untuk menelaah tipe diet yang sesuai pada kondisi tubuh berdasarkan jenis makanan dan tipe berat badan yang sesuai. 

## Ringkasan Tujuan Proyek
Dari pemaparan informasi di atas, maka perlu pengadaan suatu alat atau media untuk menyarankan masyarakat agar mengerti apa saja jenis makanan dengan resep-resep yang benar. Proses penyaranan ini menggunakan **teknik atau sistem rekomendasi** yang merekomendasikan jenis-jenis diet beserta contoh resep makanan. 

Dari dataset ini, akan dilakukan pengolahan serta pembuatan **algoritma rekomendasi hibrida *Mixed***  (*Content-Based Filtering*, dan *User-Based Filtering*) menggunakan *Machine Learning* yang akan memaksimalkan interaksi jenis diet dengan jenis-jenis diet lainnya. Hasil akhir akan memunculkan sekumpulan *Top-N Recommended Items*. Pada prosesnya, akan memaksimalkan penggunaan setiap fitur yang ada pada dataset yang ada.

Referensi:

  <u>[Pemilihan Menu Makanan untuk Diet dengan Pendekatan Algoritma Genetika](https://jptam.org/index.php/jptam/article/view/13393/10289)</u>

  <u>[Deteksi Objek pada Citra Makanan Sebagai Rekomendasi Diet Menggunakan Metode Mask R-CNN](https://journal.sinov.id/index.php/juitik/article/view/733/675)</u>
  
  <u>[Diet Sebagai Keseimbangan Hidup](https://jurnaldekonstruksi.id/index.php/dekonstruksi/article/view/195/148)</u>

# Business Understanding
Proyek ini dibuat untuk memberikan media berbasis sistem rekomendasi untuk masyarakat dalam memilih jenis makanan berdasarkan tipe diet dan tipe berat badan masyarakat.

## Problem Statements

1. Fitur unik apa saja yang dapat digunakan sebagai pertimbangan sistem rekomendasi?
   
   Masalah ini mencakup peninjauan dataset yang ada untuk melihat deskripsi, tujuan, dan informasi lainnya pada setiap kolomnya untuk dipilih menjadi pertimbangan data untuk model *Machine Learning* yang akan dibuat.

2. Bagaimana algoritma *Content-Based Filtering* dan *User-Based Filtering (Collaborative Filtering)* dapat menyimpulkan sebuah rekomendasi?
  
  Masalah ini mencakup cara penyajian akhir dari proses sistem itu sendiri ketika mengolah dari data mentah, data *model-friendly*, hingga data jadi untuk dikonsumsi masyarakat pengguna dengan informasi yang dibutuhkan pengguna. 

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

   - *User-Based Filtering (Collaborative Filtering)* 

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
   2. Mengubah tiap kalimat pada fitur **Recipe_name**, menjadi terkapitalisasi pada setiap awal kata
   3. Mengubah tipe data kolom **Weight** pada dataset *users*.
   
   ### Exploratory Data Analysis (EDA)

   Pada proses ini, terdapat beberapa langkah yang dilakukan. Tujuannya adalah memudahkan untuk mengenali dataset dengan pengelompokan dan penyajian secara visual. Berikut detailnya:

   4. Menghapus Kolom yang Tidak Perlu
      
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
  
   5. Pencarian Invalid dan Missing Value Lanjutan

      Pada tahap ini dilakukan pemeriksaan nilai-nilai yang tidak sesuai dengan tujuan analisis. 

      - Dataset Diet
      
         Pada **dataset diet**, pemeriksaan nilai tidak valid dengan melihat nilai *unique* di setiap kolom kategorikal. Hasilnya tidak ditemukan nilai yang aneh dan semua data sesuai.
      
         Lalu pada kolom numerik, dilakukan pengecekan pada angka kurang dari atau sama dengan 0. Ditemukan terdapat nilai tersebut pada kolom **Protein(g)** dan **Fat(g)**. Yang dilakukan adalah menghapus nilai-nilai itu pada kolom **Protein(g)** dan mempertahankan nilai-nilai yang ada pada kolom **Fat(g)**, sebab menyesuaikan tujuan analisis yaitu merekomendasikan masakan-masakan sehat dan rendah nilai gizi yang menyebabkan obesitas bagi pengguna yang ingin diet.

         Setelah langkah-langkah di atas, dapat disimpulkan bahwa **dataset diet** sudah bersih dan siap diproses pada langkah selanjutnya.

      - Dataset *Users*
      
         Pada **dataset *users***, pemeriksaan nilai tidak valid dengan melihat nilai *unique* di setiap kolom kategorikal. Hasilnya tidak ditemukan nilai yang aneh dan semua data sesuai.

         Lalu pada kolom numerik, dilakukan pengecekan angka kurang dari atau sama dengan 0. Juga tidak ditemukan nilai kurang dari atau sama dengan 0. 

         Setelah langkah-langkah di atas, dapat disimpulkan bahwa **dataset *users*** sudah bersih dan siap diproses pada langkah selanjutnya.
   
   6. Pencarian Nilai *Outliers*

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

         **Tabel 8. Besar Presentase dan Jumlah Data *Unique* Kolom Riwayat Keluarga Obesitas Dataset *Users***

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

# Data Preparation

Pada tahap ini, langkah yang dilakukan adalah untuk mempersiapkan data sebelum dilakukan tahap *modeling*. Tujuannya adalah agar mengetahui kekurangan data, memperbaiki data, serta merekonstruksi penataan data agar lebih mudah untuk digunakan baik oleh pengguna maupun pengolah. Untuk detail langkah-langkah yang dilakukan adalah sebagai berikut:

## Pengecekan dan Penyimpulan *Missing Value* Ulang

Langkah ini dilakukan untuk memeriksa ulang data yang sudah beberapa kali dilakukan langkah-langkah sebelumnya dan memastikan tidak ada data *null* yang tersisa sebelum dilakukan tahap selanjutnya. Hal ini bertujuan agar tidak memunculkan data kosong ketika akan direkomendasikan. Selain itu juga mencegah model mengidentifikasi nilai *null* sebagai sebuah data.

Dari hasil pemeriksaan kedua dataset, baik **data diet** dan **data *users*** sudah tidak terdapat data null yang tersisa. 

## Mengurutkan Data Berdasarkan Kategori Tertentu

Langkah ini dilakukan untuk merapikan urutan data berdasarkan fitur yang dipilih. Pada kali ini, fitur yang dipilih merupakan fitur yang mengandung data unik dan utama untuk dilakukan perekomendasian.

### Data Diet

Pada dataset ini, diurutkan berdasarkan tipe diet dan jenis masakan. Hal ini bertujuan agar nantinya ketika dilakukan perekomendasian, pengguna akan mudah mencari tipe diet yang mereka cari. Selain itu, jika pengguna ingin mencari jenis masakan tertentu, akan lebih mudah jika diurutkan. Keduanya diurutkan berdasarkan abjad dari abjad paling awal hingga paling akhir.

Selain itu, nantinya akan memudahkan dalam model mencari nilai *similarity*, karena data sudah tidak terlalu acak pada metode *Content-based Filtering*.

### Data *Users*

Pada dataset ini, diurutkan berdasarkan tipe obesitas pengguna. Hal ini bertujuan agar memudahkan pengolah dan pengguna dalam mencari data pengguna berdasarkan tipe obesitas yang sama, berdasarkan karakteristik-karakteristik lain yang tersedia. Pengurutan berdasarkan abjad dari yang paling awal hingga paling akhir.

Pengurutan juga mempermudah model dalam melakukan perekomendasian dengan metode *User-based Filtering*.

## Pengecekan dan Penyimpulan Data Duplikat

Langkah ini dilakukan untuk menghilangkan data yang diidentifikasi sebagai duplikasi dari data lainnya setelah proses pengurutan. Hal ini bertujuan agar data yang dibawa nanti pada model adalah data-data unik.

### Data Diet

Pada dataset diet, pengecekan dilakukan pada resep masakan. Hal ini bertujuan agar tidak terdapat lebih dari satu data resep yang sama pada jenis masakan atau tipe diet yang berbeda. Dengan begitu tidak terdapat redundansi data yang terjadi.

Setelah dilakukan pengecekan, ternyata memang terdapat data duplikasi pada fitur itu. Selanjutnya adalah melakukan penghapusan data duplikat.

### Data *Users*

Pada dataset *users*, pengecekan dilakukan pada fitur id. Hal ini bertujuan agar tidak terdapat redundansi data pengguna yang sama. Dengan begitu, perekomendasian metode *User-based Filtering* dapat bekerja dengan baik.

Setelah dilakukan pengecekan, ternyata sudah tidak ada data pengguna yang terduplikasi. Maka dapat dilanjutkan pada langkah selanjutnya.

## Rekonstruksi Urutan Kolom

Langkah ini dilakukan untuk mengubah tatanan kolom pada setiap dataset yang ada. Penataan ulang ini bertujuan agar data lebih rapi, konsisten, dan terurut berdasarkan fitur penting yang direkomendasikan. Pengubahan nama kolom yang tidak konsisten menjadi salah satu langkah yang dilakukan. 

Selain itu, juga menambahkan sebuah fitur baru pada data diet, yaitu fitur **fitur_tfidf** sebagai target pencarian *vector similarity* dalam metode *Content-based Filtering*. Isi dari fitur ini merupakan gabungan dari fitur-fitur penting di dalam data diet, yaitu tipe diet, jenis masakan, dan resep masakan.

# Modeling and Result

Setelah melakukan banyak tahap untuk mempersiapkan data-data yang ada menjadi data yang siap untuk dilakukan proses rekomendasi, maka pada tahap ini saatnya untuk menguji apakah data-data tersebut seharusnya memberikan hasil yang diharapkan. Algoritma yang dibuat ada dua macam, yaitu *Content-based Filtering* dan *User-based Filtering*.

## *Content-based Filtering*

Algoritma ini akan merekomendasikan tipe diet, jenis masakan, dan resepnya. Informasi lainnya yaitu nilai-nilai gizi seperti kandungan protein, lemak, dan karbohidrat yang cocok untuk pengguna yang merasa kebingungan dalam menentukan resep masakan jika sedang menjalani proses diet tertentu. 

Selain tujuan penyelesaian masalah di atas, juga algoritma *Content-based Filtering* ampuh dalam mengatasi fenomena *cold start* yang mana sistem masih belum ada data preferensi dari pengguna. Cara kerjanya mirip seperti algoritma *searching* biasa, namun yang digunakan bukan kerelatif-samaan karakternya, melainkan nilai vektor yang merepresentasikan data itu dengan data-data lainnya. Penghitungan vektor menggunakan fungsi dari **scikit-learn** yaitu *cosine similarity*.

Hasil dari algoritma ini adalah data-data ***Top-N*** berdasarkan indeks teratas hasil pencarian. Disini nilai **n** yang digunakan adalah 5. Maka yang muncul adalah 5 data paling cocok teratas dari hasil inputan pengguna. Inputan yang dimaksud adalah nama tipe diet dan jenis masakan yang pengguna ingin cari. Untuk hasil dari rekomendasi ditunjukkan pada **Tabel 9**.

**Tabel 9. Hasil Top 5 Rekomendasi Tipe Diet dan Jenis Masakan**

| tipe_diet | tipe_masakan | resep_masakan | kadar_protein | kadar_karbo | kadar_lemak |
|:--:|:--:|:--:|:--:|:--:|:--:|
| dash | american | Grilled Chicken | 148.38 | 57.14 | 79.00 |
| dash | american | Cauliflower Soup | 26.69 | 18.64 | 34.75 |
| dash | american | Bread Salad | 44.09 | 153.84 | 86.03 |
| dash | american | Baked Chicken | 108.97 | 0.86 | 48.36 |
| dash | american | Pumpkin Soup | 56.71 | 299.68 | 69.76 |

Pada studi kasus di atas, pengguna menginputkan tipe diet **dash** dan tipe masakan **american**. Maka yang muncul adalah data dengan nilai kemiripan teratas yang ada pada matriks vektor **fitur_tfidf**.

## *User-based Filtering (Collaborative Filtering)*

Algoritma ini akan sama dengan algoritma *Content-based Filtering* sebelumnya, yaitu menampilkan rekomendasi tipe diet dan makanan beserta nilai-nilai gizi yang terkandung seperti kandungan protein, lemak, dan karbohidrat. Yang membedakan adalah bagaimana algoritma ini bekerja.

Model ini memuat data masyarakat pengguna yang berisi data-data demografis seperti usia, berat badan, *Body Mass Index* (BMI). Setiap pengguna memiliki penilaian masing-masing terhadap tipe-tipe diet. Penilaian juga termasuk penilaian pada resep-resep makanan yang dipilih sesuai dengan tipe dietnya. Penentuan rekomendasi berdasarkan perhitungan prediksi *rating* dari setiap data-data *rating* yang sudah ada dan sudah dilatih. Nilai rating digunakan pada inputan **y** atau biasa disebut fitur target. Lalu, untuk inputan **x** menggunakan 2 fitur yaitu **id data diet** dan **id data pengguna** yang merupakan representasi detail setiap data di kedua dataset itu.

Hasil dari model ini akan menampilkan data-data ***Top-N*** dari hasil pengurutan setelah melakukan prediksi rating dari terbesar hingga terkecil. Nilai **N** yang digunakan adalah 5. Yang ditampilkan adalah data rekomendasi tipe diet dan resep-resep makanan sesuai dengan preferensi pengguna,dilihat dari nilai *rating* yang diberikan.

Pada pengembangannya, terbagi menjadi beberapa langkah dengan detail sebagai berikut:

### Membuat Preferensi *Rating*
Pada tahap ini, dilakukan pengumpulan data *rating* dari setiap pengguna. Sebenarnya, pada dataset asli tidak terdapat data *rating*, namun disini dilakukan pendekatan *random sampling* secara *dummy* pada setiap data pengguna. Terdapat beberapa langkah yang dilakukan dengan detail sebagai berikut:

1. Mengambil Data *User* Selain Yang Kekurangan Berat Badan 

Pada langkah ini, dilakukan penyaringan data pengguna yang cocok untuk dipasangkan dengan data diet. Yaitu pemilihan tipe berat badan yang biasanya memilih untuk melakukan diet. Disini menghapus data pengguna dengan tipe berat badan yang teridentifikasi **kekurangan berat badan**.

Sebab, pengguna-pengguna ini perlu untuk menambah kalori agar berat badannya justru meningkat.

2. Mengambil Data Setiap Tipe Berat Badan

Pada langkah ini, dilakukan pengambilan data-data tipe berat badan pengguna. Pengambilan tidak dilakukan pada keseluruhan jumlah keseluruhan setiap nilai uniknya, melainkan **hanya 20%** dari setiap nilai unik. Tujuannya agar pilihan pengguna lebih beragam dan lebih baik lagi ketika dilakukan *training model*.

Setelah diambil datanya dari setiap nilai unik, selanjutnya adalah penggabungan seluruh data itu.

3. Menyebarkan ID *Users* ke Data Diet

Pada langkah ini, dilakukan penyebaran data Id dari setiap pengguna ke data diet. Tujuannya agar nantinya dapat memasukkan data *dummy rating* ke data diet yang sudah ada data penggunanya. Dengan begitu akan dapat memperingkas dataset yang digunakan dan proses *merging* data tipe berat badan dapat dilakukan berdasarkan id pengguna.

4. Membuat Data *Rating*

Disini, *rating* yang digunakan hanya angka dengan *range* 1 sampai 5. Peletakan setiap nilai *rating* pada setiap data pengguna juga dilakukan secara *random choice*.

5. Menambahkan Tipe Berat Badan

Setelah data id pengguna ditambahkan ke data diet, maka selanjutnya dapat dilakukan *merging* data diet dengan data pengguna. Data yang diambil sebagai data baru adalah data tipe berat badan pengguna. Sebab, data ini nantinya akan dijadikan data preferensi pengguna yang akan diwakilkan oleh data id pengguna.

6. Encoding Fitur Kategorikal

Sebab dari tujuan utama adalah merekomendasikan tipe-tipe diet beserta resep-resep makanan berdasarkan preferensi tipe berat badan pengguna. Maka perlu melakukan *encoding* pada kategori-kategori diet. Tujuannya agar dapat dimasukkan ke dalam model sebagai parameter x. Model tidak dapat memroses data karakter, melainkan harus dalam bentuk angka.

7. Cek Informasi Dataset Saat Ini

Pengecekan informasi dari dataset yang akan digunakan bertujuan untuk memastikan bahwa data sudah baik dan dapat dilanjutkan dalam proses selanjutnya. Pada langkah ini juga terdapat penghapusan simbol koma pada id pengguna. Tanda koma ini awalnya merupakan penanda bahwa angka tersebut ribuan. 

### Membagi Data Untuk *Training* dan *Validation*

Setelah dataset dirasa sudah baik, maka selanjutnya adalah membaginya menjadi data *training* dan *validation*. Data *training* merupakan data inti sebagai bahan latih model, sedangkan data *validation* merupakan data lain diluar pada data *training* sebagai validasi hasil pemrosesan data apakah hasilnya dapat dengan baik untuk memprediksi. 

Pada tahap ini, terdapat beberapa langkah dengan detail sebagai berikut:

1. Mengacak Data
   
Pengacakan data dilakukan agar urutan data latih dapat beragam. Namun, pengacakan harus dilakukan dengan proposisi yang tetap. Realisasinya dapat dilakukan dengan penerapan parameter *random state* di fungsi *sample*. 

2. Membagi Data

Seperti pada tujuan awal, parameter x pada model akan diisi dengan data tipe diet dan data id pengguna. Lalu, parameter y akan diisi dengan data *rating* sebagai target prediksi.

Lalu, pengambilan data *training* hanya diambil **80%** dari jumlah keseluruhan data dan sisanya digunakan untuk data validasi sebesar 20%.

### Proses Training

Selanjutnya adalah membuat model yang akan melakukan prediksi *rating*. Model menggunakan teknik regresi menggunakan *Neural Network* untuk proses *Deep Learning* pada *library* **Tensorflow**. 

Model terdiri dari beberapa lapisan yang disebut *layer*. Untuk *layer* terbagi menjadi ***input layer***, ***hidden layer***, dan ***fully connected layer (output layer)***. Untuk detail penjelasannya adalah sebagai berikut:

1. *Input Layer*

   Untuk *input layer*, dibuat menjadi 2 masukan yang akan diisi oleh data tipe diet yang sudah di *encoding* dan id pengguna. Ukuran inputan yaitu 1 dimensi, ditandai dengan penggunaan parameter *shape* dengan isian angka 1. Hal ini dilakukan baik pada data tipe diet maupun data id pengguna.

2. *Hidden Layer*
   
   Sedangkan *hidden layer* diisi dengan lapisan-lapisan *embedding* yang akan memetakan nilai diskrit menjadi vektor kontinyu berdimensi lebih rendah untuk mencari representasi yang lebih baik dari data kategorikal.

   Lalu untuk ukurannya disesuaikan dengan ukuran data *input* atau biasa disebut ukuran *vocabulary*. *Layer Embedding* diisi dengan angka 16 yang artinya nilai dimensi vektor yang dihasilkan adalah 16 dimensi. 

   Selanjutnya adalah melakukan inisialisasi pada nilai *embedding* agar dapat memroses data lebih baik dalam jaringan saraf (*Neural Network*). Hal ini ditandai dengan penambahan *initializer* menggunakan **he_normal**.

   Selanjutnya adalah memberikan sejumlah penalti kecil pada data agar tidak terjadi overfitting dengan menggunakan *regularizers*.

   Yang terakhir adalah memasangkan *input layer* yang sudah dibuat sebelumnya. Setelah memasangkan *input layer*, dilanjutkan dengan melakukan *flatten*. Hal ini berguna agar angka-angka dengan dimensi di atas 1 pada *layer embedding*, dikembalikan pada dimensi 1 untuk dilakukan proses *dot product*. Langkah-langkah di atas diterapkan baik dari sisi data tipe diet maupun id pengguna. Untuk rumus dari *dot product* adalah sebagai berikut:

   $\vec{a} \cdot \vec{b}$ = $\sum\limits_{i=1}^n a_i \cdot b_i$

   Dengan penjelasan sebagai berikut;
   
   $\vec{a}$ : Vektor masukan pertama, pada kasus ini yaitu tipe diet.

   $\vec{b}$ : Vektor masukan kedua, pada kasus ini yaitu id pengguna.

   $\sum\limits_{i=1}^n a_i \cdot b_i$ = Penjumlahan pada angka $i$ sebanyak $n$ pada setiap hasil perkalian dot kedua vektor $a$ dan $b$.

   Rumus di atas diterapkan pada *layer dot* yang ditambahkan pada arsitektur model. *Layer* ini menghitung vektor-vektor data yang jadi masukan.

3. *Fully Connected Layer*

   Setelah mendapatkan nilai hasil *dot product*, yang dilakukan adalah mengubah hasil tersebut menjadi *fully  connected neural* dengan satu *unit output* yang merupakan data *rating* hasil prediksi. Hasil ini diperoleh menggunakan aktivasi **ReLU (*Rectified Linear Unit*)** yang memperkenalkan non-linearitas ke dalam model.

Setelah arsitektur model dibuat, selanjutnya adalah melakukan kompilasi model tersebut dengan beberapa *hyperparameter*. Untuk detailnya adalah sebagai berikut:

1. *Loss Function*
   
   Pada proses *training* di model ini, menggunakan *loss function* **Mean Squared Error (MSE)**. Fungsi ini akan mengukur seberapa besar perbedaan antara nilai hasil prediksi dengan nilai sebenarnya. Semakin kecil hasilnya, semakin baik model dalam memprediksi nilai. 

2. *Optimizer Function*
   
   Fungsi ini akan mengoptimalkan bobot (*weights*) model selama pelatihan (*training*). Untuk laju loncatan pembelajaran (*learning rate*) diatur sebesar **0,001** atau **1e-3**. Dengan learning rate sebesar itu, laju pembelajaran akan normal. Tidak terlalu dekat dan tidak terlalu jauh, maka model akan lebih efektif dalam mengambil jarak data yang dipelajari. Untuk metode pembelajarannya juga menggunakan **Adam (*Adaptive Moment Estimation*)** yang dapat dengan mudah beradaptasi pada setiap parameter model dan dapat mengoreksi bias pada momen-momen pembelajaran.

3. *Metric Function*

   Fungsi ini akan merekam hasil setiap *epochs* pembelajaran terjadi. Sebab menggunakan metrik MSE, maka disini juga menggunakan nilai MSE yang akan dipantau yang nantinya akan ditampilkan setelah proses *training* selesai.

Setelah proses kompilasi selesai, selanjutnya adalah melakukan *training*. Proses *training* dilakukan pada dua data, yaitu data **x** dan **y**. Untuk data x, disesuaikan dengan arsitektur model yang sudah dibuat. Maka perlu dilakukan pemisahan *input*, yang dibungkus dalam bentuk sebuah *list*. Data x pertama adalah tipe diet, dan yang kedua adalah data id pengguna pada **x train**. Selanjutnya, pada data y dimasukkan data **y train** yang merupakan data *ratings*. 

Disini juga menggunakan beberapa *parameter* model, dengan detail sebagai berikut:

1. Batch Size
   
   Parameter ini fungsinya untuk mendeklarasikan proporsi data yang dilakukan *training* pada setiap perulangannya. Disini menggunakan angka **8** sebagai ukuran *batch*-nya.

2. Epochs

   Parameter ini fungsinya untuk mendeklarasikan banyak perulangan pada proses *training* yang dilakukan. Disini menggunakan angka 10 yang menandakan bahwa proses *training* dilakukan sebanyak **10** kali putaran.

Selain melakukan proses *training*, juga dilakukan proses validasi. Proses validasi bertujuan agar memastikan bahwa model dapat belajar dengan data baru di luar data *training*. Untuk jenis data yang digunakan sama dengan data x dan y pada data *training*. Yang membedakan adalah sumber datanya. Di fase ini, data diambil dari hasil pemisahan data *training* dan *validation* pada tahap sebelumnya. Data diambil dari data *validation*.

### Mendapatkan Rekomendasi Tipe Diet Berdasarkan Data Pengguna

Setelah proses *training* dan *validation* selesai, saatnya untuk menguji model dalam memberikan rekomendasi tipe diet berdasarkan data pengguna. Untuk mengujinya, disini dilakukan pemilihan id pengguna saja secara acak dari data umum. Lalu dilakukan penyaringan data dari keseluruhan data dan diambil data yang memiliki id pengguna selain id pengguna yang sudah kita pilih sebelumnya. Tujuannya adalah untuk memastikan bahwa pilihan data yang diprediksi benar-benar belum pernah diambil oleh pengguna ini. 

Selanjutnya adalah proses *encoding* data kategorikal yaitu tipe diet. Sebab, data diambil dari sumber data yang belum dilakukan proses *encoding* pada data tipe diet. Setelah itu dilakukan prediksi nilai *rating* berdasarkan preferensi pengguna yang terwakilkan oleh nilai id pengguna dengan data-data diet yang belum pernah diambil oleh pengguna ini.

Setelah melakukan proses prediksi, maka dilakukan penyajian hasil rekomendasi. Hasil rekomendasi diambil urutan 5 teratas setelah pengurutan indeks hasil-hasil prediksi dari yang terbesar ke terkecil. Setelah itu dilakukan penyajian hasil rekomendasi dalam bentuk ***Dataframe***. Contoh hasil rekomendasi ditunjukkan pada **Tabel 10**.

Tabel 10. Hasil Rekomendasi Tipe Diet Beserta Informasi Lainnya

| id_diet | tipe_diet | tipe_masakan | resep_masakan | kadar_protein | kadar_karbo | kadar_lemak |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 2020 | keto | italian | Low Carb Pepperoni Pizza Meatballs | 146.41 | 34.31 | 207.44 |
| 2021 | keto | italian | Keto Pizza | 28.10 | 24.98 | 20.21 |
| 2022 | keto | Keto Gnocchi | 12.28 | 8.66 | 10.59 |
| 2034 | keto | italian | Ez Keto Pizza | 127.50 | 25.61 | 213.62 |
| 2364 | keto | south east asian | Keto Cheesy Shrimp Fritters | 96.15| 13.16 | 62.85 |

## Kelebihan dan Kekurangan Setiap Algoritma

Setelah mengimplementasikan kedua algoritma, baik *Content-based Filtering* dan *Collaborative Filtering*, terdapat kelebihan dan kekurangan dari masing-masing algoritma. Berikut adalah detailnya:

### Content-based Filtering

**Kelebihan**
- Dapat dengan mudah menangani item baru, karena rekomendasi didasarkan pada fitur atau konten dari item tersebut.
- Dapat memberikan rekomendasi yang dapat dimengerti oleh pengguna dengan mudah, karena didasarkan oleh fitur atau atribut yang spesifik dari item.
- Tidak memerlukan data atau informasi dari pengguna yang sudah ada sebagai acuan, karena informasi diambil dari hasil ekstraksi nilai-nilai dari item itu sendiri dengan item lainnya

**Kekurangan**
- Kesulitan dalam menangani preferensi pengguna yang kompleks dan sering berubah seiring bertambahnya pengguna, karena tidak ada data pengguna yang dikaitkan dalam proses perekomendasian dengan algoritma ini.
- Ketergantungan pada kualitas fitur atau atribut yang digunakan dalam mendeskripsikan item. Jika fitur tidak mewakili item dengan baik, maka kualitas rekomendasi dapat menurun.
- Cenderung memberikan rekomendasi yang serupa dengan item yang telah disukai atau pernah dipilih oleh pengguna, maka hasil rekomendasi akan tidak terlalu bervariasi.

### Collaborative Filtering

**Kelebihan**
- Dapat menangani data preferensi pengguna yag kompleks, dengan cara menemukan pola yang mungkin sulit ditemukan oleh metode lain.
- Tidak memerlukan pengetahuan tentang item, hanya cukup dengan data perwakilan antara data item dan data pengguna.
- Memberikan rekomendasi yang lebih ke arah personal berdasarkan pola yang diciptakan dari preferensi pengguna.

**Kekurangan**
- Terjadi kondisi *Cold Start*, yaitu kondisi dimana item adalah item baru dan pengguna adalah pengguna baru. Maka, tidak ditemukan data preferensi yang sesuai dengan item yang akan direkomendasikan.
- Tidak dapat memberikan rekomendasi yang akurat jika data pengguna ke item masih sangat jarang. Sebab, cakupan informasi data masih belum terlalu cenderung pada salah satu sifat pengguna yang bersangkutan.
- Terdapat masalah keamanan yang berkaiatn dengan data privasi pengguna. Dengan algoritma ini, peluang untuk terjadi kebocoran data privasi pengguna sangat besar dan memiliki risiko serangan profil palsu (*profile injection attacks*).

Kesimpulan dari beberapa hal yang sudah disampaikan di atas, maka perlu menggunakan **kedua algoritam** di atas agar performa sistem dalam merekomendasikan dapat bekerja secara maksimal. Dengan begitu, ketika sistem masih baru, sistem akan menggunakan pendekatan *Content-based Filtering* dalam merekomendasikan item. Dan jika pengguna sudah mulai ramai, dapat dialihkan ke algoritma *Collaborative Filtering* dengan menggunakan data-data preferensi pengguna.

# Evaluation

Pada analisis ini, model dievaluasi menggunakan metrik evaluasi bernama *Mean Squared Error* (MSE). Metrik ini digunakan untuk menghitung jarak perbedaan antara nilai asli dengan nilai hasil prediksi. Nilai yang dijadikan acuan biasa disebut nilai *error*. Semakin kecil nilai *error* yang dihasilkan, maka semakin baik juga kemampuan model dalam memprediksi.Rumus dari MSE adalah sebagai berikut : 

   MSE = $\frac{1}{n}\sum\limits_{i=1}^n (y_i - \hat{y}_i)^2$

   Dengan penjelasan sebagai berikut:

   $\frac{1}{n}\sum\limits_{i=1}^n$ : Pembagian angka 1 dengan jumlah observasi dalam dataset. Penjumlahan dilakukan secara iteratif dari angka 1.
   
   $\text{y}_i$ : nilai sebenarnya ke-${i}$
   
   $\hat{y}_i$ : nilai hasil prediksi ke-${i}$

Metrik ini akan menghitung selisih antara nilai yang diprediksi oleh model dan nilai sebenarnya untuk diambil nilai *error*-nya. Setelah itu, nilai *error* akan dihilangkan efek postif dan negatifnya dengan cara dikuadratkan. Setelah dikuadratka, nilai *error* akan dijumlahkan dan dibagi dengan jumlah sampel yang akan menghasilkan nilai rata-rata dari *error* kuadrat. Hasil itu yang merupakan nilai *Mean Squared Error* atau MSE.

Hasil penerapan metrik di atas, diperoleh nilai *error* sebesar **2.1528725624084473**. Hasil tersebut cukup kecil dan menandakan bahwa model dapat bekerja dengan baik dalam memprediksi data *rating* pengguna dengan preferensi tertentu pada setiap data yang belum pernah diambil atau dilakukan pemberian *rating* oleh pengguna tersebut. Untuk bentuk visualisasi hasil *training* dengan metrik evaluasi ditunjukkan pada **Gambar 16 dan 17**.

**Gambar 16. Visualisasi Hasil *Loss***
![model-loss](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/e8ef822e-1419-44be-8717-8e91b1fe0746)

**Gambar 17. Visualisasi Hasil *Mean Squared Error* (MSE)**
![mse](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/15c222e6-affc-408a-8cdb-f24a5036e2a7)


# Conclusion

Dari hasil analisis ini, telah dibuat dua algoritma sistem rekomendasi yaitu *Content-based Filtering* dan *Collaborative Filtering*. Kedua algoritma itu merekomendasikan tipe diet beserta detail lainnya baik antar item dengan *Content-based Filtering* dan merekomendasikan tipe diet beserta detail lainnya berdasarkan preferensi pengguna yang serupa dengan *Collaborative Filtering*. 

Pada algoritma *Content-based Filtering*, algoritma akan membandingkan kesamaan berdasarkan nilai *cosine similarity* setiap item tipe diet. Lalu, akan diambil nilai kesamaan paling tinggi untuk dijadikan rekomendasi. Sedangkan pada algoritma *Collaborative Filtering*, algoritma akan membandingkan kesamaan pola preferensi pengguna antar pengguna berdasarkan tipe diet yang ditandai dengan dominasi *rating* pengguna tertentu terhadap tipe diet tertentu.

Model-model ini masih memerlukan improvisasi, seperti persebaran nilai *rating* di awal sebelum proses *training*. *Rating* masih berdasarkan penempatan acak dan belum benar-benar data nyata. Kedepannya, dapat dilakukan observasi secara langsung pada masyarakat yang membutuhkan diet dan resep-resepnya agar hasilnya lebih menggambarkan kondisi nyata.

# References
[1] Rando, Setiawan L.R, "Pemilihan Menu Makanan untuk Diet dengan Pendekatan Algoritma Genetika" *Jurnal Pendidikan Tambusai*, vol. 8, no. 1, 2024.

[2] Pawening R.E, Puteri M.E, Jianika A.D, Hidayati F, "Deteksi Objek pada Citra Makanan Sebagai Rekomendasi Diet Menggunakan Metode Mask R-CNN" *Jurnal Ilmiah Teknik Informatika dan Komunikasi*, vol. 4, no. 1, 2024.

[3] Theo Y, "Diet Sebagai Keseimbangan Hidup" *Jurnal Dekonstruksi*, vol. 9, no. 4, 2023.
