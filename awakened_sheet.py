#!/usr/bin/env python3

import sys
from subprocess import call

from common import *

SVG_FILENAME = "SR4_Charsheet_2017v3_P006_Awakened.svg"
PDF_FILENAME = "SR4_Charsheet_2017v3_P006_Awakened.pdf"

def main():
  print("Creating sheet...")
  
  page = OneColumnPage("SR4 Character - Awakened Sheet")

  info = page.upper.add_child(BorderBox("Awakened Information")).add_child(FlexGrid([1],[2,1,1]))

  row = info.add_child(FlexGrid([1,1],[1,1]))
  row.add_child(WriteIn("Quality"))
  row.add_child(WriteIn("Tradition"))
  row.add_child(WriteIn("Mentor"))
  row.add_child(WriteIn("Effects"))
  info.add_child(WriteIn("Spirits"))
  row = info.add_child(FlexGrid([1,1,1],[1]))
  row.add_child(WriteIn("Drain Resist"))
  row.add_child(WriteIn("Init Grade"))
  row.add_child(WriteIn("Max Mag"))

  lower = page.lower.add_child(FlexGrid([1],[70,20]))
  
  middle = lower.add_child(FlexGrid([1,2],[1]))

  spirits = middle.add_child(BorderBox("Spirits")).add_child(FlexGrid([1],[1,1,1,1,1,1]))
  
  for x in range(6):
    spirit = spirits.add_child(Margin(0.3)).add_child(FlexGrid([1],[1,3,1,1]))
    
    spirit.add_child(WriteIn("Spirit"))

    atts = spirit.add_child(FlexGrid([1,1,1,1],[1,1,1]))
    for a in ("Frc","Svc","Bnd","Init","Bod","Agi","Rea","Str","Cha","Int","Log","Wil"):
      atts.add_child(WriteIn(a))
    spirit.add_child(WriteIn("Notes"))
    spirit.add_child(Rect(styles["border"]))

  
  col = middle.add_child(FlexGrid([1],[40,30]))
  col.add_child(BorderBox("Spells")).add_child(SPELLS_TABLE)
  col.add_child(BorderBox("Powers")).add_child(POWERS_TABLE)
  
  row = lower.add_child(FlexGrid([1,1,1],[1]))
  row.add_child(BorderBox("Metamagic")).add_child(META_TABLE)
  row.add_child(BorderBox("Foci")).add_child(FOCI_TABLE)
  row.add_child(BorderBox("Notes")).add_child(NOTES_TABLE)
  page.update()
  
  print("Writing SVG file...")
  with open(SVG_FILENAME, "w") as fh:
    page.draw(fh)
  
  print("Converting to PDF...")
  call(["inkscape","-T","-A",PDF_FILENAME,SVG_FILENAME])


META_TABLE = Table(
  columns = (1,),
  headings = None,
  anchors = ("start",),
  data = ()
)

FOCI_TABLE = Table(
  columns = (1,),
  headings = None,
  anchors = ("start","middle"),
  data = (
  )
)

NOTES_TABLE = Table(
  columns = (1,),
  headings = None,
  anchors = ("start",),
  data = ()
)

SPELLS_TABLE = Table(
  columns = (10,3,3,3,3,10),
  headings = ("Spell Name","Type","Rng","Dur","Drain","Notes/Effects"),
  anchors = ("start","middle","middle","middle","middle","middle"),
  data = ()
)

POWERS_TABLE = Table(
  columns = (13,3,3,13),
  headings = ("Power Name","Rtg","PP","Notes/Effects"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

if __name__ == "__main__": main()
