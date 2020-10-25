import streamlit as st
import keras
from PIL import Image, ImageOps
import numpy as np
import cv2
from io import BytesIO
import base64

def upscale(img, model):
    h, l = img.shape[0], img.shape[1]
    buff = np.asarray([img])
    raw = model.predict(buff)[0]
    cv2.imwrite("temp.png", raw)
    dst = cv2.fastNlMeansDenoisingColored(cv2.imread("temp.png"), None, 10, 10, 7, 21)
    return dst

def get_image_download_link(img, id):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="{str(id)+".png"}">{"Download "+str(id)+".png"}</a>'
    return href

st.title("FSRCNN Anime Image 2X Scale Up")
col1, col2 = st.beta_columns(2)
model = keras.models.load_model('FSRCNN_Waifu.h5')
uploaded_file = st.file_uploader("Choose images", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    inputs = []
    for img in uploaded_file:
        image = Image.open(img).convert('RGB')
        image = np.array(image)
        image = image[:, :, ::-1].copy()
        col1.image(image, caption='Uploaded Img.', use_column_width=True, channels='BGR')
        inputs.append(image)
    for i in range(len(inputs)):
        img = upscale(inputs[i], model)
        col2.image(img, caption='Scaled up Img.', use_column_width=True, channels='BGR')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        st.markdown(get_image_download_link(img, i+1), unsafe_allow_html=True)
