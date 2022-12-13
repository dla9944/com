import streamlit as st
# from streamlit_image_comparison import image_comparison
# import cv2


st.set_page_config("1980's P vs 2020's P")


st.image(
    "https://rlyfaazj0.toastcdn.net/20221019/145434.523656000/106827397_1.png", #카메라
    width=240,
)

st.header("1980's Fashion vs 2020's Fashion")

st.write("")
"This web is a site where you can know the fashion from the past to the present.!"
st.write("")

st.markdown("### 1980's Fashion")
col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header("1980's winter")
   st.image("https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg")

with col2:
   st.header("A dog")
   st.image("https://cdn.pixabay.com/photo/2018/03/27/17/25/cat-3266673_1280.jpg")

with col3:
    st.header("1980's winter")
    st.image("https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg")

with col4:
    st.header("1980's winter")
    st.image("https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg")


st.markdown("### 2022's Fashion")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/deep_field_700.jpg",
    img2="https://www.webbcompare.com/img/webb/deep_field_700.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Carina Nebula")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/carina_2800.png",
    img2="https://www.webbcompare.com/img/webb/carina_2800.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Stephan's Quintet")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/stephans_quintet_2800.jpg",
    img2="https://www.webbcompare.com/img/webb/stephans_quintet_2800.jpg",
    label1="Hubble",
    label2="Webb",
)


