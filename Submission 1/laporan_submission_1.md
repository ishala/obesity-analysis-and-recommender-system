# Laporan Proyek Machine Learning: Analisa Data Obesitas 
# Nama : Muhammad Faishal Ali D.

## A. Domain Proyek
### 1. Penjelasan Umum
Masalah gizi merupakan hal yang sangat kompleks dan serius. Karena menyangkut kualitas penerus-penerus bangsa. Seperti halnya di Indonesia. Salah satu masalah gizi yang masih menjadi pembahasan hangat adalah obesitas.

Obesitas merupakan suatu kondisi medis yang ditandai oleh penimbunan lemak tubuh berlebihan, yang dapat meningkatkan risiko terjadinya berbagai penyakit kronis. Faktor-faktor seperti pola makan yang tidak sehat, gaya hidup yang kurang aktif, dan perubahan budaya telah berkontribusi pada meningkatnya angka obesitas di seluruh dunia.

Menurut data Organisasi Kesehatan Dunia (WHO), obesitas telah mencapai tingkat epidemiologi, dengan lebih dari 650 juta orang dewasa di seluruh dunia dinyatakan obesitas pada tahun 2016. Hal ini menunjukkan bahwa obesitas bukan lagi hanya masalah kesehatan individu, tetapi juga menjadi beban kesehatan masyarakat yang signifikan. Obesitas dapat timbul disebabkan oleh beberapa hal sebagai berikut:

1. Kurangnya aktifitas fisik baik kegiatan harian maupun latihan fisik terstruktur
2. keturunan genetika
3. Faktor lingkungan

### 2. Sebab Akibat Masalah
Hal ini perlu dilakukan analisis serta penanggulangan lebih lanjut, sebab obesitas dapat meningkatkan risiko terjadinya penyakit-penyakit kardiovaskular, diabetes tipe 2, dan tekanan darah tinggi. Selain itu, biaya kesehatan yang terkait dengan pengobatan dan manajemen obesitas memberikan tekanan tambahan pada sistem kesehatan nasional.

Maka dari itu, perlu melakukan berbagai strategi untuk mengurangi resiko masyarakat terkena obesitas. Seperti anjuran mengkonsumsi makanan sehat, olahraga, serta pengadaan infrastruktur ideal untuk peninjauan status tubuh.

Disini saya berinisiatif untuk melakukan analisis lebih lanjut mengenai data masyarakat beserta label yang menunjukkan apakah sedang mengalami obesitas atau tidak. Serta memberikan informasi pada kondisi ciri-ciri tubuh agar lebih berhati-hati dalam melakukan kebiasaan hidup.

