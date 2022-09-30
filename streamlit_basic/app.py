
#importing streamlit library
import streamlit as st
from PIL import Image


#opening the image
image = Image.open('Raspberry-GPIO.jpg')
#displaying the image on streamlit app
st.image(image, caption='Enter any caption here')

import pandas as pd

st.write("My first DataFrame")
st.write(
pd.DataFrame({
    'A': [1, 5, 9, 7],
    'B': [3, 2, 4, 8]
  })
)

import streamlit as st
import numpy as np
import pandas as pd
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

import cv2
import streamlit as st
import numpy as np
from PIL import Image


def brighten_image(image, amount):
    img_bright = cv2.convertScaleAbs(image, beta=amount)
    return img_bright


def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (11, 11), amount)
    return blur_img


def enhance_details(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr


def main_loop():
    st.title("OpenCV Demo App")
    st.subheader("This app allows you to play with Image filters!")
    st.text("We use OpenCV and Streamlit for this demo")

    blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5)
    brightness_amount = st.sidebar.slider("Brightness", min_value=-50, max_value=50, value=0)
    apply_enhancement_filter = st.sidebar.checkbox('Enhance Details')

    image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
    if not image_file:
        return None

    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    processed_image = blur_image(original_image, blur_rate)
    processed_image = brighten_image(processed_image, brightness_amount)

    if apply_enhancement_filter:
        processed_image = enhance_details(processed_image)

    st.text("Original Image vs Processed Image")
    st.image([original_image, processed_image])


if __name__ == '__main__':
    main_loop()
#การติดตั้ง Streamlit
#pip install streamlit
#https://streamlit.io/gallery
#อาจมีปัญหากับเวอร์ชัน Python ของคุณ ดังนั้นอย่าลืมติดตั้ง Streamlit ลงใน Python 3.6+
#การนำเข้า Streamlit
#import streamlit
#Streamlit เป็น Python Library อีกตัวที่สุดยอดมาก เหมาะกับการทำ Visualization ถ้าให้ลุงอธิบายง่ายๆว่าเจ้า Streamlit คืออะไร ...อธิบายง่ายๆคือประมาณ POWER BI ของ Python เลยทีเดียว (แต่ความสามารถคงไม่เยอะขนาด BI)
#ลักษณะการรันจะเป็นคล้ายๆ Web Framework อย่าง Flask พิมพ์โค้ดใส่ไฟล์ python แล้วสั่งรันผ่าน cmd ด้วยคำสั่ง streamlit run basic.py 