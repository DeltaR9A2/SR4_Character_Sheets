#!/usr/bin/env python3

import sys
from subprocess import call

from common import *

SVG_FILENAME = "SR4_Charsheet_2017v3_P004_Vehicles.svg"
PDF_FILENAME = "SR4_Charsheet_2017v3_P004_Vehicles.pdf"

def main():
  print("Creating sheet...")
  
  page = OneColumnPage("SR4 Character - Vehicles Sheet")


  page.upper.add_child(BorderBox("Notes")).add_child(NOTES_TABLE)

  vehicles = page.lower.add_child(BorderBox("Vehicles")).add_child(FlexGrid([1],[1,1,1,1,1]))
  
  for x in range(1,6):
    vehicle = vehicles.add_child(Margin(0.3)).add_child(FlexGrid([1,1,1],[1]))

    col = vehicle.add_child(Margin(0.3)).add_child(FlexGrid([1],[1,1,1,1,1,1,1,1,1,1]))
    col.add_child(WriteIn("Vehicle"))

    row = col.add_child(FlexGrid([1,1,1],[1]))
    row.add_child(WriteIn("Hndl"))
    row.add_child(WriteIn("Accel"))
    row.add_child(WriteIn("Speed"))
    row = col.add_child(FlexGrid([1,1,1,1],[1]))
    row.add_child(WriteIn("Pilot"))
    row.add_child(WriteIn("Body"))
    row.add_child(WriteIn("Armor"))
    row.add_child(WriteIn("Snsr"))
    
    col.add_child(WriteIn("Mods"))
    for x in range(6):
      col.add_child(Rect(styles["border"]))

    col = vehicle.add_child(FlexGrid([1],[1,1]))

    for x in range(2):
      add_ranged_weapon(col, margin=0.3)

    col = vehicle.add_child(Margin(0.3)).add_child(FlexGrid([1],[1,1,1,1,1,1,1,1,1,1]))
    col.add_child(WriteIn("Notes"))
    for x in range(9):
      col.add_child(Rect(styles["border"]))

  page.update()
  
  print("Writing SVG file...")
  with open(SVG_FILENAME, "w") as fh:
    page.draw(fh)
  
  print("Converting to PDF...")
  call(["inkscape","-T","-A",PDF_FILENAME,SVG_FILENAME])

NOTES_TABLE = Table(
  columns = (1,),
  headings = None,
  anchors = ("start",),
  data = ()
)

if __name__ == "__main__": main()


