from docx import Document
from docx.shared import Pt
from docx.shared import RGBColor


class my_docx:
    purple_color = RGBColor(0x80, 0x00, 0x80)
    def __init__(self):
        self.purple_color = RGBColor(0x80, 0x00, 0x80)
        pass
    
    def get_docx():
        """
        Creates docx document.

        Returns:
            Document: docx document

        """
        purple_color = RGBColor(0x80, 0x00, 0x80)
        document = Document()
        document.styles['Normal'].font.name = 'Arial'
        document.styles['Normal'].font.size = Pt(12)
        document.styles['Heading 1'].font.name = 'Arial'
        document.styles['Heading 1'].font.size = Pt(32)
        document.styles['Heading 1'].bold = True
        document.styles['Heading 1'].color = purple_color
        document.styles['Heading 2'].font.name = 'Arial'
        document.styles['Heading 2'].font.size = Pt(24)
        document.styles['Heading 2'].bold = True
        document.styles['Heading 2'].color = purple_color
        document.styles['Heading 3'].font.name = 'Arial'
        document.styles['Heading 3'].font.size = Pt(18)
        document.styles['Heading 3'].bold = True
        document.styles['Heading 3'].color = purple_color
        return document
