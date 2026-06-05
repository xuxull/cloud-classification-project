import streamlit as st
from PIL import Image

st.set_page_config(page_title="Cloud Classifier", page_icon="☁️")

st.title("☁️ Cloud Classification App")
st.write("Upload an image of the sky and we will predict the cloud type.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.subheader("Prediction")
    st.write("Model not connected yet 🤖")

    st.subheader("Confidence")
    st.write("0%")