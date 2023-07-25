import docx2python
import docx2txt
from pdf2txt import PDF2Text

def convert_docx_to_text(docx_file_path):
    data = docx2python.docx2python(docx_file_path)
    text = ""
    for paragraph in data.body:
        if paragraph['type'] == 'paragraph':
            text += paragraph['content'] + "\n"
    return text

def convert_doc_to_text(doc_file_path):
    text = docx2txt.process(doc_file_path)
    return text

def convert_pdf_to_text(pdf_file_path):
    p2t = PDF2Text()
    text = p2t.extract(pdf_file_path)
    return text

if __name__ == "__main__":
    # Replace these file paths with your input files
    docx_file_path = "path/to/your/document.docx"
    doc_file_path = "path/to/your/document.doc"
    pdf_file_path = "path/to/your/document.pdf"

    # Convert DOCX to text
    docx_text = convert_docx_to_text(docx_file_path)
    print("DOCX Text:\n", docx_text)

    # Convert DOC to text
    doc_text = convert_doc_to_text(doc_file_path)
    print("DOC Text:\n", doc_text)

    # Convert PDF to text
    pdf_text = convert_pdf_to_text(pdf_file_path)
    print("PDF Text:\n", pdf_text)