# Laporan Proyek Machine Learning: Analisa Data Obesitas 
# Nama : Muhammad Faishal Ali D.

## Domain Proyek
### Penjelasan Umum
Masalah gizi merupakan hal yang sangat kompleks dan serius. Karena menyangkut kualitas penerus-penerus bangsa. Seperti halnya di Indonesia. Salah satu masalah gizi yang masih menjadi pembahasan hangat adalah obesitas.

Obesitas merupakan suatu kondisi medis yang ditandai oleh penimbunan lemak tubuh berlebihan, yang dapat meningkatkan risiko terjadinya berbagai penyakit kronis. Faktor-faktor seperti pola makan yang tidak sehat, gaya hidup yang kurang aktif, dan perubahan budaya telah berkontribusi pada meningkatnya angka obesitas di seluruh dunia.

Menurut data Organisasi Kesehatan Dunia (WHO), obesitas telah mencapai tingkat epidemiologi, dengan lebih dari 650 juta orang dewasa di seluruh dunia dinyatakan obesitas pada tahun 2016. Hal ini menunjukkan bahwa obesitas bukan lagi hanya masalah kesehatan individu, tetapi juga menjadi beban kesehatan masyarakat yang signifikan. Obesitas dapat timbul disebabkan oleh beberapa hal sebagai berikut:

1. Kurangnya aktifitas fisik baik kegiatan harian maupun latihan fisik terstruktur
2. keturunan genetika
3. Faktor lingkungan

### Sebab Akibat Masalah
Hal ini perlu dilakukan analisis serta penanggulangan lebih lanjut, sebab obesitas dapat meningkatkan risiko terjadinya penyakit-penyakit kardiovaskular, diabetes tipe 2, dan tekanan darah tinggi. Selain itu, biaya kesehatan yang terkait dengan pengobatan dan manajemen obesitas memberikan tekanan tambahan pada sistem kesehatan nasional.

Maka dari itu, perlu melakukan berbagai strategi untuk mengurangi resiko masyarakat terkena obesitas. Seperti anjuran mengkonsumsi makanan sehat, olahraga, serta pengadaan infrastruktur ideal untuk peninjauan status tubuh.

Disini saya berinisiatif untuk melakukan analisis lebih lanjut mengenai data masyarakat beserta label yang menunjukkan apakah sedang mengalami obesitas atau tidak. Serta menganalisis data makanan sehat dengan rincian gizi dengan tujuan untuk memberikan edukasi terhadap masyarakat dalam memilih makanan yang sehat.

### Referensi
   1. [Referensi Pertama](https://d1wqtxts1xzle7.cloudfront.net/39625453/jurnal-libre.pdf?1446519911=&response-content-disposition=inline%3B+filename%3DFAKTOR_RISIKO_OBESITAS_PADA_ANAK_5_15_TA.pdf&Expires=1706423938&Signature=CfseHwMvVXjfNg90XPlccC~RocUVem5IncpL82cJPnYcPEL9rRJgkjy3eA5AFzVMKtvSfxJfO~WGhARcxrvmn3MGkw6Eslf5UwFnNZFL5zqd7UamxeWU0mZ2qS0SAH~kcO7cF4DDHQQADyGNDPTLRRlxdL0-cpA35~ZzhmjrPqxNmbFkCKNKFz4YCsUBc4v~Hffnyl2ZjMkcR1MkJ~XBr8kJKCnQS~OaFeWkjetvIkn4FR-OBOJEXffkgmohYc~-09NT0WjluDqHP3Dx-Dt1-bhGIqowCqQEUGgfl6pvdA6O2BK-ZiNJvI~sDgZVKukUQdQpFvJgz7PDPFqNHVEQ9w__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
   2. [Referensi Kedua](https://pgm.persagi.org/index.php/pgm/article/view/47)
   3. [Referensi Ketiga](https://journals.telkomuniversity.ac.id/jett/article/download/1395/1005/)
   

## Business Understanding
Pada proses analisis ini, saya berfokus untuk mengambil permasalahan-permasalahan yang akan diangkat dari permasalahan garis besar untuk mencari solusi yang tepat. Berikut adalah uraiannya:

### Problem Statements
1. Bagaimana cara untuk mengurangi potensi masyarakat terkena obesitas?
> Mengangkat masalah pada potensi masyarakat terkena obesitas, seperti pola hidup, dan makanan yang dikonsumsi.
2. Dari segi aspek apa analisis akan dilakukan?
> Mencari aspek yang dapat dianalisis seperti berat badan, BMI, kecukupan kalori pada makanan, dan lain-lain. 
3. Bagaimana pengaruh konsumsi masyarakat terhadap potensi terkena obesitas?
> Merupakan lanjutan dari problem statement poin 2, yaitu analisis makanan-makanan yang dikonsumsi. Seperti kandungan kalori, dan lemak.

### Goals
1. Memberikan insight pada data mengenai kriteria penderita obesitas.
> Memberikan informasi terhadap data orang yang terkena obesitas maupun tidak. Berdasarkan ukuran badan seperti tinggi badan, berat badan, dan BMI.
2. Memberikan gambaran umum pada makanan-makanan yang sehat.
> Memberikan informasi terkait makanan-makanan yang cocok serta rendah kalori untuk mencegah terkena obesitas atau untuk diet.

### Solution Statements
1. Membuat analisis data dengan visualisasi data yang menggambarkan kondisi data untuk prediksi pada tahap modelling.
2. Membuat model regresi dan klasifikasi (labelling) pada data obesitas menggunakan **Random Forest**.
3. Melakukan hyperparameter tuning pada *n_estimator*, *random_state*, *n_jobs*, dan *max_depth* untuk mengoptimalisasi kinerja model. 
4. Menggunakan metrik evaluasi *Mean Squared Root* (MSE)