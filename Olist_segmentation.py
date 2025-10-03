import os
import io
import joblib
import numpy as np
import pandas as pd
import seaborn as sb
import streamlit as st
import matplotlib.pyplot as plt


FEATURES = ["recency", "frequency", "monetary", "average_rating"]
MODEL_PATH = "D:/Ds_bootcamp/final_project/model_cluster.joblib"

DEFAULTS = {
    "recency" : 1,
    "frequency" : 12,
    "monetary" : 1000,
    "average_rating" : 5
} 
cluster_names = {
    0: "Casual Seller",
    1: "Top Seller",
    2: "Steady Seller"
}
treatments = {
    0: "- Reaktivasi Marketing\n- Voucher Transaksi\n- Seleksi & Evaluasi",
    1: "- Loyalty Program\n- Insentif Transaksi\n- Promosi VIP",
    2: "- Training & Edukasi\n- Subsidi Promosi\n- Reward Target"
}
IMAGE_PATH = "D:/Ds_bootcamp/final_project/dataset/logo_olist_d7309b5f20.png"

# ----------------------------
# Utilities
# ----------------------------
@st.cache_resource(show_spinner=True)
def load_model(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Model file '{path}' not found. Place your model next to app.py."
        )
    return joblib.load(path)


def ensure_feature_order(df: pd.DataFrame) -> pd.DataFrame:
    missing = []  
    for column in FEATURES:
        if column not in df.columns:
            missing.append(column)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    return df[FEATURES]


# ----------------------------
# Sidebar — global controls
# ----------------------------
with st.sidebar:

    st.image(IMAGE_PATH)

    st.markdown("# **Apa Itu Olist?**")
    st.write(
        """Olist adalah sebuah platform B2B2C e-commerce enabler asal Brasil 
        yang membantu penjual (seller) mendistribusikan produknya ke berbagai 
        marketplace besar di Brasil.
        """
        )
    st.divider()
    st.subheader("Cara Penggunaan")
    st.write(
        """
        1. Jika menggunakan batch file, data wajib diolah dengan format 4 kolom, yaitu recency, freqeuncey, monetary, dan average_rating
        2. Masukkan data seller
        3. Klik tombol predict
        """
    )

    st.divider()
    st.subheader("Authors")
    st.write(
        """
        - [Bernando Virto Gunawan](https://www.linkedin.com/in/bernando-gunawan-45790024b/)
        - [Patrick Jonathan](http://www.linkedin.com/in/patrick-jonathan-69237821a)
        - [Reyhan Kurniawan](https://www.linkedin.com/in/reyhan-kurniawan/)
        """
    )

# ----------------------------
# Load model once
# ----------------------------
try:
    model = load_model(MODEL_PATH)
except Exception as e:
    st.error(str(e))
    st.stop()

# ----------------------------
# Header
# ----------------------------
st.title("🛍️ Segmentasi Seller Olist")
st.caption("Menos ferramentas, mais resultado em vendas") # fewer tools, more sales result

# Tabs for UX
TAB_HOME, TAB_INFO_CLUSTER, TAB_MODEL, TAB_PREDICTION, TAB_ANALYSIS = st.tabs([
    "Overview",
    "Info Cluster",
    "Model Info",
    "Prediction",
    "Results Analysis"
])

# ----------------------------
# Tab: Overview
# ----------------------------
with TAB_HOME:
    st.subheader("Tentang Aplikasi")
    st.markdown(
        """
        Aplikasi ini digunakan untuk memprediksi segmen seller di Olist 
        sehiingga memudahkan Olist memutuskan treatment yang akan diberikan.

        Features yang digunakan adalah:
        - Recency: Lama sejak terakhir seller melakukan transaksi
        - Frequency: Jumlah transaksi seller
        - Monetary: Jumlah pendapatan seller
        - Average_rating: Rating rata-rata seller
        """
    )
