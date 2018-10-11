# simple_table.py

from reportlab.lib.pagesizes import *
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import pandas as pd
from header import Header
from lxml import objectify



df = pd.read_csv(r'C:\Skyhook\Helsingborg\Commission\sales\Hel_Commissions.csv' , sep=',', encoding = "ANSI")

#print(df.info(verbose=True))

def parse_xml(xml_file):
    with open(xml_file) as f:
        xml = f.read()
    root = objectify.fromstring(xml)
    return root


def simple_table():
    doc = SimpleDocTemplate(r'C:\Skyhook\Helsingborg\Commission\sales\simple_table.pdf', pagesize=landscape((15*inch,20*inch)))
                            #,rightMargin=72, leftMargin=36,topMargin=36, bottomMargin=18)
    story = []

    # data = [['col_{}'.format(x) for x in range(1, 6)],
    #         [str(x) for x in range(1, 6)],
    #         ['a', 'b', 'c', 'd', 'e']
    #         ]
    ts = [('ALIGN', (1, 1), (-1, -1), 'CENTER'),
          ('LINEABOVE', (0, 0), (-1, 0), 1, colors.purple),
          ('LINEBELOW', (0, 0), (-1, 0), 1, colors.purple),
          ('FONT', (0, 0), (-1, 0), 'Times-Bold'),
          ('LINEABOVE', (0, -1), (-1, -1), 1, colors.purple),
          ('LINEBELOW', (0, -1), (-1, -1), 0.5, colors.purple, 1, None, None, 4, 1),
          ('LINEBELOW', (0, -1), (-1, -1), 1, colors.red),
          ('FONT', (0, -1), (-1, -1), 'Times-Bold'),
          ('BACKGROUND', (1, 1), (-2, -2), colors.whitesmoke),
          ('TEXTCOLOR', (0, 0), (1, -1), colors.red)]
    lista = [df.columns[:, ].values.astype(str).tolist()] + df.values.tolist()
    xml = parse_xml(r'C:\Skyhook\Helsingborg\Commission\sales\eob.xml')
    tbl = Table(lista, style=ts)
    header = Header(xml)
    story.append(header)
    story.append(Spacer(1, 50))
    story.append(tbl)
    doc.build(story)

if __name__ == '__main__':
    simple_table()






#
# def main(pdf_file, xml_file):
#     doc = SimpleDocTemplate(
#         pdf_file,
#         rightMargin=72, leftMargin=36,
#         topMargin=36, bottomMargin=18)
#     xml = parse_xml(xml_file)
#     elements = []
#     header = Header(xml)
#     elements.append(header)
#     doc.build(elements)
#
#
# if __name__ == '__main__':
# main(pdf_file='header.pdf', xml_file='eob.xml')