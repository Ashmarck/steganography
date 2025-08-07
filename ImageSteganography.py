import asyncio
import cv2 as cv
import Conversion
import numpy as np
import streamlit as st

def encode(img, msg):
    
    lang_ind, data = asyncio.run(Conversion.encode_translate(msg))
    
    a = [ord(i) for i in data]
    l = len(data)
    
    for i in range(len(img[0])):
        img[0][i][2] = 178
        
    img[0][0][2] = lang_ind
    img[0][1][2] = l
    
    if l > 250:
        print()
    else:
            
        for i in range(2,l+2):
            img[0][i][2] = a[i-2]
        
    success, encoded_image_buffer = cv.imencode(".png", img)

    if not success:
        st.error("Failed to encode image to PNG format.")
        return None
    
    return encoded_image_buffer.tobytes()

def decode(img, lang):
    
    asciis = []
    # lang_ind = img[0][0][2]
    l = img[0][1][2]
    
    for i in range(2,l+2):

        if img[0][i][2] in range(31,127):
            asciis.append(img[0][i][2])

    chars = [chr(i) for i in asciis]
    text = ''.join(chars)
    
    data = asyncio.run(Conversion.decode_translate(text, lang))
    
    return data
     
