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
    dst = cv2.fastNlMeansDenoisingColored(cv2.imread("temp.png"), None, 5, 5, 7, 17)
    return dst

def get_image_download_link(img):
	buffered = BytesIO()
	img.save(buffered, format="PNG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/png;base64,{img_str}" download="{"output.png"}">Download result</a>'
	return href

st.title("FSRCNN Anime Image 2X Scale Up")
model = keras.models.load_model('FSRCNN_Waifu.h5')
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    image = np.array(image)
    image = image[:, :, ::-1].copy()
    st.image(image, caption='Uploaded Img.', use_column_width=True, channels='BGR')
    st.write("")
    st.write("Upscaling...")
    img = upscale(image, model)
    st.image(img, caption='Scaled up Img.', use_column_width=True, channels='BGR')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    st.markdown(get_image_download_link(img), unsafe_allow_html=True)