# ----------------------------
# Tab: Info Cluster
# ----------------------------
with TAB_INFO_CLUSTER:
    st.subheader("📊 Info Cluster")
    st.markdown(
        """
        Terdapat 3 kelompok seller berdasarkan RFM dan Review Score.
        - Top Seller: merupakan seller dengan R, F, M, dan Review Score tinggi.
        - Steady Seller: merupakan seller dengan R, F, M, dan Review Score sedang.
        - Casual Seller: merupakan seller dengan R, F, M, dan Review Score rendah.

        Treatment yang akan diberikan untuk setiap Kelompok adalah sebagai berikut:
        - Top Seller: Loyalty Program, Insentif Transaksi, Promosi VIP
        - Steady Seller: Training & Edukasi, Subsidi Promosi, Reward Target
        - Casual Seller: Reaktivasi Marketing, Voucher Transaksi, Seleksi & Evaluasi
        """
    )

# Initialisasi
recency = frequency = monetary = average_rating = None

# ----------------------------
# Tab: Model Info
# ----------------------------
with TAB_MODEL:
    st.subheader("🧠 Model Info")
    st.markdown(
        """
        Model yang digunakan adalah K-Means. K-Means adalah algoritma clustering yang membagi data ke dalam
        k kelompok (cluster) berdasarkan kemiripan jarak.

        **Cara Kerja Model**
        - Pilih secara acak 3 titik awal sebagai pusat cluster (centroid).
        - Hitung jarak setiap data ke semua centroid, lalu tempatkan data ke cluster dengan centroid terdekat.
        - Perbarui posisi centroid dengan menghitung rata-rata semua titik dalam setiap cluster.
        - Ulangi proses penugasan data dan pembaruan centroid hingga posisi centroid tidak banyak berubah atau sudah mencapai kondisi konvergen.
        - Hasil akhirnya: data terbagi ke dalam 3 cluster sesuai pola kedekatannya.

        **Metrik yang digunakan**
        - Silhouette Score
        - Davies-Bouldin Index
        - Calinski-Harabasz Index
        """
    )

# ----------------------------
# Tab: Prediction
# ----------------------------
with TAB_PREDICTION:
    st.subheader("🔮 Predict seller")

    insert_type = st.radio("Insert Type:", ["Manual Input", "Batch Upload"])

    if insert_type == "Manual Input":
        col1, col2 = st.columns(2)
        with col1:
            recency = st.number_input("Recency (Hari)", min_value=1, max_value=1000, value=1, step=1)
            average_rating = st.number_input("Average Rating", min_value=0, max_value=5, value=1, step=1)

        with col2:
            frequency = st.number_input("Frequency", min_value=0, max_value=2000, value=0, step=1)
            monetary = st.number_input("Monetary", min_value=0, max_value=500000, value=0, step=1)

    elif insert_type == "Batch Upload":
        st.markdown("Data wajib diolah terlebih dahulu dengan format 4 kolom, yaitu recency, freqeuncey, monetary, dan average_rating")
        uploaded_file = st.file_uploader("Upload CSV/Excel for batch prediction", type=['csv','xlsx'])
        if uploaded_file:
            try:
                if uploaded_file.name.endswith(".csv"):
                    batch_data = pd.read_csv(uploaded_file)
                else:
                    batch_data = pd.read_excel(uploaded_file)
                    
                    # Ensure the batch data has the required columns
                if not all(col in batch_data.columns for col in FEATURES):
                    st.error("Batch data is missing required columns.")
                else:
                    recency = batch_data.iloc[0]["recency"]
                    frequency = batch_data.iloc[0]["frequency"]
                    monetary = batch_data.iloc[0]["monetary"]
                    average_rating = batch_data.iloc[0]["average_rating"]

            except Exception as e:
                st.error(f"Error reading file: {e}")

    submitted = st.button("Prediksi")

    if submitted:
        if insert_type == "Manual Input":
            input_df = pd.DataFrame([
                {
                    "recency": recency,
                    "frequency": frequency,
                    "monetary": monetary,
                    "average_rating": average_rating
                }]
            )
        else:
            input_df = batch_data
        try:
            input_df = ensure_feature_order(input_df)
            cluster = model.predict(input_df)
            unique_clusters = np.unique(cluster)
            if len(unique_clusters) == 1:
                st.write(f"**Cluster hasil prediksi: {cluster_names.get(unique_clusters[0],"Unknown")}**")
            st.write("Prediksi berhasil! Silahkan ke Tab Results Analysis untuk melihat hasil prediksi.")
        except Exception as ex:
            st.error(f"Prediction failed: {ex}")

