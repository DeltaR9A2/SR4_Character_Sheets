#!/usr/bin/env python3

import sys
from subprocess import call

from common import *

SVG_FILENAME = "SR4_Charsheet_2017v3_P007_Resonant.svg"
PDF_FILENAME = "SR4_Charsheet_2017v3_P007_Resonant.pdf"

def main():
  print("Creating sheet...")
  
  page = OneColumnPage("SR4 Character - Resonant Sheet")

  info = page.upper.add_child(BorderBox("Resonant Information")).add_child(FlexGrid([1],[2,1,1]))

  row = info.add_child(FlexGrid([1,1],[1,1]))
  row.add_child(WriteIn("Quality"))
  row.add_child(WriteIn("Stream"))
  row.add_child(WriteIn("Paragon"))
  row.add_child(WriteIn("Effects"))
  info.add_child(WriteIn("Sprites"))
  row = info.add_child(FlexGrid([1,1,1],[1]))
  row.add_child(WriteIn("Fade Resist"))
  row.add_child(WriteIn("Subm Grade"))
  row.add_child(WriteIn("Max Res"))

  lower = page.lower.add_child(FlexGrid([1],[70,20]))
  
  middle = lower.add_child(FlexGrid([1,2],[1]))

  sprites = middle.add_child(BorderBox("Sprites")).add_child(FlexGrid([1],[1,1,1,1,1,1]))
  
  for x in range(6):
    sprite = sprites.add_child(Margin(0.3)).add_child(FlexGrid([1],[1,2,1,1,1]))
    
    sprite.add_child(WriteIn("Sprite"))

    atts = sprite.add_child(FlexGrid([1,1,1,1],[1,1]))
    for a in ("Rtg","Svc","Reg","Init","Plt","Rsp","FW",""):
      atts.add_child(WriteIn(a))
    sprite.add_child(WriteIn("Notes"))
    sprite.add_child(Rect(styles["border"]))
    sprite.add_child(Rect(styles["border"]))

  
  col = middle.add_child(FlexGrid([1],[40,30]))
  col.add_child(BorderBox("Complex Forms")).add_child(FORMS_TABLE)
  col.add_child(BorderBox("Threaded Forms")).add_child(THREADS_TABLE)
  
  row = lower.add_child(FlexGrid([1,1,1],[1]))
  row.add_child(BorderBox("Echoes")).add_child(META_TABLE)
  row.add_child(BorderBox("Widgets")).add_child(FOCI_TABLE)
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

FORMS_TABLE = Table(
  columns = (18,4,18),
  headings = ("Complex Form","Rtg","Notes/Options"),
  anchors =  ("start","middle","middle"),
  data = ()
)

THREADS_TABLE = Table(
  columns = (18,4,18),
  headings = ("Threaded Form","Min Hits","Notes/Options"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

if __name__ == "__main__": main()
