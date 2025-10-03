# Olist E-Commerce Seller Segmentation Analysis

## Latar Belakang
E-commerce adalah model bisnis yang memungkinkan perusahaan atau individu untuk membeli atau menjual barang melalui internet. Pelanggan e-commerce memiliki karakteristik yang sangat beragam, sehingga penting untuk memahami segmen pelanggan target agar strategi komunikasi pemasaran efektif (menarik dan mendorong tindakan) serta tepat sasaran (tidak menyinggung, tepat waktu, dan relevan). Analisis RFM (Recency, Frequency, Monetary) adalah teknik segmentasi perilaku pelanggan yang berfokus pada tiga aspek utama transaksi pelanggan:
- **Recency**: Waktu sejak pembelian terakhir pelanggan.
- **Frequency**: Jumlah pembelian yang dilakukan pelanggan.
- **Monetary**: Total nilai moneter dari transaksi pelanggan.

Memahami perilaku ini memungkinkan bisnis seperti Olist untuk mengelompokkan pelanggan ke dalam segmen yang berbeda untuk pemasaran yang lebih terarah.

## Identifikasi Masalah
### Definisi Masalah
Pelanggan mengunjungi situs e-commerce dengan berbagai tujuan, mulai dari pembelian sederhana (misalnya, membeli mesin kopi) hingga tugas kompleks (misalnya, memperbaiki lubang di dinding). Tujuan ini tercermin melalui perilaku pengguna seperti kueri pencarian, klik, tampilan halaman, dan pembelian. Dengan menganalisis perilaku pengguna, kita dapat menyimpulkan strategi umum yang digunakan pelanggan untuk mencapai tujuan mereka. Tantangannya adalah data yang tersedia belum dihitung nilai RFM-nya. Untuk membuat analisis data lebih jelas, kita perlu menghitung nilai RFM dan mengelompokkan pelanggan berdasarkan analisis RFM.

### Tujuan Bisnis
Berdasarkan dataset yang tersedia, analisis RFM digunakan untuk memahami kebiasaan setiap segmen pelanggan Olist. Segmentasi pelanggan yang dihasilkan dari proyek ini akan membantu Olist menerapkan strategi pemasaran/iklan yang sesuai untuk setiap segmen. Harapan dari proyek machine learning ini adalah menciptakan algoritma berbasis analisis RFM untuk pengelompokan pelanggan, sehingga Olist dapat memahami karakteristik pengguna. Tujuan utama proyek ini adalah memenuhi ekspektasi algoritma untuk pengelompokan segmen pengguna melalui tujuan berikut:
- Mengelompokkan pelanggan berdasarkan perilaku mereka ke dalam beberapa segmen berdasarkan analisis RFM.
- Mengetahui karakteristik utama dari setiap segmen pelanggan.

Tujuan ini akan membantu tim bisnis Olist merumuskan strategi pemasaran/iklan berdasarkan jenis atau karakteristik setiap klaster yang terbentuk.

## Kebutuhan Data
Untuk melakukan segmentasi pelanggan menggunakan analisis RFM dan mengidentifikasi karakteristik setiap kelompok, kita perlu menghitung:
- **Recency**: Selang waktu antara pembelian terakhir dan saat ini.
- **Frequency**: Frekuensi pembelian pelanggan.
- **Monetary**: Total nilai transaksi pelanggan.

## Pendekatan Analitik
### Teknik Berbasis Pengetahuan Domain
Setelah menghitung nilai Recency, Frequency, dan Monetary untuk setiap pelanggan, pelanggan disegmentasikan berdasarkan nilai kuantil untuk Monetary dan Recency. Untuk Frequency, metode elbow digunakan untuk menentukan ambang batas yang relevan.

### Teknik Machine Learning
- **KMeans Clustering**: Diterapkan setelah menskalakan fitur RFM (menggunakan StandardScaler karena distribusi data tidak normal) untuk membentuk segmen pelanggan. Jumlah klaster optimal (6) ditentukan menggunakan skor siluet. Segmen meliputi Pasif, Reguler, Sesekali, Berharga, Loyal, dan Terbaik, dengan Pasif mewakili pelanggan dengan nilai RFM terendah.
- **DBSCAN**: Diterapkan pada sekitar 10% data karena keterbatasan daya komputasi, dengan segmentasi berdasarkan parameter noise, epsilon, dan min_samples. Hasilnya adalah 7 klaster: Pasif, Reguler, Sesekali, Berharga, Loyal, Emas, dan Terbaik.

### Risiko
Segmentasi pelanggan yang salah dapat menyebabkan:
- Pemborosan anggaran pemasaran.
- Iklan yang tidak tepat sasaran.
- Segmentasi pelanggan yang tidak relevan, sehingga kehilangan peluang peningkatan penjualan di masa depan.

### Pengukuran Kinerja
- **KMeans**: Dievaluasi menggunakan skor siluet untuk mengukur kohesi dan pemisahan klaster.
- **DBSCAN**: Dievaluasi berdasarkan tingkat noise, epsilon, dan parameter min_samples.

## Tindakan
Hasil segmentasi dapat digunakan oleh tim bisnis Olist untuk memahami pelanggan lebih baik dan menerapkan strategi pemasaran atau promosi yang lebih terarah untuk meningkatkan pendapatan.

