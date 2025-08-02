# src/ui/app.py (Streamlit)
import streamlit as st
import requests

st.title("Verificador de Senha Segura")

password = st.text_input("Digite sua senha:", type="password")

if st.button("Verificar"):
    if password:
        response = requests.get("http://localhost:8000/check-password", params={"password": password})
        result = response.json()
        if result["secure"]:
            st.success("✅ Senha segura!")
        else:
            st.error("❌ Senha fraca.")
    else:
        st.warning("Digite uma senha.")
