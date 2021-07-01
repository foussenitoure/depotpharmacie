
#Copyright ReportLab Europe Ltd. 2000-2017
#see license.txt for license details
__version__='3.3.0'
__doc__="""
The Canvas object is the primary interface for creating PDF files. See
doc/reportlab-userguide.pdf for copious examples.
"""

__all__ = ['Canvas']
ENABLE_TRACKING = 1 # turn this off to do profile testing w/o tracking

import os
import sys
import re
import hashlib
from string import digits
import tempfile
from math import sin, cos, tan, pi, ceil
from reportlab import rl_config, ascii, xrange
from reportlab.pdfbase import pdfutils
from reportlab.pdfbase import pdfdoc
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen  import pdfgeom, pathobject
from reportlab.pdfgen.textobject import PDFTextObject, _PDFColorSetter
from reportlab.lib.colors import black, _chooseEnforceColorSpace, Color, CMYKColor, toColor
from reportlab.lib.utils import import_zlib, ImageReader, isSeq, isStr, isUnicode, _digester
from reportlab.lib.rl_accel import fp_str, escapePDF
from reportlab.lib.boxstuff import aspectRatioFix

from reportlab.pdfgen import canvas

c = canvas.Canvas("essai.pdf")
from reportlab.lib.units import inch

# move the origin up and to the left
c.translate(inch, inch)
# define a large font
c.setFont("Helvetica", 80)
# choose some colors
c.setStrokeColorRGB(0.2, 0.5, 0.3)
c.setFillColorRGB(1, 0, 1)
# draw a rectangle
c.rect(inch, inch, 6 * inch, 9 * inch, fill=1)
# make text go straight up
c.rotate(90)
# change color
c.setFillColorRGB(0, 0, 0.77)
# say hello (note after rotate the y coord needs to be negative!)
c.drawString(6 * inch, -6 * inch, "welcome my project pharmacie")
c.showPage()
c.save()