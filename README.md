# Olist E-Commerce Seller Segmentation Analysis

## Deskripsi Proyek
Proyek ini melakukan analisis perilaku seller di Olist, sebuah platform B2B2C e-commerce enabler asal Brasil. Tujuannya adalah mengidentifikasi segmen seller berdasarkan aktivitas mereka untuk mendukung strategi retensi, pengembangan, dan optimasi revenue. Analisis mencakup exploratory data analysis (EDA), perhitungan metrik RFM + Rating, segmentasi manual, dan clustering dengan ML. Hasilnya memberikan insight tentang seller berkinerja tinggi, sedang, dan rendah, beserta rekomendasi bisnis.

## Tujuan Proyek
- Melakukan RFM + Rating Analysis pada seller untuk mengukur aktivitas dan kontribusi mereka.
- Mengelompokkan seller ke dalam segmen bermakna (misalnya: Top Sellers, Steady Sellers, Casual Sellers).
- Memberikan rekomendasi strategi bisnis, seperti program retensi dan insentif.
- Menyediakan dasar untuk pengembangan model prediksi churn atau scoring seller.

## Dataset
Dataset yang digunakan berasal dari Olist E-Commerce yang didapat dari [kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

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
- **Analisis Manual**: Distribusi RFM + Rating.
- **Machine Learning**:
  - Preprocessing: Scaling dengan RobustScaler/StandardScaler.
  - Clustering: DBSCAN (untuk deteksi outlier) dan KMeans (dengan Elbow Method/Silhouette Score untuk tentukan jumlah cluster).
  - Evaluasi: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index.
- Visualisasi: Scatterplot, boxplot, decision boundary untuk interpretasi cluster.

### 3. Business Flow
- Perbandingan proses bisnis sebelum dan sesudah analisis dan machine learning (termasuk estimasi biaya churn).
- Terminologi bisnis seperti churn, retention, dan RFM segmentation.

### 4. Hasil
- Tiga cluster utama:
  - **Casual Sellers**: Recency tinggi, frequency/monetary rendah (mayoritas seller).
  - **Steady Sellers**: Recency sedang, frequency/monetary moderat.
  - **Top Sellers**: Recency rendah, frequency/monetary tinggi.
- Visualisasi perbandingan antar cluster dengan scatterplot.

### 5. Limitasi
- Sensitivitas terhadap outlier dan asumsi bentuk cluster.
- Model bergantung pada data saat ini. Perlunya update berkala.
- Tidak ada data eksternal seperti geolokasi atau kategori produk.

### 6. Kesimpulan & Rekomendasi
- Kesimpulan: Mayoritas seller di segmen rendah, sedangkan segmen atas memiliki revenue per seller yang tinggi.
- Rekomendasi:
  - Program reaktivasi untuk Casual Sellers.
  - Upscaling dan insentif untuk Steady Sellers.
  - Loyalitas eksklusif untuk Top Sellers.
  - Mengembangkan model prediksi churn.

## Kontributor
- [Patrick Jonathan]()
- [Reyhan Kurniawan](https://github.com/ReyhanKurniawan10)
- [Bernando Virto Gunawan](https://github.com/bernandogunawan)

