from langchain_community.llms import Ollama
import os
import PyPDF2
from docx import Document
from PIL import Image
import pytesseract

# functions to extract text from PDF, DOCX or images

def pdf_extractor(filepath):
    output = ""
    with open(filepath, "rb") as file:

        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            output = output + text + "\n"

    return output


def docx_extractor(filepath):
    output = ""
    doc = Document(filepath)
    for para in doc.paragraphs:
        output += para.text + "\n"

    return output


def img_extractor(filepath):
    img = Image.open(filepath)
    output = pytesseract.image_to_string(img)

    return output

# Function to execute Ollama and get response based on prompt (user instruction + textual input) 

def ollama_procedure(user_input, filepath):
    
    llm = Ollama(model="llama3")
    filepath = os.path.normpath(filepath)

    if filepath.lower().endswith(".pdf"):
        output = pdf_extractor(filepath)
    elif filepath.lower().endswith(".docx"):
        output = docx_extractor(filepath)
    elif filepath.lower().endswith((".jpg", ".jpeg", ".png")):
        output = img_extractor(filepath)
    else:
        output = "No supported file type"

    input = output[:512]            # llm can take max 512 character hence [:512]

    response = llm.invoke(f"{user_input}" + input)

    return response
