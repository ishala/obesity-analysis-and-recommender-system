# Laporan Proyek Machine Learning: Analisa Data Obesitas 
# Nama : Muhammad Faishal Ali D.

# Domain Proyek
## Latar Belakang
Masalah gizi merupakan hal yang sangat kompleks dan serius. Karena menyangkut kualitas penerus-penerus bangsa. Seperti halnya di Indonesia. Salah satu masalah gizi yang masih menjadi pembahasan hangat adalah obesitas.

Obesitas merupakan suatu kondisi medis yang ditandai oleh penimbunan lemak tubuh berlebihan, yang dapat meningkatkan risiko terjadinya berbagai penyakit kronis. Faktor-faktor seperti pola makan yang tidak sehat, gaya hidup yang kurang aktif, dan perubahan budaya telah berkontribusi pada meningkatnya angka obesitas di seluruh dunia.

Menurut data Organisasi Kesehatan Dunia (WHO), obesitas telah mencapai tingkat epidemiologi, dengan lebih dari 650 juta orang dewasa di seluruh dunia dinyatakan obesitas pada tahun 2016. Pada paparan informasi [**"Panduan Hari Obesitas Sedunia"**](https://ayosehat.kemkes.go.id/pub/files/0b43c48e8765bf62a02f42a1359349d5.pdf) yang disampaikan oleh Ditjen Pencegahan dan Pengendalian Penyakit bersama Kementerian Kesehatan Republik Indonesia, Secara global, lebih dari **160 juta** kehidupan sehat yang hilang disebabkan oleh Indeks Massa Tubuh (IMT) (atau dalam bahasa inggris biasa disebut *Body Mass Index (BMI)*) yang tinggi pada tahun 2019, dan angkanya kemungkinan akan lebih tinggi setiap tahun. Ini berarti lebih dari 20% dari semua tahun kehidupan sehat yang hilang yang disebabkan oleh kesehatan kronis yang dapat dicegah. Serta, pada tahun 2030 diprediksi 1 dari 5 wanita dan 1 dari 7 pria akan hidup dengan obesitas (setara dengan lebih dari 1 miliar orang di seluruh dunia).

Hal ini menunjukkan bahwa obesitas bukan lagi hanya masalah kesehatan individu, tetapi juga menjadi beban kesehatan masyarakat yang signifikan. Obesitas dapat timbul disebabkan oleh beberapa hal sebagai berikut:

1. Kurangnya aktifitas fisik baik kegiatan harian maupun latihan fisik terstruktur
2. Keturunan genetika
3. Faktor lingkungan

Dalam mengantisipasi terkena obesitas, terdapat beberapa hal yang dapat dilakukan, seperti:

1. Mengkonsumsi sayur dan buah minimal 5 porsi setiap hari
2. Membatasi tidur yang berlebihan
3. Meningkatkan aktivitas fisik minimal 30 menit setiap hari
4. Batasi konsumsi gula, garam, dan lemak berlebih 

### Sebab Akibat Masalah
Hal ini perlu dilakukan analisis serta penanggulangan lebih lanjut, sebab obesitas dapat meningkatkan risiko terjadinya penyakit-penyakit kardiovaskular, diabetes tipe 2, dan tekanan darah tinggi. Selain itu, biaya kesehatan yang terkait dengan pengobatan dan manajemen obesitas memberikan tekanan tambahan pada sistem kesehatan nasional.

Maka dari itu, perlu melakukan berbagai strategi untuk mengurangi resiko masyarakat terkena obesitas. Seperti anjuran mengkonsumsi makanan sehat, olahraga, serta pengadaan infrastruktur ideal untuk peninjauan status tubuh.

Disini saya berinisiatif untuk melakukan analisis lebih lanjut mengenai data masyarakat beserta label yang menunjukkan apakah sedang mengalami obesitas atau tidak dengan proses prediksi menggunakan metode **regresi linear**.

Refrensi: 
   <u>[Perbandingan Kinerja Regresi Decision Tree dan Regresi Linear Berganda untuk Prediksi BMI pada Dataset Asthma](https://ejournal.uksw.edu/juses/article/view/8438/2430)</u>
   

# Business Understanding
Proyek ini dibuat untuk kemudahan masyarakat dalam melakukan pengecekan secara berkala *Body Mass Index (BMI)* mereka dari ukuran tinggi badan dan berat badan.

## Problem Statements
1. Fitur apa yang memiliki pengaruh tinggi terhadap perhitungan nilai *BMI*?
   
   Masalah ini mencakup pemilihan fitur atau kolom yang dapat digunakan sebagai tolak ukur prediksi nilai *Body Mass Index (BMI)* dalam perhitungan resmi.

2. Bagaimana agar fitur-fitur penting yang ada di dalam *dataset* dapat digunakan pada model?
   
   Masalah ini mencakup cara menormalisasikan bentuk data, baik dari segi tipe, distribusi, dan *range* nilai yang ada agar model dapat memberikan hasil prediksi yang maksimal.

3. Algoritma apa yang cocok untuk dilakukan regresi linear?
   
   Masalah ini mencakup pemilihan algoritma paling optimal dalam memroses kasus yang ada pada *dataset* yang digunakan. Keputusan akan dipertimbangkan dari nilai *error* masing-masing algoritma.

## Goals
1. Mengolah *dataset* agar terstruktur dengan baik, serta *model-friendly*.
   
   *Dataset* yang digunakan menjadi lebih rapi, terstruktur, dan dapat digunakan dalam proses regresi linear dengan optimal.

2. Menciptakan model yang dapat bekerja dengan baik dalam memprediksi nilai *Body Mass Index (BMI)* dari segi akurasi yang baik, dengan nilai *error* yang minimal.

   Model yang tercipta tidak mengalami *overfitting*, dapat beradaptasi dengan data baru non latih, dan yang terpenting dapat memprediksi nilai dengan baik.

## Solution Statements
1. Membuat analisis data dengan visualisasi data yang menggambarkan kondisi data untuk prediksi pada tahap *modeling*.
2. Membuat model regresi pada data obesitas menggunakan **K-Nearest Neighbors dan Random Forest** dengan kolom *BMI* sebagai fitur target.
3. Melakukan perbandingan dari kedua model tersebut dengan cara mengevaluasi hasil metrik evaluasi.
4. Menggunakan metrik evaluasi *Mean Squared Root* (MSE), dengan perolehan *error* di bawah 10%. Tujuannya agar prediksi yang dihasilkan akurat dengan kondisi tubuh saat pengecekan.

# Data Understanding
Pada bagian ini akan memberikan penjelasan terkait data yang digunakan untuk analisis. Berikut detailnya:

## Informasi Data
   Data yang digunakan pada proses analisis ini merupakan data sumber-terbuka (*open source*) dengan judul **Obesity Dataset Cleaned and Data Sinthetic** yang memuat tentang informasi gaya hidup penduduk di Mexico, Peru, dan Colombia. Data ini dikumpulkan oleh **ScienceDirect** dibawah lisensi Creative Commons. 

   Informasi Lanjutan
   
   - Jumlah Baris: 2111
   - Jumlah kolom: 19


Dengan penjelasan fitur dan variabel didalam dataset ditunjukkan pada **Tabel 1**.

**Tabel 1. Penjelasan Fitur dan Variabel Pada Dataset**

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


   - [LINK DATASET](https://www.kaggle.com/datasets/mandysia/obesity-dataset-cleaned-and-data-sinthetic)

Untuk fitur target ada di fitur **BMI** dengan perhitungan fitur **Height** dan **Weight**

## Pembersihan dan Persiapan Data
Pada prosesnya, data understanding terbagi menjadi beberapa tahapan. Berikut detailnya:

### Data Loading

Pada proses ini, dilakukan proses pemuatan data ke dalam *workspace* yang digunakan, pada kasus ini adalah *notebook*. 

### Data Assessing 

Pada proses ini, dilakukan penilaian pada kelayakan data. Hal ini meliputi berbagai aspek tinjauan. Berikut adalah detailnya:

1. Penilaian Dataset Awal

      Pada tahap ini, yang dilakukan adalah melihat informasi keseluruhan dari dataset yang akan menampilkan poin-poin seperti nama kolom yang ada, jumlah data dari setiap kolom, tipe data kolom, dan lain-lain ditunjukkan pada **Tabel 2**.


      **Tabel 2. Tipe Data dan Jumlah Kolom**

      | Tipe Data Kolom | Jumlah Kolom |
      |:----------:|:----------:|
      | Object |    14    |
      | Integer |    3    |
      | Float |    2    |

2. Pengecekan Data *Null*
      
      Pada tahap ini, dilakukan peninjauan terhadap nilai-nilai baris yang ada di setiap kolomnya. Tujuannya adalah untuk melihat banyak nilai *null* disetiap kolomnya. Setelah dilakukan pengecekan, data sudah bersih dari data *null*.

3. Pengecekan Data Duplikat
      
      Pada tahap ini, dilakukan peninjauan pada nilai-nilai yang terduplikasi secara *unique*. Tujuannya adalah untuk mengurangi distorsi pada data akibat adanya data duplikat.Hasil pemeriksaan sudah tidak ditemukan nilai duplikat dari keseluruhan kolom.

4. Deskripsi Nilai Statistik Dataset

      Pada tahap ini, dilakukan identifikasi awal nilai-nilai statistik pada kolom numerik yang ada di dataset ditunjukkan pada **Tabel 3**.

      **Tabel 3. Nilai Statistik Awal pada Dataset**

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

      Dari hasil di atas, terindikasi ada tipe data kolom yang masih kurang tepat, yaitu pada kolom **Weight**.

### Data Cleaning
      
Setelah dilakukan Data Assesing, yang dapat dilakukan pembersihan hanya pada penggantian tipe data kolom Weight. 

### Exploratory Data Analysis (EDA)

Pada proses ini, terdapat beberapa langkah yang dilakukan. Tujuannya adalah memudahkan untuk mengenali dataset dengan pengelompokan dan penyajian secara visual. Berikut adalah detailnya:

1. Menghapus Kolom yang Tidak Perlu
   
   Tahap ini bertujuan agar dimensi data tidak terlalu besar, dengan begitu pemuatan data tidak akan terlalu lama dan berat. 

   Dataframe saat ini hanya terdiri dari 5 kolom yaitu:
      - Height
      - Weight
      - BMI
      - CAEC
      - NObeyesdad
  
2. Pencarian Missing Value Lanjutan
   
      Pada pencarian missing value mendalam, dilakukan penelusuran pada setiap kolom numerik dengan pencarian input nilai pada nilai yang kemungkinan formatnya salah.

      Pada setiap kolom numerik, penanganannya sama yaitu mengantisipasi tidak adanya nilai kurang dari atau sama dengan 0. Sebab, nilai 0 ke bawah tidak mungkin ada pada ukuran berat badan dan tinggi badan.

      Dari hasil proses di atas, dapat disimpulkan bahwa kolom numerik sudah bersih dari missing value.

3. Pencarian Nilai *Outliers*
   
   Pada proses ini, terdapat beberapa langkah untuk mengidentifikasi nilai outliers pada setiap kolom numerik yang akan digunakan untuk fitur-fitur modelling. Sebab, jika tidak dibersihkan akan memberikan kualitas data dan model yang tidak maksimal.

   Pada langkah-langkah di bawah, dilakukan visualisasi data menggunakan boxplot. Jenis plot ini sangat umum digunakan untuk mencari nilai outliers dari titik-titik persebaran data. Hasil pencarian nilai *Outliers* ditunjukkan pada **Gambar 1, 2, dan 3**.


   **Gambar 1. Pencarian *Outliers* Kolom Height**
   
   ![Hasil Height 1](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/6efcd767-5138-4c9c-8733-43af0fb920d2)
      
   **Gambar 2. Pencarian *Outliers* Kolom Weight**
   
   ![Hasil Weight 1](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/8e6779f4-123b-458f-bd75-52e80a8f8820)
   
   **Gambar 3. Pencarian *Outliers* Kolom *BMI***
   
   ![Hasil_ BMI_1](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/982a1d6c-6930-485b-989f-402d5b9026e2)

   Dari hasil di atas, terdapat outliers pada kolom **Height** dan **Weight**. Maka selanjutnya adalah menangani data tersebut menggunakan metode **IQR (Inter Quartile Range)**.

5. Penanganan Outlier
   
      Pada proses ini, dilakukan identifikasi dan eliminasi nilai-nilai outlier yang ada di dalam fitur-fitur yang akan digunakan dalam modeling. Terdapat banyak cara atau rumus dalam mengeliminasinya. Namun, disini akan menggunakan metode IQR atau *Inter Quartile Range*. 
      
      Rumus:

      $IQR = Q3 - Q1$

      Penjelasan:

      $Q1$ = Kuartil pertama dari data (25%)

      $Q3$ = Kuartil ketiga dari data (75%)

      $IQR$ = Inter Quartile Range, jarak antara kuartil 1 dan 3

6. Pencarian Nilai *Outliers* Lanjut
   
   Setelah itu dilakukan pengecekan dengan menggunakan *box plot* lanjut yang ditunjukkan pada **Gambar 4, 5, dan 6**.

   **Gambar 4. Pencarian *Outliers* Kolom Height Lanjut**
   
   ![Hasil Height 2](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/4812b284-688b-47c1-a4af-d49b15b24b66)
   
   **Gambar 5. Pencarian *Outliers* Kolom Weight Lanjut**
   
   ![Hasil Weight 2](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/70e847eb-448f-47db-9e85-d7ce5eb68fa9)
   
   **Gambar 6. Pencarian *Outliers* Kolom *BMI* Lanjut**
   
   ![Hasil BMI 2](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/016a4a23-9974-466f-a9d4-e28d2e897ddc)
   
   Dari hasil penghapusan outlier sebelumnya, ternyata masih terdapat data outlier di dalam kolom **Height**. Dan juga, dapat terlihat bahwa nilai outlier merupakan nilai maksimal. 
   
   Maka yang perlu dilakukan adalah mengeksekusi ulang kode-kode penghapusan data outlier (seperti pada langkah sebelumnya)

8. Univariate Analysis
   
   Pada tahap ini, fokusnya adalah mencari pola data dari setiap kolomnya. Dalam pengolahan dan ekstraksi isinya, dibagi menjadi:

      1. Kolom Kategorikal

      Pada kolom kategorikal, fokusnya adalah mencari presentase jumlah pada nilai unique. Pada kolom *CAEC* ditunjukkan pada **Tabel 4**.

      **Tabel 4. Jumlah Sampel dan Presentase Kolom *CAEC***
      | CAEC | Jumlah Sampel | Presentase
      |:--|:--:|:--:|
      | sometimes | 1764 | 83.7% | 
      | frequently | 241 | 11.4% | 
      | always | 52 | 2.5% | 
      | no | 51 | 2.4% |

      Dengan hasil visualisasi data ditunjukkan pada **Gambar 7**.

      **Gambar 7. Visualisasi Data Jumlah Data Kolom *CAEC***

      ![Hasil CAEC](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/56dea09b-2fa7-48e9-a881-b9de51b742c4)
      
      Lalu pada kolom kategori berat badan (*NObeyesdad*), jumlah sampel dan presentase ditunjukkan pada **Tabel 5**.

      **Tabel 5. Jumlah Sampel dan Presentase Kolom *NObeyesdad***
      | NObeyesdad | Jumlah Sampel | Presentase
      |:--|:--:|:--:|
      | obesity_type_i | 349 | 16.6% | 
      | obesity_type_iii  | 323 | 15.3% | 
      | obesity_type_ii | 297 | 14.1% | 
      | overweight_level_i  | 290 | 13.8% |
      | overweight_level_ii  | 290 | 13.8% |
      | normal_weight  | 287 | 13.6% |
      | insufficient_weight  | 272 | 12.9% |

      Dengan hasil visualisasi data ditunjukkan pada **Gambar 8**

      **Gambar 8. Visualisasi Data Jumlah Data Kolom *NObeyesdad***

      ![Hasil NObeyesdad](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/061c3315-e034-4389-92ae-d47d374bdbdb)

      2. Kolom Numerik

      Pada kolom-kolom numerik, fokusnya yaitu melihat pola persebaran data. Identifikasi bentuk distribusi data ditunjukkan pada **Gambar 9**.

      **Gambar 9. Visualisasi Distribusi Data Kolom Numerik**
   
      ![Hasil Numerikal](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/948faa5d-f58e-4723-b2f0-b3a957d9e449)

      Dengan penjelasan sebagai berikut:
      1. Kolom BMI
         - Pada kolom BMI (Kolom Target) persebaran banyak data cenderung rata. Dengan perolehan banyak data terbanyak ada di kisaran BMI 27 dan 18.
         - Banyak BMI terendah ada di angka 50 dengan total hampir 0 data.
         - Kemiringan data cenderung ke kanan (Right-Skewed), tetapi masih dapat dikatakan hampir simetris.
      2. Kolom Height
         - Data cenderung simetris.
         - Banyak data terbanyak ada di kisaran angka 1.7-1.8
      3. Kolom Weight
         - Kemiringan data cenderung ke kanan (Right-Skewed)
         - Banyak data terbanyak ada di angka 80
         - Banyak data terendah ada di kisaran angka 140 - 160

10. Multivariate Analysis

   Pada proses ini, tujuannya adalah mencari relasi pola pada dua atau lebih kolom untuk menyimpulkan keterkaitan antar kolom-kolom itu. Berikut detailnya:

   1. Kolom Kategorikal
      Pada kolom kategorikal, *plotting* dilakukan pada satu kolom ke kolom target.
      
      Hasil *plotting* kolom *CAEC* dan *BMI* ditunjukkan pada **Gambar 10**.
      
      **Gambar 10. Visualisasi Bentuk Data Kolom *CAEC* terhadap Kolom *BMI***
      
      ![multi-CAEC](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/0bbc889d-ce11-452a-9fbd-7e7b46ce8050)


      - Rata-rata BMI bervariasi, dengan frekuensi memakan cemilan kategori "sometimes" memiliki rata-rata tertinggi
      - Frekuensi memakan cemilan kategori "frequently" memiliki rata-rata terendah
      - Dapat diasumsikan bahwa fitur CAEC memiliki pengaruh relatif rendah terhadap fitur BMI

      Hasil *plotting* kolom *NObeyesdad* dan *BMI* ditunjukkan pada **Gambar 11**.
      
      **Gambar 11. Visualisasi Bentuk Data Kolom *NObeyesdad* terhadap Kolom *BMI***

      ![multi-NObeyesdad](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/4da797b7-d7ca-4573-bbad-02543f72b36e)

      - Rata-rata BMI bervariasi, dengan kategori "*obesity_type_iii*" memiliki rata-rata tertinggi
      - Kategori "*insufficient_weight*" memiliki rata-rata terendah
      - Dapat diasumsikan bahwa fitur *NObeyesdad* memiliki pengaruh relatif tinggi terhadap fitur *BMI*, sebab fitur ini merepresentasikan langsung data *BMI* yang dikonversikan dalam bentuk kategorikal.

   3. Kolom Numerik
      
      Pada kolom numerik akan dilakukan beberapa langkah *plotting* dengan memasukkan semua kolom numerikal secara bersamaan. Hal ini berbeda dengan kolom kategorikal yang dilakukan antar dua kolom.

      *Plotting* menggunakan *Pair Plot* ditunjukkan pada **Gambar 12**.
      
      **Gambar 12. Visualisasi Bentuk *Plotting* dengan *Pair Plot***

      ![multi-numerical-pairplot](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/ccc0956e-1753-42f5-88c0-7cfd4d80acba)

      Terdapat korelasi positif kuat antara kolom **Weight** dan **BMI** ditandai dengan pola semu menjulang ke atas secara linear. Hal ini sesuai dengan topik data yang digunakan, yaitu representasi keadaan berat badan dengan *Body Mass Index (BMI)* terhadap indikasi obesitas. Dan Kolom *Height* tidak berkorelasi dengan kolom *BMI*.

      Selanjutnya adalah melakukan *Plotting* menggunakan *Heat Map* ditunjukkan pada **Gambar 13**.
      
      **Gambar 13. Visualisasi Bentuk *Plotting* dengan *Heat Map***

      ![multi-numerical-heatmap](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/674d748f-b4d9-41ec-808f-16572445b63c)

      Dari hasil di atas, terlihat bahwa kolom **Weight** memiliki relasi positif kuat dengan kolom **BMI** dengan nilai korelasi mendekati positif (+) 1.

      Hal ini sesuai dengan topik data dan tujuan analisi yaitu obesitas yang berkaitan erat dengan berat badan.

# Data Preparation

Pada tahap ini, data yang ada akan diolah sedemikian rupa agar bekerja dengan baik dengan model yang akan dibuat. Fokus pada proses ini adalah mengubah setiap fitur agar dapat menyesuaikan model dengan hasil yang diharapkan. Berikut adalah detailnya:

## *Encoding* Fitur Kategorikal
      
   Pada fitur kategorikal dengan tipe data *object*, tidak dapat diproses oleh model yang memerlukan nilai numerik. Maka dari itu, perlu dilakukan proses *Encoding*.

   Proses ini dilakukan dengan menggunakan *One Hot Method*. Dengan begitu, ukuran data menjadi tidak terlalu besar serta dapat dilakukan prediksi lebih lanjut pada proses regresi. Transformasi fitur dari tipe data *object* menjadi *integer* agar fitur menjadi *model-friendly* untuk model yang memrosesnya.

## Peninjauan Dimensi Data dengan PCA
     
   Pada kasus dataset ini, nampaknya tidak perlu dilakukan reduksi dimensi dengan PCA dikarenakan hanya ada 2 fitur numerik yang tidak memiliki bentuk yang mirip. Yaitu *Height* dan *Weight* yang ditunjukkan pada **Gambar 14**.

   **Gambar 14. Peninjauan Korelasi Sebagai Prasyarat Reduksi Dimensi Dengan *PCA***
   
   ![pca](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/866c06bf-cef6-4542-b23c-af742e9e21a3)

   Fitur *Height* dan *Weight* tidak memiliki korelasi, tidak berbentuk pola. Jika dilakukan reduksi dan penghapusan fitur asli, akan merusak standarisasi yang akan dilakukan pada *step* selanjutnya.

## Train Test Split

   Proses ini akan membagi dataset menjadi dua, yaitu Fitur X dan Y. Fitur X akan menjadi acuan prediksi, sedangkan Fitur Y akan menjadi bahan belajar mesin dalam mempelajari fitur X. Berikut Kodenya:

   Pada pembagian train dan test, disini hanya mengambil **10%** yaitu sebanyak **211** data dari keseluruhan data X sebanyak **2108** data untuk menjadi data test, dengan pengambilan *random state* pada state **42** dengan tujuan agar data yang diambil konsisten.

## Standarisasi Fitur X
     
   Pada proses ini, bertujuan untuk mengubah **fitur X** asli menjadi nilai-nilai baru dengan skala yang relatif sama atau mendekati distribusi normal. Standarisasi hanya dilakukan pada **fitur X** untuk menghindari kebocoran data.

   Standarisasi menggunakan fungsi **StandarScaler** dari *library* **Scikit-learn**. 

   Dari hasil proses ini, maka sekarang distribusi data menjadi lebih tereduksi. Hasil standarisasi ditunjukkan pada **Tabel 6**.

   **Tabel 6. Nilai Fitur X Setelah Standarisasi Berdasarkan Nilai Statistik**
   |  | Height | Weight
   |:-:|:-:|:-:|
   | count | 1897.0000 | 1897.0000 |
   | mean | 0.0000 | 0.0000 |
   | std | 1.0003 | 1.0003 |
   | min | -2.7149 | -1.8140 |
   | 25% | -0.7728 | -0.8206 |
   | 50% | -0.0108 | -0.1329 |
   | 75% | 0.7114 | 0.8223 |
   | max | 2.6517 | 3.0001 |

   Dapat dilihat bahwa saat ini rata-rata (*mean*) dan standar deviasi (*std*) sudah sama dari kedua kolom yang dilakukan standarisasi. Maka dapat dilanjutkan untuk proses *modeling*.

# Modeling

   Pada proses ini, fokusnya adalah membuat model yang akan melakukan prediksi dari **fitur X** sebagai bahan prediksi dan **fitur y** sebagai acuan belajar pola hasilnya. Jenis algoritma-algoritma yang digunakan adalah *K-Nearest Neighbors* dan *Random Forest*. Berikut adalah detailnya:
   
   ## *K-Nearest Neighbors*
      
   *K-Nearest Neighbors* atau biasa disebut *KNN* adalah sebuah algoritma yang pada proses prediksinya adalah melakukan pemetaan data prediksi secara acak, lalu akan diambil data dengan jarak terdekat. 
      
   ### Kelebihan
      
   - Mudah dipahami dan diimplementasikan, dengan konsep perhitungan jarak antara titik data untuk menentukan tetangga terdekat
   - Tidak diperlukan pembelajaran atau proses *training* ketika membuat model
   - Dapat menangani data non linear dengan dimensi data yang tinggi.

   ### Kekurangan

   - Tenaga komputasi yang dihasilkan tinggi, apalagi pada data dengan tingkat dimensi tinggi
   - Sangat sensitif pada data *outliers*, sebab algoritma ini mengedepankan ukuran jarak antar data.
   - Prestasi menurun pada keberlanjutan dimensi, sebab dengan dimensi yang terus meningkat akan menunrunkan makna dari jarak data.

   Lalu, dalam pengimplementasiannya terdapat penggunaan parameter, yaitu *n_neighbors*. Parameter ini akan memberikan batasan tetangga yang akan dicek dengan batas **5** tetangga terdekat.
      
   Setelah dilakukan pengujian pada data *training*, dilanjutkan dengan pengujian besar *error* menggunakan metrik *Mean Squared Error (MSE)*.

   ## *Random Forest*

   Random Forest adalah algoritma *ensemble* dengan metode *bagging* yang isinya terdapat banyak algoritma yang berjalan secara independen. Dari hasil keseluruhan algoritma, akan dipilih yang memiliki peforma terbaik. Jadi, algoritma *Random Forest* adalah algoritma yang tersusun dari banyak algoritma pohon (*decision tree*) dengan pembagian fitur secara acak.

   ### Kelebihan
   - Memiliki stabilitas terhadap *overfitting*, sebab pada prosesnya membangun banyak pohon keputusan yang berbeda lalu digabungkan
   - Tidak sensitif pada *outliers*, sebab hasil prediksi didasarkan pada mayoritas keputusan pohon
   - Dapat menangani campuran tipe data tanpa memerlukan banyak *preprocessing data*.
      
   ### Kekurangan
   - Tidak selalu interpretatif, sulit untuk diintepretasi secara intuitif terutama jika terdapat banyak *decision tree* yang ada di dalam *ensemble*.
   - Rentan pada kesalahan, jika data yang digunakan tidak seimbang
   - Tidak efektif pada data tabular yang linear dengan hubungan linear yang kuat 

   Pada proses pengujian model pada variabel, terdapat penggunaan parameter-parameter dengan detail sebagai berikut:

   - *n_estimators* dengan nilai **10** untuk melakukan *set* pohon untuk bercabang sebanyak maksimal **10** kali.
   - *max_depth* dengan nilai **4** agar pohon cabang hanya melakukan percabangan yang lebih kecil lagi sebanyak paling dalam **4** kali kedalaman.
   - *random_state* dengan nilai **25** agar nilai random yang dilakukan *sampling* konsisten pada kombinasi **ke-25**.
   - *n_jobs* dengan nilai **-1** agar pekerjaan yang dilakukan oleh model dilakukan secara paralel pada keseluruhan proses.

   Setelah dilakukan pengujian pada data *training*, dilanjutkan dengan pengujian besar *error* menggunakan metrik *Mean Squared Error (MSE)*.

   Setelah proses *training* fitur *train* baik x maupun y, dilanjutkan dengan membandingkan perolehan *error* dari keduanya. Hasilnya dapat ditunjukkan pada **Tabel 7**.

   **Tabel 7. Jumlah *Error* Algoritma *KNN* dan *Random Forest* pada Data *Training***

   | K-Nearest Neighbors | Random Forest|
   |:-:|:-:|
   | 0.148428 | 1.298258 |

   Dari hasil di atas, dapat disimpulkan sementara bahwa ***K-Nearest Neighbors*** akan dipilih menjadi algoritma solusi, dengan perolehan error terkecil, yaitu **0.148428**. Selain itu, juga algoritma ini ternyata dapat berjalan dengan baik pada data *training* yang digunakan saat ini yang berukuran relatif kecil.

   Selanjutnya, akan dilakukan evaluasi alternatif yaitu pengujian dengan data *testing* sebagai representasi data asli diluar data latih.

# Evaluation

Walaupun sudah terlihat bahwa *KNN* lebih baik daripada *Random Forest*, tetapi hal itu masih diambil dari hasil perolehan prediksi **data *training*** dan perlu untuk melakukan prediksi pada **data *testing***. Sebab, pada dasarnya nanti model akan memprediksi data asli, tidak pada data *training*. Maka diperlukan proses prediksi lagi pada data *testing* dengan kedua algoritma tersebut.

Pada proses analisis saat ini, prediksi yang dilakukan adalah menggunakan metode regresi, maka metrik yang cocok untuk diujikan adalah *Mean Squared Error (MSE)*. 

Metrik ini bekerja dengan menghitung seberapa jauh perbedaan antara nilai sebenarnya dengan nilai hasil prediksi. Semakin jauh perbedaannya, maka semakin tidak akurat. Jauh dan tidaknya dilihat dari hasil *error* yang didapatkan. Berikut adalah formulanya:

MSE = $\frac{1}{n}\sum\limits_{i=1}^n (y_i - \hat{y}_i)^2$

Dengan penjelasan sebagai berikut:

- $\frac{1}{n}\sum\limits_{i=1}^n$ adalah pembagian angka 1 dengan jumlah observasi dalam dataset. Penjumlahan dilakukan secara iteratif dari angka 1.
- $\text{y}_i$ adalah nilai sebenarnya ke-${i}$
- $\hat{y}_i$ adalah nilai hasil prediksi ke-${i}$

Selanjutnya adalah implementasi pada fitur *X_test*. Berikut adalah tahapan-tahapannya:

  1. *Scaling* dengan Standarisasi pada Fitur *X_test*
   
     Proses scaling pada fitur **X_test** dilakukan agar data pada fitur tersebut dapat terkonvergensi dengan baik ketika akan dimasukkan ke dalam model. 
     
     Langkahnya kurang lebih sama ketika melakukan scaling pada fitur **X_train** pada langkah sebelumnya. Hanya pemilihan fitur saja yang berbeda.

  2. Evaluasi Metrik
      Seperti pada pernyataan di awal, penentu algoritma yang baik adalah ketika dilakukan uji metrik di **data *testing***, sebagai representasi data baru. Data dapat dikatakan **baru** dikarenakan tidak ada pada hasil pembelajaran di **data *training***. Maka dapat dilakukan evaluasi metrik pada kedua algoritma ini.

      Setelah dilakukan prediksi menggunakan kedua algoritma tersebut pada data *testing*, selanjutnya dapat ditampilkan hasil dari keduanya. Hasilnya dapat ditunjukkan pada **Tabel 8**.

      **Tabel 8. Hasil *Error* Algoritma *KNN* dan *Random Forest* pada Data *Training* Dan *Testing***

      | | KNN | Random Forest|
      |:-|:-:|:-:|
      | trainMSE | 0.148428 | 1.298258 |
      | testMSE | 0.413398 | 1.384255 |

      Selain itu, juga dilakukan *plotting* menggunakan *horizontal bar chart* yang ditunjukkan pada **Gambar 15**.

      **Gambar 15. Visualisasi *Error* Algoritma *KNN* dan *Random Forest* pada Data *Training* dan *Testing***

     ![compare-error](https://github.com/ishala/obesity-analysis-and-recommender-system/assets/97838402/61957046-eacb-4a24-8dc5-59d4486a9089)

      Dari tabel hasil di atas, dapat disimpulkan bahwa ternyata saat dilakukan evaluasi metrik pada *KNN* dan *Random Forest* menggunakan *MSE*, hasil uji data testing pada ***KNN*** lebih kecil daripada ***Random Forest*** dari segi nilai *error*-nya. 
      

      Untuk sementara dapat dikatakan bahwa ***KNN* lebih baik** performanya dibandingkan dengan Random Forest. Selanjutnya dapat dilakukan evaluasi hasil prediksi.

  4. Evaluasi Prediksi

      Untuk memastikan algoritma mana yang cocok adalah mencoba membandingkan data asli dengan data hasil prediksi. Semakin mirip, maka algoritma itu baik performanya dalam memprediksi.

      Yang perlu dilakukan adalah mengumpulkan sampel yang akan diuji, dengan langkah-langkah sebagai berikut:

      Sample data di ambil dari 3 data teratas dari data *testing x*, begitu juga data harapan nilai asli diambil dari 3 data teratas dari data *testing y*.

      Setelah sampel data didapatkan, maka dapat langsung saja dilakukan prediksi untuk melihat seberapa baik kedua algoritma tersebut memprediksi. Hasil prediksi ditunjukkan pada **Tabel 9**.

      **Tabel 9. Hasil Perbandingan Nilai Asli dengan Nilai Prediksi pada Algoritma *KNN* dan *Random Forest*** 
      | | y_true | prediksi_KNN | prediksi_RF|
      |:-:|:-:|:-:|:-:|
      | 1446 | 31.896722 | 31.9 | 32.8 |
      | 2077 | 46.027679 | 46.5 | 47.5 |
      | 1204 | 28.969812 | 28.9 | 27.4 |


# Conclusion
Dari hasil analisis ini, telah didapatkan sebuah model regresi untuk memprediksi angka *Body Mass Index (BMI)* seseorang dari input tinggi badan dan berat badan. Model ini akan memudahkan pengguna untuk mengetahui *level* berat badan mereka dari angka ideal. Model ini masih memerlukan improvisasi seperti pelabelan *level BMI* yang didapatkan dari hasil prediksi.

# References
[1] Tegar Nurani, A. Setiawan A. Susanto B, "Perbandingan Kinerja Regresi Decision Tree danRegresi Linear Berganda untuk Prediksi BMI pada Dataset Asthma" *Jurnal Sains dan Edukasi Sains*, vol. 6, no. 1, pp 34-43, 2023.
