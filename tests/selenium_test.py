from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

def add_underlined_heading(doc, text, level):
    paragraph = doc.add_heading(text, level)
    if level == 0:  
        run = paragraph.runs[0]
        run.font.underline = True

add_underlined_heading(doc, '가장 큰 제목 (아래에 밑줄)', level=0)
doc.add_heading('제목 크기, H1', level=1)
doc.add_heading('제목 크기, H2', level=2)
doc.add_heading('제목 크기, H3', level=3)
doc.add_heading('제목 크기, H4', level=4)
doc.add_heading('제목 크기, H5', level=5)
doc.add_heading('제목 크기, H6', level=6)

for paragraph in doc.paragraphs:
    if paragraph.style.name.startswith('Heading'):
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.save('저장하고 싶은 파일명.docx')
