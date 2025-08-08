import cv2 as cv
import numpy as np
import streamlit as st
import ImageSteganography 
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Steganography App", layout="wide")

with st.sidebar:
    options = option_menu(
        "Steganography", 
        ["Image", "Audio", "Video"], 
        icons=["card-image", "volume-up-fill", "camera-reels"], 
        menu_icon="cast",
        default_index=0
    )

if options == "Image":
    st.title("Image Steganography: Hide Your Secrets")
    st.markdown("---")

    choose = st.selectbox("Choose an Operation", ["Encode", "Decode"])
    
    if choose == "Encode":
        st.header("Encode a Message into an Image")
        col1, col2 = st.columns(2)

        with col1:
            img_take = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
            if img_take is not None:
                st.image(img_take, caption="Image to encode", use_container_width=True)

        with col2:
            text = st.text_area("Enter your secret message...", max_chars=250, height=150)
            enc = st.checkbox("Do you want to encrypt your message?")
            enc_button = st.button("Encode Message", type="primary", use_container_width=True)

            if enc_button:
                if img_take is not None and text:
                    img_bytes = img_take.getvalue()
                    np_arr = np.frombuffer(img_bytes, np.uint8)
                    img_array = cv.imdecode(np_arr, cv.IMREAD_COLOR)
                    try:
                        if enc:
                            key, encoded_data = ImageSteganography.encode(img_array, text, code=1)
                        else:
                            key, encoded_data = ImageSteganography.encode(img_array, text, code=0)
                        
                        st.success("Message encoded successfully!")
                        if key:
                            st.info(f"**Your Encryption Key: `{key}`**")
                        
                        st.download_button(
                            label="Download Encoded Image",
                            data=encoded_data,
                            file_name="encoded_image.png",
                            mime="image/png",
                            use_container_width=True
                        )
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                else:
                    st.warning("Please upload an image and enter a message before encoding.")

    elif choose == "Decode":
        st.header("Decode a Message from an Image")
        col1, col2 = st.columns(2)
        with col1:
            img_to_decode = st.file_uploader("Upload your encoded image:", type=["png"])
            if img_to_decode is not None:
                st.image(img_to_decode, caption="Encoded Image", use_container_width=True)
            
        with col2:
            dec = st.checkbox("Is your message encrypted?")
            user_key = ""
            if dec:
                user_key = st.text_input("Enter your encryption key:")
            
            dec_button = st.button("Decode Image", type="primary", use_container_width=True)
            
            if dec_button:
                if img_to_decode is not None:
                    img_bytes = img_to_decode.getvalue()
                    np_arr = np.frombuffer(img_bytes, np.uint8)
                    img_array = cv.imdecode(np_arr, cv.IMREAD_COLOR)
                    
                    try:
                        if dec:
                            decoded_message = ImageSteganography.decode(img_array, key=user_key, code=1)
                        else:
                            decoded_message = ImageSteganography.decode(img_array, code=0)
                    
                        st.success("Decoding process finished.")
                        st.text_area("Decoded Message:", value=decoded_message, height=150, disabled=True)
                    except Exception as e:
                        st.error(f"An error occurred during decoding: {e}")
                else:
                    st.warning("Please upload an image to decode.")

if options == "Audio" or options == "Video":
    st.title(f"{options} Steganography")
    st.info("This feature is coming soon!")