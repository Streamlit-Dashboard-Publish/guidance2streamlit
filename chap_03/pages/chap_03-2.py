#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
from PIL import Image
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(current_dir, "data/example.jpg")


st.title('3.2 이미지, 비디오, 오디오 출력')


st.divider()
# st.image 예시 1
st.markdown('#### *st.image 예시 1*')
img_path = os.path.join(current_dir, "data/example.jpg")
image = Image.open(img_path)

st.image(image, caption="image1")
# st.image 예시 2
st.markdown('#### *st.image 예시 2*')

image = Image.open("./data/example.jpg")

st.image(image, caption="width=100", width=100)
# st.image 예시 3
st.markdown('#### *st.image 예시 3*')
image = Image.open("./data/example.jpg")

st.image(image, caption="example", width=200, use_column_width="auto")
st.divider()
# st.audio 예시 1
st.markdown('#### *st.audio 예시 1*')
aud_path = os.path.join(current_dir, "data/example.mp3")
audio_file = open(aud_path, "rb")

audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mp3", start_time=5)


# st.audio 예시 2
st.markdown('#### *st.audio 예시 2*')
sample_rate = 44100  # 44100 초당 샘플수
seconds = 2  # 2초 동안 음이 지속됩니다.
frequency_la = 440  # 재생할 음파를 나타냅니다.

t = np.linspace(0, seconds, seconds * sample_rate, False) 
note_la = np.sin(frequency_la * t * 2 * np.pi) #440 헤르쯔의 사인파를 만듭니다.

st.audio(note_la, sample_rate=sample_rate)

st.divider()
# st.video 예시 1
st.markdown('#### *st.video 예시 1*')
vid_path = os.path.join(current_dir, "data/example.mp4")
# 동영상 파일을 로컬 경로에서 재생하는 예시
video_file = open("./data/example.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)
# st.video 예시 2
st.markdown('#### *st.video 예시 2*')
vid_path = os.path.join(current_dir, "data/example1.mp4")
video_file = open(vid_path, "rb")
video_bytes = video_file.read()

st.video(video_bytes)



