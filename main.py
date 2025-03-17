import streamlit as st
import ollama
from PIL import Image
import base64
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
MODEL_NAME = "gemma3:12b"
PAGE_TITLE = "Google AI OCR"
PAGE_ICON = "🔎"
GOOGLE_AI_LOGO_PATH = "GAI.png"

# Helper Functions
def get_base64_image(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        logger.error(f"Logo file not found at {file_path}")
        return ""

def process_image(file):
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{
                'role': 'user',
                'content': """Analyze the text in the provided image. Extract all readable content
                            and present it in a structured Markdown format that is clear, concise, 
                            and well-organized. Ensure proper formatting (e.g., headings, lists, or
                            code blocks) as necessary to represent the content effectively.""",
                'images': [file.getvalue()]
            }]
        )
        return response.message.content
    except Exception as e:
        logger.error(f"Error processing image: {e}")
        raise

# Page Configuration
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        padding: 20px;
    }
    .main-content {
        flex: 1 0 auto;
        padding: 20px 0;
    }
    .sidebar .stButton>button {
        width: 100%;
        margin-top: 10px;
    }
    .footer {
        flex-shrink: 0;
        text-align: center;
        font-size: 12px;
        color: #666;
        padding: 10px;
        background-color: #f8f9fa;
        border-top: 1px solid #e0e0e0;
        width: 100%;
    }
    .footer a {
        color: #1a73e8;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# UI Components
def render_header():
    st.markdown(
        f"""
        # <img src="data:image/png;base64,{get_base64_image(GOOGLE_AI_LOGO_PATH)}" alt="Google AI Logo" width="50" style="vertical-align: -12px;"> {PAGE_TITLE}
        <p style="margin-top: -10px;">Extract structured text from images using Google AI Vision!</p>
        """, 
        unsafe_allow_html=True
    )
    st.markdown("---")

def render_sidebar():
    with st.sidebar:
        st.header("Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image...", 
            type=['png', 'jpg', 'jpeg'], 
            help="Supported formats: PNG, JPG, JPEG. Max size: 10MB"
        )
        if uploaded_file:
            st.image(Image.open(uploaded_file), caption="Uploaded Image", use_container_width=True)
            if st.button("Extract Text 🔍", type="primary", help="Extract text from the uploaded image"):
                with st.spinner("Processing image..."):
                    try:
                        result = process_image(uploaded_file)
                        st.session_state['ocr_result'] = result
                    except Exception as e:
                        st.error(f"Failed to process image: {str(e)}")
        else:
            st.info("Upload an image to start the extraction process.")
        if st.button("Clear 🗑️", help="Clear the current OCR result"):
            if 'ocr_result' in st.session_state:
                del st.session_state['ocr_result']
            st.rerun()
        return uploaded_file

def render_results():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    if 'ocr_result' in st.session_state:
        st.markdown(st.session_state['ocr_result'])
    st.markdown('</div>', unsafe_allow_html=True)

def render_footer():
    st.markdown(
        '<div class="footer">'
        '<a href="https://sahil-bhoite.github.io/Portfolio/" target="_blank">Portfolio</a> | Powered by Google AI'
        '</div>',
        unsafe_allow_html=True
    )

# Main App Logic
def main():
    render_header()
    uploaded_file = render_sidebar()
    render_results()
    render_footer()

if __name__ == "__main__":
    main()