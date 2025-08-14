from langchain_community.document_loaders import WebBaseLoader
from PyPDF2 import PdfReader
from services.preprocess import clean_page_content

def url_scraper(url):
    loader = WebBaseLoader(url)
    data = loader.load()
    return clean_page_content(data[0].page_content)

def pdf_scraper(file_object):
    pdf_reader = PdfReader(file_object)
    all_text = ""
    for page in pdf_reader.pages:
        all_text += page.extract_text() + "\n"
    cleaned_pdf_data = clean_page_content(all_text)
    return cleaned_pdf_data