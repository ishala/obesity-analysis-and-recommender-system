# Laporan Proyek Machine Learning: Analisa Data Obesitas 
# Nama : Muhammad Faishal Ali D.

## A. Domain Proyek
### 1. Penjelasan Umum
Masalah gizi merupakan hal yang sangat kompleks dan serius. Karena menyangkut kualitas penerus-penerus bangsa. Seperti halnya di Indonesia. Salah satu masalah gizi yang masih menjadi pembahasan hangat adalah obesitas.

Obesitas merupakan suatu kondisi medis yang ditandai oleh penimbunan lemak tubuh berlebihan, yang dapat meningkatkan risiko terjadinya berbagai penyakit kronis. Faktor-faktor seperti pola makan yang tidak sehat, gaya hidup yang kurang aktif, dan perubahan budaya telah berkontribusi pada meningkatnya angka obesitas di seluruh dunia.

Menurut data Organisasi Kesehatan Dunia (WHO), obesitas telah mencapai tingkat epidemiologi, dengan lebih dari 650 juta orang dewasa di seluruh dunia dinyatakan obesitas pada tahun 2016. Hal ini menunjukkan bahwa obesitas bukan lagi hanya masalah kesehatan individu, tetapi juga menjadi beban kesehatan masyarakat yang signifikan. Obesitas dapat timbul disebabkan oleh beberapa hal sebagai berikut:

1. Kurangnya aktifitas fisik baik kegiatan harian maupun latihan fisik terstruktur
2. Keturunan genetika
3. Faktor lingkungan

### 2. Sebab Akibat Masalah
Hal ini perlu dilakukan analisis serta penanggulangan lebih lanjut, sebab obesitas dapat meningkatkan risiko terjadinya penyakit-penyakit kardiovaskular, diabetes tipe 2, dan tekanan darah tinggi. Selain itu, biaya kesehatan yang terkait dengan pengobatan dan manajemen obesitas memberikan tekanan tambahan pada sistem kesehatan nasional.

Maka dari itu, perlu melakukan berbagai strategi untuk mengurangi resiko masyarakat terkena obesitas. Seperti anjuran mengkonsumsi makanan sehat, olahraga, serta pengadaan infrastruktur ideal untuk peninjauan status tubuh.

Disini saya berinisiatif untuk melakukan analisis lebih lanjut mengenai data masyarakat beserta label yang menunjukkan apakah sedang mengalami obesitas atau tidak. Serta memberikan informasi pada kondisi ciri-ciri tubuh agar lebih berhati-hati dalam melakukan kebiasaan hidup.

