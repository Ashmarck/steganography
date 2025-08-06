import cv2 as cv
import numpy as np
import streamlit as st

def encode(img, msg):

    a = [ord(i) for i in msg]
    for i in range(len(img[0])):
        img[0][i][2] = 178
        
    if len(msg) > 300:
        print()
    else:
            
        for i in range(len(a)):
            img[0][i][2] = a[i]
        
    success, encoded_image_buffer = cv.imencode(".png", img)

    if not success:
        st.error("Failed to encode image to PNG format.")
        return None
    
    return encoded_image_buffer.tobytes()

def decode(img):
    asciis = []

    for i in range(len(img[0])):
        if img[0][i][2] in range(65,91) or img[0][i][2] in range(97,123) or img[0][i][2]==32 or img[0][i][2] in range(48,58):
            asciis.append(img[0][i][2])

    chars = [chr(i) for i in asciis]
    final_text = ''.join(chars)

    return final_text
     
# img = cv.imread("steganography/eagle.png")
# t = input("Enter your message: ")

# print(encode(img, t))
# print(decode(img))