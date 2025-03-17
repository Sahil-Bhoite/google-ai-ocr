# Google AI OCR

A Streamlit-based application that extracts structured text from images using Google AI Vision powered by the gemma3:12b model via Ollama. This app allows users to upload images and retrieve readable text in a well-organized Markdown format.

## Features

- Upload images (PNG, JPG, JPEG) and extract text.
- Display results in a structured Markdown format.
- Clear results with a single click.
- Responsive and user-friendly interface.
- Powered by Google AI Vision and hosted via Streamlit.

## Prerequisites

- Python 3.7 or higher
- Streamlit
- Ollama with the gemma3:12b model
- Required Python libraries (listed below)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Sahil-Bhoite/google-ai-ocr
cd google-ai-ocr
```

### Step 2: Install Dependencies

Create a virtual environment and install the required Python packages:

```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

**Note**: Create a requirements.txt file with the following content if not already present:

```text
streamlit
ollama
Pillow
```

### Step 3: Download and Set Up Ollama

Ollama is required to run the gemma3:12b model locally. Follow these steps to install Ollama and the model:

#### Install Ollama

1. Visit the Ollama official website or use the installation command for your operating system:
   * **MacOS/Linux**:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```
   * **Windows**: Download the installer from the Ollama GitHub releases page and follow the installation instructions.

2. Verify the installation by running:
   ```bash
   ollama --version
   ```

#### Download the gemma3:12b Model

1. Pull the gemma3:12b model using the Ollama CLI:
   ```bash
   ollama pull gemma3:12b
   ```
   * This command downloads the model (approximately 12GB) to your local machine. Ensure you have sufficient disk space.
   * The process may take some time depending on your internet speed.

2. Verify the model is available:
   ```bash
   ollama list
   ```
   You should see gemma3:12b in the list of installed models.

#### Run Ollama

Start the Ollama server to make the model accessible to the app:

```bash
ollama serve
```

Leave this terminal open and proceed to run the Streamlit app in a new terminal.

### Step 4: Run the Application

1. Ensure the Ollama server is running (from the previous step).
2. Launch the Streamlit app:
   ```bash
   streamlit run main.py
   ```
3. Open your browser and navigate to http://localhost:8501 to use the app.

## Usage

1. **Upload an Image**: Use the sidebar to upload an image file (PNG, JPG, JPEG) up to 10MB.
2. **Extract Text**: Click the "Extract Text" button to process the image and extract text using the gemma3:12b model.
3. **View Results**: The extracted text will appear in the main area in a structured Markdown format.
4. **Clear Results**: Click the "Clear" button in the sidebar to reset the app.
5. **Footer**: Access the portfolio link or learn that the app is powered by Google AI.

## Project Structure

* main.py: The main Streamlit application file.
* requirements.txt: List of Python dependencies (create if not present).

## Customization

* **Model**: The app uses gemma3:12b. To use a different model, modify MODEL_NAME in main.py and pull the new model with Ollama.
* **Styling**: Adjust the CSS in the st.markdown() call under Custom CSS to customize the appearance.