### 3. Referensi
   1. [FAKTOR RISIKO OBESITAS PADA ANAK 5-15](https://d1wqtxts1xzle7.cloudfront.net/39625453/jurnal-libre.pdf?1446519911=&response-content-disposition=inline%3B+filename%3DFAKTOR_RISIKO_OBESITAS_PADA_ANAK_5_15_TA.pdf&Expires=1706423938&Signature=CfseHwMvVXjfNg90XPlccC~RocUVem5IncpL82cJPnYcPEL9rRJgkjy3eA5AFzVMKtvSfxJfO~WGhARcxrvmn3MGkw6Eslf5UwFnNZFL5zqd7UamxeWU0mZ2qS0SAH~kcO7cF4DDHQQADyGNDPTLRRlxdL0-cpA35~ZzhmjrPqxNmbFkCKNKFz4YCsUBc4v~Hffnyl2ZjMkcR1MkJ~XBr8kJKCnQS~OaFeWkjetvIkn4FR-OBOJEXffkgmohYc~-09NT0WjluDqHP3Dx-Dt1-bhGIqowCqQEUGgfl6pvdA6O2BK-ZiNJvI~sDgZVKukUQdQpFvJgz7PDPFqNHVEQ9w__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
   2. [FAKTOR RISIKO OBESITAS SENTRAL PADA ORANG DEWASA UMUR 25-65 TAHUN DI INDONESIA (ANALISIS DATA RISET KESEHATAN DASAR 2013)](https://pgm.persagi.org/index.php/pgm/article/view/47)
   3. [ANALISIS KALKULASI BODY MASS INDEX DENGAN PENGOLAHAN CITRA DIGITAL BERBASIS APLIKASI ANDROID](https://journals.telkomuniversity.ac.id/jett/article/download/1395/1005/)
   

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
2. Membuat model regresi pada data obesitas menggunakan **K-Nearest Neighbors dan Random Forest** dengan kolom BMI sebagai target.
3. Melakukan perbandingan dari kedua model tersebut dengan cara mengevaluasi hasil metrik evaluasi.
4. Menggunakan metrik evaluasi *Mean Squared Root* (MSE)

## C. Data Understanding
Pada bagian ini akan memberikan penjelasan terkait data yang digunakan untuk analisis. Berikut detailnya:

### 1. Informasi Data
      Data yang digunakan pada proses analisis ini merupakan data sumber-terbuka (open source) yang memuat tentang informasi gaya hidup penduduk di Mexico, Peru, dan Colombia. Data ini dikumpulkan oleh **ScienceDirect** dibawah lisesn Creative Commons. Data asli sudah cukup bersih, hanya perlu dilakukan beberapa langkah pembersihan.

      Untuk jumlah data awal sebelum analisis lebih lanjut adalah **2111 baris** dan **19 kolom fitur** hasil dari pengambilan sumber dari tautan dan menggunakan perintah

```py
obesDf.shape
```

Perintah di atas memanggil variabel dataframe yang memuat dataset, dilanjutkan dengan fungsi yang menampilkan bentuk data berdasarkan baris dan kolom.

### 2. Tautan Sumber Data
Berikut adalah link yang mengarah pada sumber tautan

[LINK DATASET](https://www.kaggle.com/datasets/mandysia/obesity-dataset-cleaned-and-data-sinthetic)

### 3. Uraian Fitur di Dalam Data
Di dalam dataset itu sendiri, terdapat banyak fitur yang ada dan dapat dilakukan analisis. Berikut adalah uraiannya:

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


Untuk fitur target ada di fitur **BMI** dengan perhitungan fitur **Height** dan **Weight**

### 4. Penjelasan Tahapan-tahapan Data Understanding
Pada prosesnya, data understanding terbagi menjadi beberapa tahapan. Berikut detailnya:

A. Data Loading

Pada proses ini, dilakukan proses pemuatan data ke dalam *workspace* yang digunakan, pada kasus ini adalah *notebook*. Perintah yang ditulis adalah
```py
obesDfPath = 'data/ObesityDataSet_cleaned_and_data_sinthetic.csv'
obesDf = pd.read_csv(obesDfPath)
```

Path yang ditulis disesuaikan dengan direktori yang digunakan. Pada analisis ini, data diletakkan pada perangkat lokal pengguna dengan menggunakan *Jupyter Notebook*.

B. Data Assessing 

Pada proses ini, dilakukan penilaian pada kelayakan data. Hal ini meliputi berbagai aspek tinjauan. Berikut adalah detailnya:

1. Penilaian Dataset Awal

      Pada tahap ini, yang dilakukan adalah melihat informasi keseluruhan dari dataset. Berikut kodenya:
      ```py
      obesDf.info()
      ```

      Dari hasil perintah di atas, akan menampilkan poin-poin seperti nama kolom yang ada, jumlah data dari setiap kolom, tipe data kolom, dan lain-lain.

      Hasilnya adalah terdapat **2111** data tidak null pada setiap kolom. Dengan karakteristik kolom sebagai berikut:

      | Tipe Data Kolom | Jumlah Kolom |
      |:----------:|:----------:|
      | Object |    14    |
      | Integer |    3    |
      | Float |    2    |

2. Pengecekan Data Null
      
      Pada tahap ini, dilakukan peninjauan terhadap nilai-nilai baris yang ada di setiap kolomnya. Tujuannya adalah untuk melihat banyak nilai null disetiap kolomnya. Berikut adalah kodenya:

      ```py
      obesDf.isna().sum()
      ```

      Dari hasil kode di atas, tidak ditemukan nilai null dari keseluruhan kolom.

3. Pengecekan Data Duplikat
      
      Pada tahap ini, dilakukan peninjauan pada nilai-nilai yang terduplikasi secara *unique*. Tujuannya adalah untuk mengurangi distorsi pada data akibat adanya data duplikat. Berikut kodenya:

      ```py
      obesDf.duplicated().sum()
      ```

      Dari hasil kode di atas, tidak ditemukan nilai duplikat dari keseluruhan kolom.

4. Deskripsi Nilai Statistik Dataset

      Pada tahap ini, dilakukan identifikasi awal nilai-nilai statistik pada kolom numerik yang ada di dataset. Berikut Kodenya:

      ```py
      obesDf.describe()
      ```

      Untuk hasil dari kode di atas adalah sebagai berikut:
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

C. Data Cleaning
      
Setelah dilakukan Data Assesing, yang dapat dilakukan pembersihan hanya pada penggantian tipe data kolom Weight. Berikut kodenya:

```py
obesDf['Weight'] = obesDf.Weight.astype(float)
```

D. Exploratory Data Analysis (EDA)

Pada proses ini, terdapat beberapa langkah yang dilakukan. Tujuannya adalah memudahkan untuk mengenali dataset dengan pengelompokan dan penyajian secara visual. Berikut adalah detailnya:

1. Menghapus Kolom yang Tidak Perlu
   
   Tahap ini bertujuan agar dimensi data tidak terlalu besar, dengan begitu pemuatan data tidak akan terlalu lama dan berat. Berikut adalah kodenya:

   ```py
   obesDf = obesDf[['Height', 'Weight', 'BMI', 'CAEC', 'NObeyesdad']]
   ```

   Dari hasil kode di atas, saat ini dataframe hanya terdiri dari 5 kolom yaitu:
      - Height
      - Weight
      - BMI
      - CAEC
      - NObeyesdad
  
2. Pencarian Missing Value Lanjutan
   
      Pada pencarian missing value mendalam, dilakukan penelusuran pada setiap kolom numerik dengan pencarian input nilai pada nilai yang kemungkinan formatnya salah.

      Pada setiap kolom numerik, penanganannya sama yaitu mengantisipasi tidak adanya nilai kurang dari atau sama dengan 0. Sebab, nilai 0 ke bawah tidak mungkin ada pada ukuran berat badan dan tinggi badan.

      - Kolom Height

        ```py
        heightZero = (obesDf.Height <= 0).sum()
        ```

        hasilnya:
        > 0
      - Kolom Weight

        ```py
        weightZero = (obesDf.Weight <= 0).sum()
        ```
        
        Hasilnya:
        > 0

      - Kolom BMI

        ```py
        zeroBMI = (obesDf.BMI <= 0).sum()
        ```

        Hasilnya:
        > 0

      Dari hasil proses di atas, dapat disimpulkan bahwa kolom numerik sudah bersih dari missing value.

3. Pencarian Nilai *Outliers*
   
   Pada proses ini, terdapat beberapa langkah untuk mengidentifikasi nilai outliers pada setiap kolom numerik yang akan digunakan untuk fitur-fitur modelling. Sebab, jika tidak dibersihkan akan memberikan kualitas data dan model yang tidak maksimal.

   Pada langkah-langkah di bawah, dilakukan visualisasi data menggunakan boxplot. Jenis plot ini sangat umum digunakan untuk mencari nilai outliers dari titik-titik persebaran data. Berikut adalah hasilnya:

   - Kolom Height
      ![Hasil Height 1](assets/height1.png)
   - Kolom Weight
      ![Hasil Weight 1](assets/weight1.png)
   - Kolom BMI
      ![Hasil BMI 1](assets/BMI1.png)

   Dari hasil di atas, terdapat outliers pada kolom **Height** dan **Weight**. Maka selanjutnya adalah menangani data tersebut menggunakan metode **IQR (Inter Quartile Range)**.

4. Penanganan Outlier
   
      Pada proses ini, dilakukan identifikasi dan eliminasi nilai-nilai outlier yang ada di dalam fitur-fitur yang akan digunakan dalam modeling. Terdapat banyak cara atau rumus dalam mengeliminasinya. Namun, disini akan menggunakan metode IQR atau *Inter Quartile Range*. 
      
      Rumus:

      IQR = Q3 - Q1

      Penjelasan:

      Q1 = Kuartil pertama dari data (25%)

      Q3 = Kuartil ketiga dari data (75%)

      IQR = Inter Quartile Range

      Kode:

      **Pengambilan Kuartil**
      ```py
      q1 = numerical.quantile(0.25)
      q3 = numerical.quantile(0.75)
      iqr = q3 - q1
      ```

      Setelah mendapatkan nilai IQR-nya, maka selanjutnya adalah mencari batas atas dan batas bawahnya.

      **Pencarian Batas Atas dan Bawah**
      ```py
      upper = q3 + 1.5 * iqr
      bottom = q1 - 1.5 * iqr
      ```

      Dapat diketahui bahwa outlier selalu berada di bawah atau di atas batas-batas tersebut. Selanjutnya adalah menghapus nilai outliers yang terjaring pada kondisi ini. 

      **Penyaringan Data**
      ```py
      outliers = ((numerical < bottom) | (numerical > upper))
      ```

      Setelah data outlier didapatkan, maka dapat dihapus

      **Penghapusan Data Outlier**
      ```py
      cleanedObesDf = obesDf[~outliers.any(axis=1)]
      ```

5. Pencarian Nilai *Outliers* Lanjut
   
   Setelah itu dilakukan pengecekan dengan menggunakan box plot lanjut
   - Kolom Height

      ![Hasil Height 2](assets/height2.png)
   - Kolom Weight
      
      ![Hasil Weight 2](assets/weight2.png)
   - Kolom BMI
      
      ![Hasil BMI 2](assets/BMI2.png)
   
   Dari hasil penghapusan outlier sebelumnya, ternyata masih terdapat data outlier di dalam kolom **Height**. Dan juga, dapat terlihat bahwa nilai outlier merupakan nilai maksimal. 
   
   Maka yang perlu dilakukan adalah mengeksekusi ulang kode-kode penghapusan data outlier (seperti pada langkah sebelumnya)

6. Univariate Analysis
   
   Pada tahap ini, fokusnya adalah mencari pola data dari setiap kolomnya. Dalam pengolahan dan ekstraksi isinya, dibagi menjadi:

      1. Kolom Kategorikal
   
         Pada kolom kategorikal, fokusnya adalah mencari presentase jumlah pada nilai unique.
         
         Terdapat formula umum yang digunakan adalah sebagai berikut:

         ```py
            count = cleanedObesDf[feature].value_counts()
            percent = 100 * cleanedObesDf[feature].value_counts(normalize=True)   

            df = pd.DataFrame({
            'Jumlah sampel':count, 
            'Persentase':percent.round(1)
            })
            print(df)
         ```

            Hasilnya adalah sebagai berikut:
            - Kolom FAVC

            | CAEC | Jumlah Sampel | Presentase
            |:--|:--:|:--:|
            | sometimes | 1764 | 83.7% | 
            | frequently | 241 | 11.4% | 
            | always | 52 | 2.5% | 
            | no | 51 | 2.4% |

            Dengan hasil visualisasi data sebagai berikut:

            ![Hasil CAEC](assets/CAEC.png)
            - Kolom Kategori Berat Badan (NObeyesdad)

            | NObeyesdad | Jumlah Sampel | Presentase
            |:--|:--:|:--:|
            | obesity_type_i | 349 | 16.6% | 
            | obesity_type_iii  | 323 | 15.3% | 
            | obesity_type_ii | 297 | 14.1% | 
            | overweight_level_i  | 290 | 13.8% |
            | overweight_level_ii  | 290 | 13.8% |
            | normal_weight  | 287 | 13.6% |
            | insufficient_weight  | 272 | 12.9% |

            Dengan hasil visualisasi data sebagai berikut:

            ![Hasil NObeyesdad](assets/nobeyesdad.png)

      2. Kolom Numerik

         Pada kolom-kolom numerik, fokusnya yaitu melihat pola persebaran data. Berikut detailnya:

            ![Hasil Numerikal](assets/numerical.png)
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

7. Multivariate Analysis

   Pada proses ini, tujuannya adalah mencari relasi pola pada dua atau lebih kolom untuk menyimpulkan keterkaitan antar kolom-kolom itu. Berikut detailnya:

   1. Kolom Kategorikal
      Pada kolom kategorikal, plotting dilakukan pada satu kolom ke kolom target.
      1. Kolom CAEC
            
            ![Hasil CAEC](assets/multi-CAEC.png)

            - Rata-rata BMI bervariasi, dengan frekuensi memakan cemilan kategori "sometimes" memiliki rata-rata tertinggi
            - Frekuensi memakan cemilan kategori "frequently" memiliki rata-rata terendah
            - Dapat diasumsikan bahwa fitur CAEC memiliki pengaruh relatif rendah terhadap fitur BMI

      2. Kolom NObeyesdad
            
            ![Hasil CAEC](assets/multi-NObeyesdad.png)

            - Rata-rata BMI bervariasi, dengan kategori "obesity_type_iii" memiliki rata-rata tertinggi
            - Kategori "insufficient_weight" memiliki rata-rata terendah
            - Dapat diasumsikan bahwa fitur NObeyesdad memiliki pengaruh relatif tinggi terhadap fitur BMi, sebab fitur ini merepresentasikan langsung data BMI yang dikonversikan dalam bentuk kategorikal

   2. Kolom Numerik
      Pada kolom numerik akan dilakukan beberapa langkah plotting dengan memasukkan semua kolom numerikal secara bersamaan. Hal ini berbeda dengan kolom kategorikal yang dilakukan antar dua kolom.

      1. Plotting Pair Plot
            
            ![Hasil Pair Plot](assets/multi-numerical-pairplot.png)

            - Terdapat korelasi positif kuat antara kolom **Weight** dan **BMI** ditandai dengan pola semu menjulang ke atas secara linear. Hal ini sesuai dengan topik data yang digunakan, yaitu representasi keadaan berat badan dengan *Body Mass Index* (BMI) terhadap indikasi obesitas
            - Kolom Height tidak berkorelasi dengan kolom BMI
      2. Plotting Heatmap
            
            ![Hasil Heat Map](assets/multi-numerical-heatmap.png)

            Dari hasil di atas, terlihat bahwa kolom **Weight** memiliki relasi positif kuat dengan kolom **BMI** dengan nilai korelasi mendekati positif (+) 1.

            Hal ini sesuai dengan topik data dan tujuan analisi yaitu obesitas yang berkaitan erat dengan berat badan.

## D. Data Preparation

Pada tahap ini, data yang ada akan diolah sedemikian rupa agar bekerja dengan baik dengan model yang akan dibuat. Fokus pada proses ini adalah mengubah setiap fitur agar dapat menyesuaikan model dengan hasil yang diharapkan. Berikut adalah detailnya:

  1. *Encoding* Fitur Kategorikal
      
      Pada fitur kategorikal dengan tipe data objek, tidak dapat diproses oleh model yang memerlukan nilai numerik. Maka dari itu, perlu dilakukan proses *Encoding*.

      Proses ini dilakukan dengan menggunakan *One Hot Method*.

      ```py
      cleanedObesDf = pd.concat([cleanedObesDf, pd.get_dummies(cleanedObesDf['CAEC'], prefix='calories')], axis=1)

      cleanedObesDf = pd.concat([cleanedObesDf, pd.get_dummies(cleanedObesDf['NObeyesdad'], prefix='obesity')], axis=1)
      ```

      Perintah di atas akan mengubah fitur *CAEC* dan *NObeyesdad* menjadi angka 0 atau 1 pada setiap data unique-nya.

      Setelah itu, dapat menghapus kolom asli dengan kode:

      ```py
      cleanedObesDf.drop(['CAEC', 'NObeyesdad'], axis=1, inplace=True)
      ``` 

      Dengan begitu, ukuran data menjadi tidak terlalu besar. Setelah itu, ternyata data yang tercipta adalah data dengan tipe data boolean. Maka perlu diubah dengan membuat fungsi dan menerapkannya pada setiap data yang ada. Berikut kodenya:

      ```py
      def toInt(value):
      if type(value) == bool:
        if value == True:
            return 1
        else:
            return 0
      else:
        return value
      ```

      Dengan begitu, sekarang nilainya sudah menjadi 0 dan 1 bertipe data integer.

  2. Peninjauan Dimensi Data dengan PCA
     
     Proses ini ditujukan untuk mengurangi dimensi data agar lebih terkonvergensi. Dengan begitu model yang dibuat akan bekerja lebih optimal dan cepat. Namun, sebelumnya harus dilakukan pengecekan korelasi pada fitur-fitur yang akan digunakan sebagai acuan prediksi. Berikut hasilnya:

     ![Hasil PCA](assets/pca.png)

     Dari hasil di atas, ternyata kolom-kolom fitur yaitu Height dan Weight **tidak memiliki korelasi**. Maka tidak akan dilakukan reduksi dimensi agar tidak terjadi kehilangan data yang merusak struktur dataset.

  3. Train Test Split
   
     Proses ini akan membagi dataset menjadi dua, yaitu Fitur X dan Y. Fitur X akan menjadi acuan prediksi, sedangkan Fitur Y akan menjadi bahan belajar mesin dalam mempelajari fitur X. Berikut Kodenya:

     - Fitur X

      ```py
      X = cleanedObesDf.drop(['BMI'], axis=1)
      ```

     - Fitur Y
      
      ```py
      y = cleanedObesDf['BMI']
      ```

     - Pembagian Train dan Test 

      ```py
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.1, random_state=42)
      ```

      Pada pembagian train dan test, disini hanya mengambil **10%** yaitu sebanyak **211** data dari keseluruhan data X sebanyak **2108** data untuk menjadi data test, dengan pengambilan random state pada state **42** dengan tujuan agar data yang diambil konsisten.

  4. Standarisasi Fitur X
     
     Pada proses ini, bertujuan untuk mengubah fitur X asli menjadi nilai-nilai baru dengan skala yang relatif sama atau mendekati distribusi normal. Standarisasi hanya dilakukan pada fitur X untuk menghindari kebocoran data.

     Standarisasi menggunakan fungsi **StandarScaler** dari library Scikit-learn. Berikut kodenya

     ```py
      # Mendefinisikan StandarScaler untuk standarisasi
      scaler = StandardScaler()

      scaler.fit(X_train[numericalFeatures])

      # Melakukan transformasi pada data
      X_train[numericalFeatures] = scaler.transform(X_train.loc[:, numericalFeatures])
     ```

     Dari hasil kode di atas, maka sekarang distribusi data menjadi lebih tereduksi. Berikut adalah hasil pencarian deksripsi statistik pada fitur X:

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

     Dapat dilihat bahwa saat ini rata-rata (mean) dan standar deviasi (std) sudah sama dari kedua kolom yang dilakukan standarisasi. Maka dapat dilanjutkan untuk proses modelling.

## E. Modeling

   Pada proses ini, fokusnya adalah membuat model yang akan melakukan prediksi dari **fitur X** sebagai bahan prediksi dan **fitur y** sebagai acuan belajar pola hasilnya. Jenis algoritma-algoritma yang digunakan adalah **K-Nearest Neighbors dan Random Forest**. Berikut adalah detailnya:
   
   1. K-Nearest Neighbors
      
      K-Nearest Neighbors atau biasa disebut KNN adalah sebuah algoritma yang pada proses prediksinya adalah melakukan pemetaan data prediksi secara acak, lalu akan diambil data dengan jarak terdekat. 
      
      **a. Kelebihan**
      
      - Mudah dipahami dan diimplementasikan, dengan konsep perhitungan jarak antara titik data untuk menentukan tetangga terdekat
      - Tidak diperlukan pembelajaran atau proses *training* ketika membuat model
      - Dapat menangani data non linear dengan dimensi data yang tinggi.

      **b. Kekurangan**

      - Tenaga komputasi yang dihasilkan tinggi, apalagi pada data dengan tingkat dimensi tinggi
      - Sangat sensitif pada data *outliers*, sebab algoritma ini mengedepankan ukuran jarak antar data.
      - Prestasi menurun pada keberlanjutan dimensi, sebab dengan dimensi yang terus meningkat akan menunrunkan makna dari jarak data.

      Lalu, implementasi data pada model adalah sebagai berikut:

      **Pendefinisian Model ke Variabel**
      ```py
      knnModel = KNeighborsRegressor(n_neighbors=5)
      ```
      Perintah di atas adalah untuk merepresentasikan library model ke sebuah variabel agar dapat digunakan setelah melakukan import library **KNeighborsRegressor**. Lalu, terdapat penggunaan parameter disini, yaitu *n_neighbors*. Parameter ini akan memberikan batasan tetangga yang akan dicek dengan batas **5** tetangga terdekat.

      **Fit Data ke Model**
      ```py
      knnModel.fit(X_train, y_train)
      ```
      Perintah di atas bertujuan untuk menyesuaikan model dengan fitur-fitur yang sudah disiapkan yaitu **fitur X** dan **fitur y**.

      **Merangkum Hasil**
      ```py
      trainModels.loc['trainMSE', 'KNN'] = mean_squared_error(y_pred= knnModel.predict(X_train), y_true=y_train)
      ```
      Perintah di atas bertujuan untuk memasukkan hasil prediksi dengan metrik ***Mean Squared Error* (MSE)** yang akan dijelaskan lebih lanjut pada bab evaluasi. Terdapat proses-proses yang terjadi yaitu melakukan prediksi pada fitur *X_train* dengan membandingkan nilai asli **y_train** sebagai bahan acuan. 

   2. Random Forest

      Random Forest adalah algoritma *ensemble* dengan metode *bagging* yang isinya terdapat banyak algoritma yang berjalan secara independen. Dari hasil keseluruhan algoritma, akan dipilih yang memiliki peforma terbaik. Jadi, algoritma Random Forest adalah algoritma yang tersusun dari banyak algoritma pohon (decision tree) dengan pembagian fitur secara acak.

      **a. Kelebihan**
      - Memiliki stabilitas terhadap overfitting, sebab pada prosesnya membangun banyak pohon keputusan yang berbeda lalu digabungkan
      - Tidak sensitif pada outliers, sebab hasil prediksi didasarkan pada mayoritas keputusan pohon
      - Dapat menangani campuran tipe data tanpa memerlukan banyak *preprocessing data*.
      
      **b. Kekurangan**
      - Tidak selalu interpretatif, sulit untuk diintepretasi secara intuitif terutama jika terdapat banyak *decision tree* yang ada di dalam *ensemble*.
      - Rentan pada kesalahan, jika data yang digunakan tidak seimbang
      - Tidak efektif pada data tabular yang linear dengan hubungan linear yang kuat 

      Lalu, implementasi data pada model adalah sebagai berikut:

      **Pendefinisian Model ke Variabel**
      ```py
      rfModel = RandomForestRegressor(n_estimators=10, max_depth=4, random_state=25, n_jobs=-1)
      ```

      Pada proses pendefinisian model pada variabel, terdapat penggunaan parameter-parameter dengan detail sebagai berikut:

      - *n_estimators* dengan nilai **10** untuk melakukan set pohon untuk bercabang sebanyak maksimal **10** kali.
      - *max_depth* dengan nilai **4** agar pohon cabang hanya melakukan percabangan yang lebih kecil lagi sebanyak paling dalam **4** kali kedalaman.
      - *random_state* dengan nilai **25** agar nilai random yang dilakukan *sampling* konsisten pada kombinasi **ke-25**.
      - *n_jobs* dengan nilai **-1** agar pekerjaan yang dilakukan oleh model dilakukan secara paralel pada keseluruhan proses.
  
      **Fit Data ke Model**
      ```py
      rfModel.fit(X_train, y_train)
      ```
      Perintah di atas bertujuan untuk menyesuaikan model dengan fitur-fitur yang sudah disiapkan yaitu **fitur X** dan **fitur y**.

      **Merangkum Hasil**
      ```py
      trainModels.loc['trainMSE', 'RandomForest'] = mean_squared_error(y_pred=rfModel.predict(X_train), y_true=y_train)
      ```
      Perintah di atas bertujuan untuk memasukkan hasil prediksi dengan metrik ***Mean Squared Error* (MSE)** yang akan dijelaskan lebih lanjut pada bab evaluasi. Terdapat proses-proses yang terjadi yaitu melakukan prediksi pada fitur *X_train* dengan membandingkan nilai asli **y_train** sebagai bahan acuan. 

      Setelah proses *training* fitur train baik x maupun y, lalu tampilkan hasilnya dengan perintah :

      ```py
      trainModels.loc['trainMSE', :]
      ``` 

      Hasilnya adalah sebagai berikut :

      | K-Nearest Neighbors | Random Forest|
      |:-:|:-:|
      | 0.148428 | 1.298258 |

      Dari hasil di atas, dapat disimpulkan sementara bahwa **K-Nearest Neighbors** akan dipilih menjadi algoritma solusi, dengan perolehan error terkecil, yaitu **0.148428**. Selain itu, juga algoritma ini ternyata dapat berjalan dengan baik pada data *training* yang digunakan saat ini yang berukuran relatif kecil.

## F. Evaluation

Walaupun sudah terlihat bahwa KNN lebih baik daripada Random Forest, tetapi hal itu masih diambil dari hasil perolehan prediksi **data training** dan perlu untuk melakukan prediksi pada **data testing**. Sebab, pada dasarnya nanti model akan memprediksi data asli, tidak pada data training. Maka diperlukan proses prediksi lagi pada data testing dengan kedua algoritma tersebut.

Pada proses analisis saat ini, prediksi yang dilakukan adalah menggunakan metode regresi, maka metrik yang cocok untuk diujikan adalah *Mean Squared Error* (MSE). 

Metrik ini bekerja dengan menghitung seberapa jauh perbedaan antara nilai sebenarnya dengan nilai hasil prediksi. Semakin jauh perbedaannya, maka semakin tidak akurat. Jauh dan tidaknya dilihat dari hasil *error* yang didapatkan. Berikut adalah formulanya:

MSE = $\frac{1}{n} \sum_{i=1}^{n} (\text{y}_i - \text{y}\_\text{pred}_{i})^2$

Dengan penjelasan sebagai berikut:

- ${n}$ adalah jumlah observasi dalam dataset
- $\text{y}_i$ adalah nilai sebenarnya ke-${i}$
- $\text{y}\_\text{pred}_{i}$ adalah nilai hasil prediksi ke-${i}$

Selanjutnya adalah implementasi pada fitur X_test. Berikut adalah tahapan-tahapannya:

  1. Scaling dengan Standarisasi pada Fitur X_test
   
     Proses scaling pada fitur **X_test** dilakukan agar data pada fitur tersebut dapat terkonvergensi dengan baik ketika akan dimasukkan ke dalam model. 
     
     Langkahnya kurang lebih sama ketika melakukan scaling pada fitur **X_train** pada langkah sebelumnya. Hanya pemilihan fitur saja yang berbeda.

     ```py
     X_test.loc[:, numericalFeatures] = scaler.transform(X_test[numericalFeatures])
     ```

     Mirip dengan hasil standarisasi pada fitur **X_train**, sekarang nilainya tidak terlalu besar untuk dimasukkan ke dalam model.

  2. Evaluasi Metrik
      Seperti pada pernyataan di awal, penentu algoritma yang baik adalah ketika dilakukan uji metrik di **data testing**, sebagai representasi data baru. Data dapat dikatakan **baru** dikarenakan tidak ada pada hasil pembelajaran di **data training**. Maka dapat dilakukan evaluasi metrik pada kedua algoritma ini.

      - Evaluasi KNN
         ```py
         trainModels.loc['testMSE', 'KNN'] = mean_squared_error(y_pred=knnModel.predict(X_test), y_true=y_test)
         ```

      - Evaluasi Random Forest
         ```py
         trainModels.loc['testMSE', 'RandomForest'] = mean_squared_error(y_pred=rfModel.predict(X_test), y_true=y_test)
         ```

      Setelah dilakukan prediksi menggunakan kedua algoritma tersebut pada data testing, selanjutnya dapat ditampilkan hasil dari keduanya. Hasilnya adalah:

      **Hasil tabel**

      | | KNN | Random Forest|
      |:-|:-:|:-:|
      | trainMSE | 0.148428 | 1.298258 |
      | testMSE | 0.413398 | 1.384255 |

      **Visualisasi Error**
      ![Hasil Komparasi](assets/compare-error.png)
      Dari tabel hasil di atas, dapat disimpulkan bahwa ternyata saat dilakukan evaluasi metrik pada KNN dan Random Forest menggunakan MSE, hasil uji data testing pada **KNN** lebih kecil daripada **Random Forest** dari segi nilai *error*-nya. 
      

      Untuk sementara dapat dikatakan bahwa **KNN lebih baik** performanya dibandingkan dengan Random Forest. Selanjutnya dapat dilakukan evaluasi hasil prediksi.

  3. Evaluasi Prediksi

      Untuk memastikan algoritma mana yang cocok adalah mencoba membandingkan data asli dengan data hasil prediksi. Semakin mirip, maka algoritma itu baik performanya dalam memprediksi.

      Yang perlu dilakukan adalah mengumpulkan sample yang akan diuji, dengan langkah-langkah sebagai berikut:

      **Pengambilan Sample**
      ```py
      # Ambil Nilai X dari X_test
      XForPredict = X_test[:3].copy()
      # Ambil Nilai y asli dari y_test
      yForPredict = {'y_true':y_test[:3]}
      ```

      Sample data di ambil dari 3 data teratas dari data testing x, begitu juga data harapan nilai asli diambil dari 3 data teratas dari data testing y.

      Setelah sample data didapatkan, maka dapat langsung saja dilakukan prediksi untuk melihat seberapa baik kedua algoritma tersebut memprediksi.

      **Pengujian Prediksi**
      ```py
      for name, model in modelDict.items():
         yForPredict['prediksi_'+name] = model.predict(XForPredict).round(1)

      pd.DataFrame(yForPredict)
      ```

      Hasilnya adalah:
      | | y_true | prediksi_KNN | prediksi_RF|
      |:-:|:-:|:-:|:-:|
      | 1446 | 31.896722 | 31.9 | 32.8 |
      | 2077 | 46.027679 | 46.5 | 47.5 |
      | 1204 | 28.969812 | 28.9 | 27.4 |

      Ternyata, sudah jelas bahwa algoritma **K-Nearest Neighbors** lebih unggul daripada algoritma **Random Forest** dalam hal memprediksi nilai **BMI** dari bahan ajar nilai **Berat Badan (Weight)** dan **Tinggi Badan (Height)** dengan selisih nilai asli dan nilai prediksi yang sedikit.

      Note:

      Jika membutuhkan data assets berupa gambar visualisasi data, tekan [tulisan ini](https://drive.google.com/drive/folders/1BfC2oPBtgQg049I64Q1BAPjCuqi-IKlm?usp=sharing). Karena pengerjaan menggunakan lokal **Jupyter Notebook**