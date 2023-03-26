import streamlit as st
import pandas as pd
import numpy as np
import openai
import webbrowser

from time import sleep
from PIL import Image

openai.api_key = "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"
# 페이지 기본설정
st.set_page_config(
    page_icon="",
    page_title="나의 이상형 이미지 배포하기",
    layout="wide",
)

#페이지 헤더, 서브헤더 제목설정
st.header("나의 이상형 이미지 찾기")
st.subheader("내가 생각하는 나의 이상형")

prompt_input = st.text_input("원하는 이성은? ")
st.title(prompt_input)

response = openai.Image.create(
  prompt=prompt_input,
  n=2,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print("==================================")
print(response["data"][0]["url"])
st.image(image_url, width=400,)
print("==================================")
