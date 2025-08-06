import streamlit as st
import cv2
import numpy as np
import requests # You'll need to install this: pip install requests
import base64
import time
import ImageSteganography as obj

# --- PAGE CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Image Steganography", page_icon="🕵️‍♀️")


# --- PLACEHOLDER FOR IMAGE HOSTING (FOR SHARE FUNCTIONALITY) ---
def upload_to_imgbb(image_bytes, api_key):
    """
    Uploads an image to imgbb.com and returns the URL.
    This is a placeholder. To make it work:
    1. Get a free API key from https://api.imgbb.com/
    2. Replace the placeholder logic with the actual API call.
    """
    # ---- REAL API CALL LOGIC (currently commented out) ----
    # api_url = "https://api.imgbb.com/1/upload"
    # payload = {
    #     "key": api_key,
    #     "image": base64.b64encode(image_bytes),
    # }
    # try:
    #     response = requests.post(api_url, payload)
    #     response.raise_for_status()  # Raise an exception for bad status codes
    #     result = response.json()
    #     if result["data"]["url"]:
    #         return result["data"]["url"]
    #     else:
    #         return None
    # except Exception as e:
    #     st.error(f"Failed to upload image for sharing: {e}")
    #     return None
    # ---- END OF REAL LOGIC ----

    # ---- DEMONSTRATION LOGIC (returns a fake link after a pause) ----
    with st.spinner("Generating shareable link..."):
        time.sleep(2) # Simulate network delay
    return "https://i.ibb.co/your-placeholder-image.png"


# --- UI LAYOUT ---
st.markdown("<h1 style='text-align: center; color: white;'>Image Steganography 🕵️‍♀️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a0a0a0;'>Hide your secret messages inside an image.</p>", unsafe_allow_html=True)
st.divider()

choice = st.radio(
    "**Select Your Operation:**",
    ("Encode Message", "Decode Message"),
    horizontal=True
)
st.divider()

# --- ENCODE OPERATION ---
if choice == "Encode Message":
    st.subheader("Encode a Message")
    col1, col2 = st.columns(2)

    with col1:
        uploaded_image = st.file_uploader("Upload an Image to Encode:", type=["png", "jpg", "jpeg"])
        if uploaded_image:
            st.image(uploaded_image, caption="Image to be encoded.", use_column_width=True)

    with col2:
        if uploaded_image:
            message = st.text_area(
                "**Enter your secret message below (max 300 characters):**",
                max_chars=300, height=150, placeholder="The eagle flies at midnight..."
            )
            
            if st.button("Encode Message", use_container_width=True, type="primary"):
                if not message:
                    st.warning("Please enter a message to encode.")
                else:
                    # --- YOUR BACKEND LOGIC FOR ENCODING ---
                    file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)

                    img_to_encode = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
                    
                    # Replace this with your actual encode function
                    st.info("Encoding in progress...")
                    encoded_image_array = obj.encode(img_to_encode, message) 
                    
                    _, buffer = cv2.imencode('.png', encoded_image_array)
                    image_bytes_for_download = buffer.tobytes()
                    # --- END OF YOUR BACKEND LOGIC ---
                    
                    st.success("✅ Message Encoded Successfully!")
                    st.markdown("---")
                    st.markdown("#### **Get Your Encoded Image:**")

                    # --- DOWNLOAD & SHARE BUTTONS ---
                    btn_col1, btn_col2 = st.columns(2)

                    with btn_col1:
                        # DOWNLOAD BUTTON
                        st.download_button(
                            label="📥 Download Image",
                            data=image_bytes_for_download,
                            file_name="encoded_image.png",
                            mime="image/png",
                            use_container_width=True
                        )
                    
                    with btn_col2:
                        # SHARE BUTTON
                        if st.button("🔗 Generate Share Link", use_container_width=True):
                            # --- API KEY (replace with your own) ---
                            IMGBB_API_KEY = "YOUR_API_KEY_HERE" # IMPORTANT!
                            
                            if IMGBB_API_KEY == "YOUR_API_KEY_HERE":
                                st.error("Please add your ImgBB API key to the code to enable sharing.")
                            else:
                                shareable_link = upload_to_imgbb(image_bytes_for_download, IMGBB_API_KEY)
                                if shareable_link:
                                    st.text_input("Copy & Share this link:", value=shareable_link, disabled=False)
                                else:
                                    st.error("Could not generate a shareable link.")


# --- DECODE OPERATION ---
elif choice == "Decode Message":
    st.subheader("Decode a Message")
    encoded_image_upload = st.file_uploader("Upload an Encoded Image to Decode:", type=["png"])

    if encoded_image_upload:
        st.image(encoded_image_upload, caption="Image to be decoded.", use_column_width=True)
        
        if st.button("Decode Message", use_container_width=True, type="primary"):
            # --- YOUR BACKEND LOGIC FOR DECODING ---
            file_bytes = np.asarray(bytearray(encoded_image_upload.read()), dtype=np.uint8)
            img_to_decode = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            
            st.info("Decoding in progress...")
            # Replace this with your actual decode function
            decoded_message = obj.decode(img_to_decode)
            # --- END OF YOUR BACKEND LOGIC ---
            
            st.success("✅ Message Decoded Successfully!")
            st.text_area(
                "**Decoded Message:**", value=decoded_message, height=150, disabled=True
            )