## Nilai
Proyek ini menghemat biaya pemasaran dengan menargetkan segmen pelanggan yang memiliki peluang pembelian tertinggi, alih-alih memasarkan ke semua pelanggan yang mungkin tidak tertarik. Pendekatan ini juga meningkatkan tingkat keterlibatan pelanggan melalui pengalaman yang lebih personal.

## Pemahaman dan Persiapan Data
Analisis dimulai dengan mengimpor dataset yang diperlukan, menganalisis kolom, membuat fitur baru, dan mengonversi format data ke bentuk yang lebih mudah digunakan. Tabel-tabel yang relevan digabungkan menjadi satu tabel dasar analitik untuk exploratory data analysis (EDA), menangani data yang hilang, dan memilih fitur yang relevan untuk pemodelan. Fitur baru, termasuk metrik RFM (Recency, Frequency, Monetary), dibuat:
- **Recency**: Waktu sejak pembelian terakhir.
- **Frequency**: Jumlah pembelian.
- **Monetary**: Total nilai transaksi.

## Pemodelan
### Klasterisasi Berbasis Pengetahuan Domain
Pelanggan disegmentasikan ke dalam 4 klaster (Pasif, Reguler, Berharga, Royal) berdasarkan skor RFM, dengan kuantil digunakan untuk Recency dan Monetary, serta metode elbow untuk Frequency. Skor diakumulasikan untuk menentukan klaster.

### KMeans Clustering
KMeans dipilih karena kesederhanaan dan biaya komputasi rendah. Fitur disesuaikan dengan StandardScaler karena distribusi data tidak normal. Enam klaster (Pasif, Reguler, Sesekali, Berharga, Loyal, Terbaik) diidentifikasi berdasarkan evaluasi skor siluet, dengan Pasif mewakili pelanggan dengan nilai RFM terendah.

### DBSCAN Clustering
DBSCAN diterapkan pada ~10% data karena keterbatasan komputasi, menghasilkan 7 klaster (Pasif, Reguler, Sesekali, Berharga, Loyal, Emas, Terbaik) berdasarkan parameter noise, min_samples, dan epsilon.

## Evaluasi
Berdasarkan segmentasi klaster menggunakan pendekatan non-model, KMeans, dan DBSCAN, segmentasi KMeans dengan 6 klaster (Pasif, Reguler, Sesekali, Berharga, Loyal, Terbaik) memberikan hasil paling jelas dengan meminimalkan tumpang tindih antar klaster. Ini memungkinkan Olist untuk menganalisis pelanggan secara akurat, mendukung pemasaran relasi, dan meningkatkan profitabilitas dengan menangani kebutuhan pelanggan secara efektif.

Segmentasi non-model menghasilkan tumpang tindih antara klaster rendah, menengah, dan tinggi, sehingga sulit untuk dianalisis, meskipun lebih sederhana karena hanya memiliki 4 kelompok. DBSCAN menghasilkan 7 klaster yang lebih jelas dibandingkan non-model, tetapi sulit dipahami karena jumlah klaster yang lebih banyak. Selain itu, DBSCAN menunjukkan tumpang tindih pada hubungan Recency-Monetary, meskipun hubungan Recency-Frequency dan Frequency-Monetary terpisah dengan baik.

KMeans memberikan segmentasi paling jelas meskipun ada sedikit tumpang tindih pada hubungan Recency-Monetary untuk klaster menengah, menjadikannya pendekatan terbaik untuk kebutuhan segmentasi Olist.

## Dependensi
Notebook menggunakan pustaka Python berikut:
- `pandas`, `numpy`: Manipulasi data.
- `matplotlib`, `seaborn`: Visualisasi.
- `scikit-learn`: Preprocessing, klasterisasi, dan metrik evaluasi.
- `itertools`, `warnings`: Fungsi utilitas.

Instalasi dependensi (di luar Colab):
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Cara Menjalankan Notebook
1. Buka notebook (`Final_Project_Team_Alpha (3).ipynb`) di Google Colab atau lingkungan Jupyter lokal.
2. Jika menggunakan Colab, sambungkan ke Google Drive:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Pastikan dataset Olist tersedia di jalur Google Drive yang sesuai.
4. Jalankan sel secara berurutan.
5. Pastikan backend matplotlib mendukung output inline untuk visualisasi.

## Mengunduh README
Untuk mengunduh file `README.md`:
1. Salin isi file ini.
2. Buat file baru bernama `README.md` di editor teks atau IDE.
3. Tempel isi file dan simpan dengan ekstensi `.md`.
4. Alternatifnya, di Google Colab, jalankan:
   ```python
   with open('README.md', 'w') as f:
       f.write('''[Tempel isi README di sini]''')
   ```
   Kemudian unduh file melalui file explorer Colab (klik kanan > Download).

## Kontributor
- Team Alpha (Proyek Akhir)

Jika ada pertanyaan atau masalah, silakan buka issue di repositori ini.

---
*Notebook ini dibuat sebagai bagian dari proyek akhir. Dataset bersifat ilustrasi dan mungkin memerlukan penyesuaian jalur file.*
