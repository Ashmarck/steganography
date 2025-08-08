import asyncio
import cv2 as cv
import Conversion
import numpy as np
import EncDec as ed
import streamlit as st

def encode(img, msg, code=0):
   
    l = len(msg)
    if l > 250:
        raise ValueError("Message too long. Maximum 250 characters.")

    img[0][0][2] = l

    if code == 1: 
        a = [ord(i) for i in msg]
        key, enc_data, img_with_key = ed.encrypt(a, img.copy()) 
        
        for i in range(1, l + 1):
            img_with_key[0][i][2] = enc_data[i-1]
        
        image_to_save = img_with_key

    else:
        key = None 
        a = [ord(i) for i in msg]
        img_plaintext = img.copy()
        for i in range(1, l + 1):
            img_plaintext[0][i][2] = a[i-1]
        image_to_save = img_plaintext

    success, encoded_image_buffer = cv.imencode(".png", image_to_save)
    if not success:
        raise ConnectionError("Failed to encode image to PNG format.")
    
    return key, encoded_image_buffer.tobytes()

def decode(img, key=None, code=0):
   
    if code == 1: 
        if key is None or key == "":
            return "Error: A key is required for decryption."
        return ed.decrypt(img, key)
        
    else: 
        l = img[0][0][2]
        asciis = []
        for i in range(1,l+1):
            asciis.append(img[0][i][2])
        
        chars = [chr(i) for i in asciis]
        text = ''.join(chars)
        return text