import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Prediksi Customer Churn",
    page_icon="📊",
    layout="wide"
)

model = joblib.load("best_rf_sales_marketing.pkl")

st.title("📊 Prediksi Customer Churn")
st.write("Aplikasi ini digunakan untuk memprediksi apakah pelanggan berpotensi churn atau tidak.")

st.sidebar.header("Input Data Pelanggan")

gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=30)

country = st.sidebar.selectbox("Country", ["USA", "UK", "Canada", "Australia", "Germany"])
city = st.sidebar.selectbox("City", ["New York", "London", "Toronto", "Sydney", "Berlin", "Chicago", "Manchester"])

acquisition_channel = st.sidebar.selectbox(
    "Acquisition Channel",
    ["Organic", "Ads", "Email", "Referral", "Social Media"]
)

device_type = st.sidebar.selectbox("Device Type", ["Mobile", "Desktop", "Tablet"])
subscription_type = st.sidebar.selectbox("Subscription Type", ["Monthly", "Yearly", "Free"])

is_premium_user = st.sidebar.selectbox("Premium User", [0, 1])
total_visits = st.sidebar.number_input("Total Visits", min_value=0, value=10)
avg_session_time = st.sidebar.number_input("Average Session Time", min_value=0.0, value=20.0)
pages_per_session = st.sidebar.number_input("Pages per Session", min_value=0.0, value=3.0)

email_open_rate = st.sidebar.slider("Email Open Rate", 0.0, 1.0, 0.5)
email_click_rate = st.sidebar.slider("Email Click Rate", 0.0, 1.0, 0.2)

total_spent = st.sidebar.number_input("Total Spent", min_value=0.0, value=500.0)
avg_order_value = st.sidebar.number_input("Average Order Value", min_value=0.0, value=100.0)

discount_used = st.sidebar.selectbox("Discount Used", [0, 1])
coupon_code = st.sidebar.selectbox("Coupon Code", ["Tidak Ada", "WELCOME10", "SAVE20", "DISCOUNT15"])

support_tickets = st.sidebar.number_input("Support Tickets", min_value=0, value=1)
refund_requested = st.sidebar.selectbox("Refund Requested", [0, 1])
delivery_delay_days = st.sidebar.number_input("Delivery Delay Days", min_value=0, value=0)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    ["Credit Card", "PayPal", "Bank Transfer", "Debit Card"]
)

satisfaction_score = st.sidebar.slider("Satisfaction Score", 1.0, 5.0, 3.5)
nps_score = st.sidebar.slider("NPS Score", -10, 10, 0)

marketing_spend_per_user = st.sidebar.number_input("Marketing Spend per User", min_value=0.0, value=50.0)
lifetime_value = st.sidebar.number_input("Lifetime Value", min_value=0.0, value=1000.0)
last_3_month_purchase_freq = st.sidebar.number_input("Last 3 Month Purchase Frequency", min_value=0, value=2)

if coupon_code == "Tidak Ada":
    coupon_code = np.nan

input_data = pd.DataFrame({
    "gender": [gender],
    "age": [age],
    "country": [country],
    "city": [city],
    "acquisition_channel": [acquisition_channel],
    "device_type": [device_type],
    "subscription_type": [subscription_type],
    "is_premium_user": [is_premium_user],
    "total_visits": [total_visits],
    "avg_session_time": [avg_session_time],
    "pages_per_session": [pages_per_session],
    "email_open_rate": [email_open_rate],
    "email_click_rate": [email_click_rate],
    "total_spent": [total_spent],
    "avg_order_value": [avg_order_value],
    "discount_used": [discount_used],
    "coupon_code": [coupon_code],
    "support_tickets": [support_tickets],
    "refund_requested": [refund_requested],
    "delivery_delay_days": [delivery_delay_days],
    "payment_method": [payment_method],
    "satisfaction_score": [satisfaction_score],
    "nps_score": [nps_score],
    "marketing_spend_per_user": [marketing_spend_per_user],
    "lifetime_value": [lifetime_value],
    "last_3_month_purchase_freq": [last_3_month_purchase_freq]
})

st.subheader("Data Input Pelanggan")
st.dataframe(input_data)

if st.button("Prediksi Churn"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Pelanggan diprediksi CHURN")
        st.write("Pelanggan berpotensi berhenti menggunakan layanan.")
    else:
        st.success("✅ Pelanggan diprediksi TIDAK CHURN")
        st.write("Pelanggan diprediksi tetap menggunakan layanan.")