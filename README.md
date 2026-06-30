# 📊 Customer Churn Prediction using Machine Learning

## 📖 Deskripsi

Project ini merupakan implementasi Machine Learning untuk memprediksi **Customer Churn** menggunakan dataset **Sales & Marketing Customer Dataset**.

Penelitian ini membandingkan tiga algoritma klasifikasi:

- Logistic Regression
- Random Forest
- Voting Classifier

Model dibangun melalui tiga tahapan, yaitu:

- Direct Modeling
- Modeling dengan Preprocessing
- Hyperparameter Tuning

Berdasarkan hasil evaluasi, **Random Forest** memberikan performa terbaik sehingga dipilih sebagai model deployment pada aplikasi Streamlit.

---

## 📂 Dataset

Dataset yang digunakan adalah **Sales & Marketing Customer Dataset** dengan karakteristik:

- Jumlah data : **15.000**
- Jumlah fitur : **30**
- Target : **Customer Churn**
  - 0 = Tidak Churn
  - 1 = Churn

---

## ⚙️ Tahapan Project

### 1. Exploratory Data Analysis (EDA)

Melakukan analisis awal dataset meliputi:

- Menampilkan informasi dataset
- Statistik deskriptif
- Analisis Missing Value
- Analisis Data Duplikat
- Analisis Outlier
- Distribusi Target
- Heatmap Korelasi

---

### 2. Direct Modeling

Tahapan baseline model tanpa preprocessing lanjutan.

Model yang digunakan:

- Logistic Regression
- Random Forest
- Voting Classifier

Evaluasi menggunakan:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

### 3. Modeling dengan Preprocessing

Tahapan preprocessing meliputi:

- Penghapusan fitur yang tidak relevan
- Penanganan Missing Value
- Feature Selection
- StandardScaler
- SMOTE
- Pipeline Preprocessing

Model yang digunakan:

- Logistic Regression
- Random Forest
- Voting Classifier

---

### 4. Hyperparameter Tuning

Optimasi model menggunakan **RandomizedSearchCV**.

Model yang dioptimasi:

- Logistic Regression
- Random Forest
- Voting Classifier

---

## 📈 Hasil Model Terbaik

Model terbaik diperoleh menggunakan:

**Random Forest + Preprocessing + SMOTE + Hyperparameter Tuning**

Hasil evaluasi:

| Metric | Nilai |
|---------|-------:|
| Accuracy | **85.60%** |
| Precision | **51.59%** |
| Recall | **98.48%** |
| F1-Score | **67.71%** |

---

## 🚀 Deployment

Model terbaik telah diimplementasikan menggunakan **Streamlit Community Cloud**.

🔗 **Link Aplikasi:*https://meganbr-uas-bengkodds.streamlit.app/*

https://meganbr-uas-bengkodds.streamlit.app/

Pengguna dapat:

- Menginput data pelanggan
- Melakukan prediksi Customer Churn
- Melihat probabilitas Churn dan Tidak Churn
- Menampilkan hasil prediksi secara interaktif

---

## Colab

**Link Colab: *https://colab.research.google.com/drive/1MWk7KM9m7z_O-TCGQf0o8OLzIxzASQjY?usp=sharing*
## 📁 Repository

GitHub Repository:

https://github.com/meganfbr/UAS_BENGKOD

---

## 🛠️ Library yang Digunakan

- Python
- Pandas
- NumPy
- Scikit-Learn
- Imbalanced-Learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

---

## 👩‍💻 Author

**Megan Febriana Putri Johana**

NIM: **A11.2023.15039**

Universitas Dian Nuswantoro (UDINUS)

Mata Kuliah: **Bengkel Coding**
