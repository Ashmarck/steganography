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
            
            enc_button = st.button("Encode Message", type="primary", use_container_width=True)

        if enc_button:
            if img_take is not None and text:
                img_bytes = img_take.getvalue()
                np_arr = np.frombuffer(img_bytes, np.uint8)
                img_array = cv.imdecode(np_arr, cv.IMREAD_COLOR)
                
                encoded_image_array = ImageSteganography.encode(img_array, text)
                st.success("Message encoded successfully!")
                
                st.download_button(
                    label="Download Encoded Image",
                    data=encoded_image_array,
                    file_name="encoded_image.png",
                    mime="image/png",
                    use_container_width=True
                )
            else:
                st.warning("Please upload an image and enter a message before encoding.")

    elif choose == "Decode":
        st.header("Decode a Message from an Image")

        img_to_decode = st.file_uploader("Upload your encoded image:", type=["jpg", "jpeg", "png"])

        if img_to_decode is not None:
            st.image(img_to_decode, caption="Encoded Image", use_container_width=True)
            choice = st.selectbox("Select language to decode your message:", ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'])
            dec_button = st.button("Decode Image", type="primary", use_container_width=True)

            if dec_button:
                img_bytes = img_to_decode.getvalue()
                np_arr = np.frombuffer(img_bytes, np.uint8)
                img_array = cv.imdecode(np_arr, cv.IMREAD_COLOR)
                
                decoded_message = ImageSteganography.decode(img_array, choice)
                
                st.success("Message decoded successfully!")
                st.text_area("Decoded Message:", value=decoded_message, height=150, disabled=True)

if options == "Audio":
    st.title("Audio Steganography")
    st.info("This feature is coming soon!")

if options == "Video":
    st.title("Video Steganography")
    st.info("This feature is coming soon!")
