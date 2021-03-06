import io

from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter

resource_manager = PDFResourceManager()

with io.StringIO() as pdf_data:
    with TextConverter(resource_manager, pdf_data,
                       laparams=LAParams()) as converter:
        process_page = PDFPageInterpreter(resource_manager, converter)

        with open('smileusage.pdf', 'rb') as fh:
            for page in PDFPage.get_pages(fh,
                                          caching=True,
                                          check_extractable=True):
                process_page.process_page(page)

            text = pdf_data.getvalue()

        total = sum([
            float(x.replace('-', '').replace(',', '').split(' MB')[0])
            for x in text.splitlines() if "MB" in x and '0.0 MB' not in x
        ])

        print(total)
