#!/usr/bin/env python3

import sys
from subprocess import call

from common import *

SVG_FILENAME = "SR4_Charsheet_2017v3_P002_Secondary.svg"
PDF_FILENAME = "SR4_Charsheet_2017v3_P002_Secondary.pdf"

def main():
  print("Creating sheet...")

  page = TwoColumnRightPage("SR4 Character - Secondary Sheet")

  col = page.l_col.add_child(FlexGrid([1],[22,22,26,20]))
  col.add_child(BorderBox("Assets")).add_child(ASSETS_TABLE)
  col.add_child(BorderBox("Liabilities")).add_child(LIABILITIES_TABLE)
  col.add_child(BorderBox("Contacts")).add_child(CONTACTS_TABLE)
  col.add_child(BorderBox("Notes")).add_child(NOTES_TABLE)

  col = page.r_col.add_child(FlexGrid([1],[24,30,46]))
  identities = col.add_child(BorderBox("Identities")).add_child(FlexGrid([1],[1,1,1]))
  commlinks = col.add_child(BorderBox("Commlinks")).add_child(FlexGrid([1,1,1],[1]))
  col.add_child(BorderBox("Other Gear")).add_child(GEAR_TABLE)

  for x in range(3):
    add_identity(identities)


  for x in range(3):
    add_commlink(commlinks)
    
  page.update()

  print("Writing SVG file...")
  with open(SVG_FILENAME, "w") as fh:
    page.draw(fh)
  
  print("Converting to PDF...")
  call(["inkscape","-T","-A",PDF_FILENAME,SVG_FILENAME])

ASSETS_TABLE = Table(
  columns = (7,3),
  headings = ("Description","Value"),
  anchors = ("start","middle"),
  data = ()
)

LIABILITIES_TABLE = Table(
  columns = (7,3),
  headings = ("Description","Value"),
  anchors = ("start","middle"),
  data = ()
)

CONTACTS_TABLE = Table(
  columns = (14,3,3),
  headings = ("Name/Type","Con","Loy"),
  anchors = ("start","middle","middle"),
  data = ()
)

NOTES_TABLE = Table(
  columns = (1,),
  headings = None,
  anchors = ("start",),
  data = ()
)

GEAR_TABLE = Table(
  columns = (4,1,1,8),
  headings = ("Item","Rtg","Qty","Notes"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

IDENTITIES_TABLE = Table(
  columns = (3,3,1,5),
  headings = ("Name","Vocation","Rtg","Notes"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

if __name__ == "__main__": main()
