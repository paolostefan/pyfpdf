#!/usr/bin/env python
# -*- coding: utf8 -*-

from fpdf import FPDF, HTMLMixin
import sys

fn = 'unicode_cells.pdf'


class HPDF(FPDF, HTMLMixin):
    pass


pdf = HPDF()
pdf.add_page()


def print_sample_text(title='A nice title for an HTML text'):
    global pdf

    text = "<h2>{}</h2>".format(title) + u"""
    <p><b>English</b>: Hello World<br />
    Greek: Γειά σου κόσμος<br />
    Polish: Witaj świecie<br />
    Portuguese: Olá mundo<br />
    Russian: Здравствуй, Мир
    </p>
    <p>
    <i>Arabic</i>: مرحبا العالم<br />
    Hebrew: שלום עולם<br />
    </p>
    <h3>Asian languages</h3>
    <p>
    Vietnamese: Xin chào thế giới<br />
    Hindi: नमस्ते दुनिया<br />
    Chinese: 你好世界<br />
    Japanese: こんにちは世界<br />
    Korean: 안녕하세요<br />
    Thai: สวัสดีชาวโลก<br />
    </p>
    """

    pdf.write_html(text)
    pdf.ln(10)


# DejaVu Unicode font Supports more than 200 languages. For a coverage status see:
# http://dejavu.svn.sourceforge.net/viewvc/dejavu/trunk/dejavu-fonts/langcover.txt
#
# gargi: a Indic Unicode font (uses UTF-8)
# Supports: Bengali, Devanagari, Gujarati,
#           Gurmukhi (including the variants for Punjabi)
#           Kannada, Malayalam, Oriya, Tamil, Telugu, Tibetan
#
# fireflysung: AR PL New Sung Unicode font (uses UTF-8)
# The Open Source Chinese Font (also supports other east Asian languages)
#
# Eunjin: Alee Unicode font General purpose Hangul truetype fonts that contain Korean syllable
# and Latin9 (iso8859-15) characters.
#
# Waree: Fonts-TLWG (formerly ThaiFonts-Scalable)

print_sample_text()

# A standard font would give an encoding error
# print_sample_text('times', 'times')

pdf.output(fn, 'F')
import os

try:
    os.startfile(fn)
except:
    os.system("xdg-open \"%s\"" % fn)
