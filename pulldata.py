import io

from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer3.pdfpage import PDFPage

resource_manager = PDFResourceManager()

with io.StringIO() as pdf_data:
    with TextConverter(resource_manager, pdf_data, laparams=LAParams()) as converter:
        process_page = PDFPageInterpreter(resource_manager, converter)

        with open("smileusage.pdf", "rb") as fh:
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                process_page.process_page(page)

            text = pdf_data.getvalue()

        result = []
        for x in text.splitlines():
            try:
                if "MB" in x and "0.0 MB" not in x:
                    see_data = x.replace("-", "").replace(",", "").split(" MB")
                    result.append(float(see_data[0]))

            except ValueError as e:
                pass

        print(sum(result))
