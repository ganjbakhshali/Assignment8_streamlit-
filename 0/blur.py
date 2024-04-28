import streamlit as st
import cv2
import numpy as np

def blur_image(image, blur_degree):
    """
    Apply mean filter (blur) to the input image with the specified blur degree.
    """
    # Apply mean filter with kernel size (7, 7) and specified blur degree
    
    blurred_image = cv2.blur(image, (blur_degree, blur_degree))
    return blurred_image

def main():
    st.title("Image Blur App")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Display original image
        st.image(image, caption="Original Image", use_column_width=True)

        # Slider for blur degree
        blur_degree = st.slider("Blur Degree", min_value=0, max_value=99, value=50)

        # Apply blur
        blurred_image = blur_image(image, blur_degree)

        # Display blurred image
        st.image(blurred_image, caption=f"Blurred Image (Blur Degree: {blur_degree})", use_column_width=True)

if __name__ == "__main__":
    main()
