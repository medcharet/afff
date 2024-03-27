import streamlit as st
from streamlit_option_menu import option_menu
#from streamlit.components.v1 import html
#from st_on_hover_tabs import on_hover_tabs
import requests
#from streamlit_lottie import st_lottie
from PIL import Image
#import streamlit_analytics
import base64
#from streamlit_extras.mention import mention
#from streamlit_extras.app_logo import add_logo
import sqlite3
#from bs4 import BeautifulSoup
#from streamlit_extras.echo_expander import echo_expander

#test

# Set page title
st.set_page_config(page_title="CHARET Mohamed", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")
# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 CHARET Mohamed';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href
img_utown = Image.open("utown.PNG")


st.markdown("*Copyright © 2024 CHARET Mohamed*")

