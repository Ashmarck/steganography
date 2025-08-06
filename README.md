# Steganography Streamlit App

A simple web application built with Streamlit to hide secret text messages within images. This project demonstrates basic steganography techniques in a user-friendly interface.

## Live Demo
You can access the live, deployed version of the app here:
**[https://ashstegano.streamlit.app/](https://ashstegano.streamlit.app/)**

## Features

- **Encode**: Hide a secret text message inside a cover image (`.png`, `.jpg`).
- **Decode**: Extract a hidden message from an encoded image.
- **User-Friendly Interface**: Clean, simple, and interactive UI powered by Streamlit.
- **Downloadable Output**: Easily download the newly encoded image.

### Planned Features
- ** Audio Steganography**: Hiding data within `.wav` files.
- ** Video Steganography**: Hiding data within video files.



##  Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Ashmarck/steganography.git
    cd steganography
    ```

2.  **Create and activate a virtual environment:**
    * **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

Once the setup is complete, run the Streamlit application with the following command:

```bash
streamlit run app.py