### 3. Referensi
   1. [Referensi Pertama](https://d1wqtxts1xzle7.cloudfront.net/39625453/jurnal-libre.pdf?1446519911=&response-content-disposition=inline%3B+filename%3DFAKTOR_RISIKO_OBESITAS_PADA_ANAK_5_15_TA.pdf&Expires=1706423938&Signature=CfseHwMvVXjfNg90XPlccC~RocUVem5IncpL82cJPnYcPEL9rRJgkjy3eA5AFzVMKtvSfxJfO~WGhARcxrvmn3MGkw6Eslf5UwFnNZFL5zqd7UamxeWU0mZ2qS0SAH~kcO7cF4DDHQQADyGNDPTLRRlxdL0-cpA35~ZzhmjrPqxNmbFkCKNKFz4YCsUBc4v~Hffnyl2ZjMkcR1MkJ~XBr8kJKCnQS~OaFeWkjetvIkn4FR-OBOJEXffkgmohYc~-09NT0WjluDqHP3Dx-Dt1-bhGIqowCqQEUGgfl6pvdA6O2BK-ZiNJvI~sDgZVKukUQdQpFvJgz7PDPFqNHVEQ9w__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
   2. [Referensi Kedua](https://pgm.persagi.org/index.php/pgm/article/view/47)
   3. [Referensi Ketiga](https://journals.telkomuniversity.ac.id/jett/article/download/1395/1005/)
   

## B. Business Understanding
Pada proses analisis ini, saya berfokus untuk mengambil permasalahan-permasalahan yang akan diangkat dari permasalahan garis besar untuk mencari solusi yang tepat. Berikut adalah uraiannya:

### 1. Problem Statements
1. Bagaimana cara untuk mengurangi potensi masyarakat terkena obesitas?
> Mengangkat masalah pada potensi masyarakat terkena obesitas, seperti pola hidup, dan makanan yang dikonsumsi.
1. Dari segi aspek apa saja tubuh dapat dikatakan tidak obesitas?
> Mencari aspek yang dapat dianalisis seperti berat badan, BMI, kecukupan kalori pada makanan, dan lain-lain. Membuktikan bahwa parameter-parameter ini yang dapat menjadi acuan seseorang mengidap obesitas atau tidak dengan penghitungan BMI secara resmi.

### 2. Goals
1. Memberikan insight pada data mengenai kriteria penderita obesitas.
> Memberikan informasi terhadap data orang yang terkena obesitas maupun tidak. Berdasarkan ukuran badan seperti tinggi badan, berat badan, dan BMI.
2. Memberikan gambaran umum pada ciri-ciri tubuh yang sehat.
> Memberikan informasi terkait ciri-ciri tubuh yang sehat dan tidak terindikasi obesitas.

### 3. Solution Statements
1. Membuat analisis data dengan visualisasi data yang menggambarkan kondisi data untuk prediksi pada tahap modelling.
2. Membuat model regresi pada data obesitas menggunakan **Random Forest** dengan kolom BMI sebagai target.
3. Melakukan hyperparameter tuning pada *n_estimator*, *random_state*, *n_jobs*, dan *max_depth* untuk mengoptimalisasi kinerja model. 
4. Menggunakan metrik evaluasi *Mean Squared Root* (MSE)

## C. Data Understanding
Pada bagian ini akan memberikan penjelasan terkait data yang digunakan untuk analisis. Berikut detailnya:

### 1. Informasi Data
Data yang digunakan pada proses analisis ini merupakan data sumber-terbuka (open source) yang memuat tentang informasi gaya hidup penduduk di Mexico, Peru, dan Colombia. Data ini dikumpulkan oleh **ScienceDirect** dibawah lisesn Creative Commons. Data asli sudah cukup bersih, hanya perlu dilakukan beberapa langkah pembersihan.

Untuk jumlah data awal sebelum analisis lebih lanjut adalah **2111 baris** dan **19 kolom fitur** hasil dari pengambilan sumber dari tautan dan menggunakan perintah

```
obesDf.shape
```

Perintah di atas memanggil variabel dataframe yang memuat dataset, dilanjutkan dengan fungsi yang menampilkan bentuk data berdasarkan baris dan kolom.

### 2. Tautan Sumber Data
Berikut adalah link yang mengarah pada sumber tautan

[LINK DATASET](https://www.kaggle.com/datasets/mandysia/obesity-dataset-cleaned-and-data-sinthetic)

### 3. Uraian Fitur di Dalam Data
Di dalam dataset itu sendiri, terdapat banyak fitur yang ada dan dapat dilakukan analisis. Berikut adalah uraiannya:

1. Id 
   - Kolom index pada setiap baris data
2. BMI (*Body Mass Index*): 
   - Indeks masa tubuh ideal
3. Gender
   - Jenis Kelamin target yang diobservasi 
4. Age
   - Usia target yang diobservasi
5. Height 
   - Tinggi badan dalam satuan *inch* target yang diobservasi
6. Weight
   - Berat badan dalam satuan *kilogram* target yang diobservasi
7. family_history_with_overweight
   - Riwayat keluarga dengan berat badan berlebih (obesitas)
8. FAVC
   - Frekuensi mengkonsumsi makanan tinggi kalori target yang diobservasi
9.  FCVC
       - Frekuensi mengkonsumsi sayur-mayur target yang diobservasi
10. NCP
      - Jumlah makan pokok perhari target yang diobservasi
11. CAEC
      - Frekuensi makan cemilan target yang diobservasi
12. SMOKE
      - Kebiasaan merokok target yang diobservasi
13. CH2O 
      - Jumlah minum air target yang diobservasi
14. SCC
      - Kebiasaan monitoring konsumsi kalori target yang diobservasi
15. FAF
      - Frekuensi kegiatan fisik target yang diobservasi
16. TUE
      - Waktu penggunaan perangkat dalam satuan *jam* target yang diobservasi
17. CALC
      - Frekuensi mengkonsumsi alkohol target yang diobservasi
18. MTRANS
      - Kategori transportasi yang digunakan target yang diobservasi
19. NObeyesdad
      - Kategori berat badan
  
Untuk fitur target ada di fitur **BMI** dengan perhitungan fitur **Height** dan **Weight**