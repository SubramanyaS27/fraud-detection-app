import streamlit as st
import joblib

model = joblib.load('fraud_model.pkl')
fraud_sample = joblib.load('fraud_sample.pkl')
non_fraud_sample = joblib.load('non_fraud_sample.pkl')
random_pool = joblib.load('random_pool.pkl')

st.set_page_config(page_title="Fraud Detection System", layout="centered")
st.title("💳 Credit Card Fraud Detection")
st.caption("RandomForest | AUC 97.3% | Recall 84% | Precision 85%")
st.divider()

col1, col2, col3 = st.columns(3)
if 'sample' not in st.session_state:
    st.session_state.sample = non_fraud_sample

with col1:
    if st.button("Test Non-Fraud", use_container_width=True):
        st.session_state.sample = non_fraud_sample
with col2:
    if st.button("Test Fraud", use_container_width=True):
        st.session_state.sample = fraud_sample
with col3:
    if st.button("Test Random Txn", use_container_width=True):
        st.session_state.sample = random_pool.sample(1).iloc[0]

sample = st.session_state.sample
prob = model.predict_proba([sample.values])[0][1]
pred = model.predict([sample.values])[0]

st.divider()
c1, c2 = st.columns(2)
c1.metric("Prediction", "FRAUD ❌" if pred==1 else "SAFE ✅")
c2.metric("Fraud Probability", f"{prob*100:.1f}%")

st.progress(prob)

st.subheader("Transaction Details")
st.dataframe(sample.to_frame().T, use_container_width=True)

if pred == 1:
    st.error(f"Action: Transaction BLOCKED and flagged for review.")
else:
    st.success(f"Action: Transaction APPROVED.")

st.info(f"Amount: ${sample['Amount']:.2f} | Time: {sample['Time']:.0f}s")