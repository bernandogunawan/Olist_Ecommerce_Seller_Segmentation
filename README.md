# Olist E-Commerce Seller Segmentation Analysis

Ini adalah README untuk file Jupyter Notebook `Final_Project_Team_Alpha (3).ipynb`. Notebook ini berisi analisis segmentasi seller pada platform e-commerce Olist menggunakan pendekatan RFM (Recency, Frequency, Monetary) + Rating Analysis, dengan implementasi clustering menggunakan algoritma machine learning seperti DBSCAN dan KMeans.

## Deskripsi Proyek
Proyek ini melakukan analisis perilaku seller di Olist, sebuah platform B2B2C e-commerce enabler asal Brasil. Tujuannya adalah mengidentifikasi segmen seller berdasarkan aktivitas mereka untuk mendukung strategi retensi, pengembangan, dan optimasi revenue. Analisis mencakup exploratory data analysis (EDA), perhitungan metrik RFM + Rating, segmentasi manual, dan clustering dengan ML. Hasilnya memberikan insight tentang seller berkinerja tinggi, sedang, dan rendah, beserta rekomendasi bisnis.

Notebook ini dibangun menggunakan Google Colab dan memerlukan akses ke Google Drive untuk memuat dataset.

## Tujuan Proyek
- Melakukan RFM + Rating Analysis pada seller untuk mengukur aktivitas dan kontribusi mereka.
- Mengelompokkan seller ke dalam segmen bermakna (misalnya: Top Sellers, Steady Sellers, Casual Sellers).
- Memberikan rekomendasi strategi bisnis, seperti program retensi dan insentif.
- Menyediakan dasar untuk pengembangan model prediksi churn atau scoring seller.

## Dataset
Dataset yang digunakan berasal dari Olist E-Commerce (tidak disertakan dalam repo ini, asumsikan disimpan di Google Drive). Dataset mencakup:
- Data transaksi order, seller, review, dan pembayaran.
- Kolom kunci: `seller_id`, `order_purchase_timestamp`, `payment_value`, `review_score`, dll.

Data diproses untuk menghitung:
- **Recency**: Waktu sejak order terakhir.
- **Frequency**: Jumlah order per seller.
- **Monetary**: Total nilai transaksi per seller.
- **Rating**: Rata-rata review score per seller.

## Metodologi
### 1. Business Understanding
- Kontekstualisasi bisnis Olist.
- Identifikasi stakeholder, problem statements, dan objectives.

### 2. Analytical Approach
- **Analisis Manual**: Distribusi RFM + Rating, segmentasi berbasis kuartil.
- **Machine Learning**:
  - Preprocessing: Scaling dengan RobustScaler/StandardScaler.
  - Clustering: DBSCAN (untuk deteksi outlier) dan KMeans (dengan Elbow Method/Silhouette Score untuk tentukan jumlah cluster).
  - Evaluasi: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index.
- Visualisasi: Scatterplot, boxplot, dan heatmap untuk interpretasi cluster.

### 3. Business Flow
- Perbandingan proses bisnis sebelum dan sesudah analisis (termasuk estimasi biaya churn dan operasional).
- Terminologi bisnis seperti churn, retention, dan RFM segmentation.

### 4. Hasil
- Tiga cluster utama:
  - **Casual Sellers**: Recency tinggi, frequency/monetary rendah (mayoritas seller).
  - **Steady Sellers**: Recency sedang, frequency/monetary moderat.
  - **Top Sellers**: Recency rendah, frequency/monetary tinggi.
- Visualisasi perbandingan antar cluster (scatterplot total customer vs frequency).

### 5. Limitasi
- Sensitivitas terhadap outlier dan asumsi bentuk cluster.
- Model bergantung pada data saat ini; perlu update berkala.
- Tidak ada data eksternal seperti geolokasi atau kategori produk.

### 6. Kesimpulan & Rekomendasi
- Kesimpulan: Mayoritas seller di segmen rendah, tapi segmen atas berkontribusi besar pada revenue. Potensi pengurangan churn 20-30% dengan strategi targeted.
- Rekomendasi:
  - Program reaktivasi untuk Casual Sellers.
  - Upscaling dan insentif untuk Steady Sellers.
  - Loyalitas eksklusif untuk Top Sellers.
  - Integrasi dashboard real-time dan model prediksi churn.

## Dependensi
Notebook menggunakan library berikut:
- `pandas`, `numpy` untuk manipulasi data.
- `matplotlib`, `seaborn` untuk visualisasi.
- `sklearn` untuk preprocessing, clustering, dan evaluasi metrik.
- `itertools`, `warnings` untuk utilitas.

Instalasi (jika di luar Colab):
```
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Cara Menjalankan Notebook
1. Buka notebook di Google Colab atau Jupyter lokal.
2. Mount Google Drive (jika menggunakan Colab):
   ```
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Pastikan dataset Olist tersedia di path Google Drive yang sesuai.
4. Jalankan sel secara berurutan.
5. Notebook mencakup visualisasi; pastikan matplotlib backend mendukung output inline.

## Download README
Untuk mendownload file `README.md`:
1. Salin isi file ini dari output.
2. Buat file baru bernama `README.md` di editor teks atau IDE.
3. Paste konten di atas dan simpan dengan ekstensi `.md`.
4. Alternatifnya, jika menggunakan Google Colab, gunakan perintah berikut untuk menyimpan file:
   ```python
   with open('README.md', 'w') as f:
       f.write('''[paste konten README di sini]''')
   ```
   Lalu unduh file dari Colab menggunakan menu File > Download.

## Kontributor
- Team Alpha (Final Project).

Jika ada pertanyaan atau isu, buka issue di repo ini.

---
*Notebook ini dibuat sebagai bagian dari proyek akhir. Data bersifat contoh dan mungkin memerlukan penyesuaian path file.*
