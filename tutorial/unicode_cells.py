#!/usr/bin/env python
# -*- coding: utf8 -*-

from fpdf import FPDF
import sys

fn = 'unicode_cells.pdf'



pdf = FPDF()
pdf.add_page()


def print_sample_text(fontname, title):
    global pdf

    text = u"""
    English: Hello World
    Greek: Γειά σου κόσμος
    Polish: Witaj świecie
    Portuguese: Olá mundo
    Russian: Здравствуй, Мир
    Vietnamese: Xin chào thế giới
    Arabic: مرحبا العالم
    Hebrew: שלום עולם
    Hindi: नमस्ते दुनिया / End Hindi
    Chinese: 你好世界 / End Chinese
    Japanese: こんにちは世界 / End Japanese 
    Korean: 안녕하세요 / End Korean
    Thai: สวัสดีชาวโลก / End thai
    """

    pdf.set_font(fontname, '', 12)
    pdf.write(6, title)
    pdf.ln()
    pdf.set_font(fontname, '', 10)
    pdf.multi_cell(100, 8, text, align='L', ln=1)
    pdf.ln(20)


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

for font in (
        'SourceSansPro-Regular.ttf', 'DejaVuSansCondensed.ttf', 'gargi.ttf', 'fireflysung.ttf', 'Eunjin.ttf',
        'Waree.ttf'):
    short = font.split(".")[0].lower()
    pdf.add_font(short, '', font, uni=True)
    print_sample_text(short, font)

# A standard font would give an encoding error
# print_sample_text('times', 'times')

pdf.output(fn, 'F')
import os

try:
    os.startfile(fn)
except:
    os.system("xdg-open \"%s\"" % fn)
