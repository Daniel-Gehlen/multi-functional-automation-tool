import os
from PyPDF2 import PdfReader
from markdownify import markdownify as md

# Função para extrair texto do PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Função para salvar o texto extraído como Markdown
def save_as_markdown(text, md_path):
    markdown_text = md(text)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_text)

# Função principal para converter PDF para Markdown
def convert_pdf_to_md(pdf_path, md_path):
    if not os.path.exists(pdf_path):
        return f"Arquivo {pdf_path} não encontrado."
    
    try:
        # Extrair texto do PDF
        text = extract_text_from_pdf(pdf_path)
        
        # Salvar como Markdown
        save_as_markdown(text, md_path)
        
        return f"Arquivo {md_path} criado com sucesso."
    
    except Exception as e:
        return f"Erro ao processar o arquivo {pdf_path}: {str(e)}"
