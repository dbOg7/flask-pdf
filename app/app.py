import os
from flask import Flask, render_template, url_for
from xhtml2pdf import pisa
from io import StringIO, BytesIO

app = Flask(__name__)

os.environ.get('.env')


@app.route('/')
def home():
    return render_template('home.html')


class Pdf():

    def render_pdf(self, name, html):
        pdf = BytesIO()
        pisa.CreatePDF(StringIO(html), pdf)
        return pdf.getvalue()

@app.route('/pdf',  methods=['GET'])
def view_invoice():

    html = render_template('home.html')
    file_class = Pdf()
    pdf = file_class.render_pdf('home.html',html)
    headers = {
        'content-type': 'application.pdf',
        'content-disposition': 'attachment; filename=certificate.pdf'}
    return pdf, 200, headers