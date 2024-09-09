import streamlit as st
from moviepy.editor import *

st.set_page_config(
    page_title="Gifify - MP4 to GIF Converter",
    page_icon="icon.png",
    menu_items={
        "About":"Gifify is your go-to tool for converting MP4 videos into high-quality GIFs in just a few clicks. Upload your video, customize your settings, and get your GIF instantly. Perfect for creating engaging social media content, memes, and more!"
    }   
)

st.write("<h2 style='color:#F6464C;'>Turn Videos into Stunning GIFs Instantly.</h2>",unsafe_allow_html=True)

file=st.file_uploader("Upload Video",type=["mp4"])

if file:
    with open("video.mp4","wb") as vid:
        vid.write(file.getbuffer())
    video=VideoFileClip("video.mp4")
    start=st.slider("Start Time (seconds)",min_value=0,max_value=int(video.duration),value=1)
    end=st.slider("End Time (seconds)",min_value=0,max_value=int(video.duration),value=3)
    frame=st.select_slider("Frame Rate (FPS)",options=[5,7,10,12,16,20,25,33],value=10)
    if(end>start):
        video=video.subclip(start,end)
        btn=st.button("Convert to GIF!")
        if btn:
            with st.spinner("This may take few seconds..."):
                video.write_gif("gifify.gif",fps=frame)
                st.image("gifify.gif")
                with open("gifify.gif","rb") as gif:
                    st.download_button("Download",gif.read(),"gifify.gif")
    else:
        st.error("Enter a valid video duration.")