# ----------------------------
# Tab: Results Analysis
# ----------------------------
with TAB_ANALYSIS:
    st.subheader("📊 Results Analysis")

    # Cek apakah ada hasil prediksi
    if 'cluster' in locals():
        # Menampilkan hasil prediksi cluster
        if len(input_df) == 1:
            st.write(f"**Seller ini termasuk dalam cluster {cluster_names.get(cluster[0],"Unknown")}**")

        # Membuat DataFrame untuk seller yang diprediksi
        results_df = input_df.copy()
        results_df['Cluster'] = cluster

        if len(input_df) >= 5:
            st.markdown("### Visualisasi Fitur Seller yang Diprediksi")

            # Plotting untuk menunjukkan seller yang diprediksi dengan fitur-fitur terkait
            fig, ax = plt.subplots(3, 2, figsize=(12, 15))  # 3 baris, 2 kolom

            # Recency x Frequency
            sb.scatterplot(data=results_df, x='recency', y='frequency', ax=ax[0, 0])
            ax[0, 0].set_title('Recency x Frequency for Predicted Seller')
            ax[0, 0].set_xlim(left=0)
            ax[0, 0].set_ylim(bottom=0)

            # Recency x Monetary
            sb.scatterplot(data=results_df, x='recency', y='monetary', ax=ax[0, 1])
            ax[0, 1].set_title('Recency x Monetary for Predicted Seller')
            ax[0, 1].set_xlim(left=0)
            ax[0, 1].set_ylim(bottom=0)

            # Recency x Average Rating
            sb.scatterplot(data=results_df, x='recency', y='average_rating', ax=ax[1, 0])
            ax[1, 0].set_title('Recency x Average Rating for Predicted Seller')
            ax[1, 0].set_xlim(left=0)
            ax[1, 0].set_ylim(bottom=0)

            # Frequency x Monetary
            sb.scatterplot(data=results_df, x='frequency', y='monetary', ax=ax[1, 1])
            ax[1, 1].set_title('Frequency x Monetary for Predicted Seller')
            ax[1, 1].set_xlim(left=0)
            ax[1, 1].set_ylim(bottom=0)

            # Frequency x Average Rating
            sb.scatterplot(data=results_df, x='frequency', y='average_rating', ax=ax[2, 0])
            ax[2, 0].set_title('Frequency x Average Rating for Predicted Seller')
            ax[2, 0].set_xlim(left=0)
            ax[2, 0].set_ylim(bottom=0)

            # Monetary x Average Rating
            sb.scatterplot(data=results_df, x='monetary', y='average_rating', ax=ax[2, 1])
            ax[2, 1].set_title('Monetary x Average Rating for Predicted Seller')
            ax[2, 1].set_xlim(left=0)
            ax[2, 1].set_ylim(bottom=0)

            # Show the plots
            plt.tight_layout()
            st.pyplot(fig)

        if len(input_df) == 1:
            st.markdown("### Detailed Seller Information")
            st.write(f"**Recency**: {recency}")
            st.write(f"**Frequency**: {frequency}")
            st.write(f"**Monetary**: {monetary}")
            st.write(f"**Average Rating**: {average_rating}")

        st.markdown("### Seller Data and Cluster Prediction")
        st.write(results_df)

        # ----------------------------
        # Interpretasi Cluster
        # ----------------------------
        st.markdown("### 🧠 Cluster Interpretation")

        unique_clusters = sorted(results_df['Cluster'].unique())

        for clust in unique_clusters:
            st.write(f"**{cluster_names.get(clust, 'Unknown')}**")
            st.markdown("**Recommended Treatment:**")
            st.markdown(treatments.get(clust, "-"))
            st.markdown("---")

    else:
        st.warning("No prediction results available yet. Please run a prediction first.")