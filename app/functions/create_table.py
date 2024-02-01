import openpyxl
from openpyxl.styles import Font, NamedStyle

    
def create_table(filename: str, matrix: list):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    style: NamedStyle = NamedStyle(name="custom_style")
    font: Font = Font(name='Times New Roman', size=12, 
        bold=False, italic=False)
    bold_style = NamedStyle(name='bold_style', font=Font(bold=True))
    style.font = font

    for row_idx, row in enumerate(matrix, 1):
        for col_idx, value in enumerate(row, 1):
            cell = sheet.cell(row=row_idx, column=col_idx, value=value)
            cell.alignment = openpyxl.styles.Alignment(
                horizontal='left', vertical='center', shrink_to_fit=True)
            if row_idx == 1:
                cell.style = bold_style
        sheet.row_dimensions[row_idx].height = 50

    column_widths = {'A': 10, 'B': 12, 'C': 60, 'D': 60, 'E': 0}
    for col, width in column_widths.items():
        sheet.column_dimensions[col].width = width  
    sheet.delete_cols(openpyxl.utils.column_index_from_string('E'))
    workbook.save(filename)
