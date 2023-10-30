import streamlit as st

st.set_page_config(
    page_title="CCTV monitor",
    page_icon="🎥",
)
st.title("CCTV Monitor")

col1, col2 = st.columns(2)
with col1:
   st.text_input("Enter student ID")
   st.button("Scan CCTV Footage", type="primary")

