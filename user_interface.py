import streamlit as st
from PIL import Image


def main():
    st.title("Dynamic Banner Generator")

    # File uploader for a single image
    uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

    # Text input for a single promotional offer
    promotional_offer = st.text_input("Enter a promotional offer")

    # Dropdown for theme selection (single selection)
    theme = st.selectbox("Select a theme", ["Select theme","diwali", "independence_day"])

    if st.button("Generate Banner"):
        if uploaded_file and promotional_offer:
            # Open the uploaded image
            image = Image.open(uploaded_file).convert("RGB")
            
            # Generate the banner (replace with actual logic)
            banner = 'banner.jpg'

            # Display the generated banner
            st.image(banner, caption="Generated Banner")

            # Option to download the banner
            if st.button("Download Banner"):
                banner.save("generated_banner.png")  # Save the banner locally
                st.success("Banner saved as 'generated_banner.png'")

        else:
            st.error("Please upload an image and enter a promotional offer.")

if __name__ == "__main__":
    main()
