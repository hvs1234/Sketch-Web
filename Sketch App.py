import streamlit as slt
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import numpy as np
import cv2

hide = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility :hidden;}
"""
slt.set_page_config(page_title="Pencil Sketcher",page_icon=":printer:",layout="wide")
slt.markdown(hide,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        slt.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

def load(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def dodgeV2(x,y):
    return cv2.divide(x, 255-y, scale=256)

def pencilsketch(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21,21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray,img_smoothing)
    return(final_img)

lottie_coding1 = load("https://assets9.lottiefiles.com/packages/lf20_xmkgn4jj.json")
lottie_coding2 = load("https://assets8.lottiefiles.com/packages/lf20_1lgyzo9c.json")

with slt.container():
    left,right = slt.columns(2)
    with left:
        slt.header("Photo To Sketch Converter :pencil:")
        slt.text("This web app converts your photo to pencil sketch.")
        slt.text("It is basically a sketch of that image.")
        slt.write("---")
    with right:
        st_lottie(lottie_coding1,height=150,key="Converter")

with slt.container():
    file_name = slt.sidebar.file_uploader("Upload your files",type=["jpg","jpeg","png","webp"])
    slt.sidebar.write("---")
slt.text("To upload the files, go to the left sidebar function ...")
if file_name is None:
    slt.write("You haven't upload any files here ...")
else:
    img = Image.open(file_name)
    final_sketch = pencilsketch(np.array(img))
    slt.write("**Input Photos**")
    slt.image(img)
    slt.write("**Output Pencil Sketch**")
    slt.image(final_sketch)
slt.write("---")
with slt.container():
    slt.write('Get Touch With Me! :thought_balloon:'); slt.write("##")
    contact_form = """
    <form action="https://formsubmit.co/3469harshsharma@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column,right_column = slt.columns(2)
    with left_column:
        slt.markdown(contact_form,unsafe_allow_html=True)
        local_css("style/style.css")
    with right_column:
        st_lottie(lottie_coding2,height=250,key="Join Us")
slt.write("---")
slt.write("If you guys have any query, so send me your perspective above. Thanks !!!")