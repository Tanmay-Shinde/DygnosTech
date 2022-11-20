# import numpy as np
import streamlit as st
# from PIL import Image
# import utils as utl
from pages import patient

# st.set_page_config(layout="wide", page_title='Navbar sample')
# st.set_option('deprecation.showPyplotGlobalUse', False)
# utl.inject_custom_css()
# utl.navbar_component()
#
#
# def navigation():
#     route = utl.get_current_route()
#     if route == "home":
#         home.load_view()
#     elif route == "about":
#         about.load_view()
#     elif route == "analysis":
#         analysis.load_view()
#     elif route == "options":
#         options.load_view()
#     elif route == "configuration":
#         configuration.load_view()
#     elif route == None:
#         home.load_view()
#
#
# navigation()


u = "https://storage.googleapis.com/rishit-dagli.appspot.com/My_project-1_1.png"
page_title = "Home Screen"

# Set page title and favicon.
st.set_page_config(page_title=page_title, page_icon=u)


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.discordapp.com/attachments/1043363043947581533/1043480856150409257/marcel-strauss-iCR53oVMqcs-unsplash.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True,
    )


add_bg_from_url()

u = "https://storage.googleapis.com/rishit-dagli.appspot.com/My_project-1_1.png"
st.image(u, width=150)

st.markdown(
    f'<h1 style="color:#000000;font-size:35px;">{"Home Screen"}</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<h1 style="color:#000000;font-size:15px;">{"Spelled as We Detect"}</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<h1 style="color:#000000;font-size:15px;">{"Note: The word weed here refers to unwanted plant growth."}</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<h1 style="color:#000000;font-size:24px;">{"Farmers waste hours scouring fields to find weeds, our model helps them drastically reduce this time. Weed Detech helps farmer detect the position of weed on a field with a single photo click. Our model is trained on over 15000 images and achieves plausible performance."}</h1>',
    unsafe_allow_html=True,
)

# st.button('Try it out!!')
