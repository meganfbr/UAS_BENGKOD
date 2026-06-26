import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediksi Customer Churn",
    page_icon="📊",
    layout="wide"
)

model = joblib.load("best1_rf_sales_marketing.pkl")

st.title("📊 Prediksi Customer Churn")
st.write(
    "Aplikasi ini digunakan untuk memprediksi kemungkinan pelanggan melakukan churn "
    "berdasarkan 10 fitur perilaku pelanggan."
)

st.sidebar.header("Input Data Pelanggan")

total_spent = st.sidebar.number_input(
    "Total Spent",
    min_value=0.0,
    value=500.0
)

satisfaction_score = st.sidebar.slider(
    "Satisfaction Score",
    min_value=1.0,
    max_value=5.0,
    value=3.5
)

support_tickets = st.sidebar.number_input(
    "Support Tickets",
    min_value=0,
    value=1
)

last_3_month_purchase_freq = st.sidebar.number_input(
    "Last 3 Month Purchase Frequency",
    min_value=0,
    value=2
)

lifetime_value = st.sidebar.number_input(
    "Lifetime Value",
    min_value=0.0,
    value=1000.0
)

avg_session_time = st.sidebar.number_input(
    "Average Session Time",
    min_value=0.0,
    value=20.0
)

pages_per_session = st.sidebar.number_input(
    "Pages per Session",
    min_value=0.0,
    value=3.0
)

total_visits = st.sidebar.number_input(
    "Total Visits",
    min_value=0,
    value=10
)

email_open_rate = st.sidebar.slider(
    "Email Open Rate",
    min_value=0.0,
    max_value=1.0,
    value=0.5
)

email_click_rate = st.sidebar.slider(
    "Email Click Rate",
    min_value=0.0,
    max_value=1.0,
    value=0.2
)

input_data = pd.DataFrame({
    "total_spent": [total_spent],
    "satisfaction_score": [satisfaction_score],
    "support_tickets": [support_tickets],
    "last_3_month_purchase_freq": [last_3_month_purchase_freq],
    "lifetime_value": [lifetime_value],
    "avg_session_time": [avg_session_time],
    "pages_per_session": [pages_per_session],
    "total_visits": [total_visits],
    "email_open_rate": [email_open_rate],
    "email_click_rate": [email_click_rate]
})

st.subheader("Data Input Pelanggan")
st.dataframe(input_data, use_container_width=True)

if st.button("Prediksi Churn"):
    proba = model.predict_proba(input_data)[0]

    proba_tidak_churn = proba[0]
    proba_churn = proba[1]

    prediction = model.predict(input_data)[0]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Probabilitas Tidak Churn",
            value=f"{proba_tidak_churn:.2%}"
        )

    with col2:
        st.metric(
            label="Probabilitas Churn",
            value=f"{proba_churn:.2%}"
        )

    st.subheader("Hasil Prediksi")

    if prediction == 1:
        st.error("⚠️ Pelanggan diprediksi CHURN")
        st.write("Pelanggan berpotensi berhenti menggunakan layanan.")
    else:
        st.success("✅ Pelanggan diprediksi TIDAK CHURN")
        st.write("Pelanggan diprediksi tetap menggunakan layanan.")

    st.info(
        "Perhitungan probabilitas diperoleh dari fungsi `predict_proba()` pada model Random Forest. "
        "Model menghitung peluang pelanggan masuk ke kelas 0 (Tidak Churn) dan kelas 1 (Churn) "
        "berdasarkan pola data pelatihan. Kelas dengan probabilitas lebih besar digunakan sebagai hasil prediksi akhir."
    )