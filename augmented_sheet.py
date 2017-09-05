#!/usr/bin/env python3

import sys
from subprocess import call

from common import *

SVG_FILENAME = "SR4_Charsheet_2017v3_P005_Augmented.svg"
PDF_FILENAME = "SR4_Charsheet_2017v3_P005_Augmented.pdf"

def main():
  print("Creating sheet...")
  
  page = ThreeColumnPage("SR4 Character - Augmented Sheet")

  col = page.l_col.add_child(FlexGrid([1],[10,18,22,20,20]))

  col.add_child(BorderBox("Essence Calculations")).add_child(ESSENCE_TABLE)
  head = col.add_child(BorderBox("Head")).add_child(FlexGrid([1],[2,7]))
  eyes = col.add_child(BorderBox("Eyes")).add_child(FlexGrid([1],[2,9]))
  ears = col.add_child(BorderBox("Ears")).add_child(FlexGrid([1],[2,8]))
  torso = col.add_child(BorderBox("Torso")).add_child(FlexGrid([1],[2,1,7]))


  col = page.m_col.add_child(FlexGrid([1],[20,20,20,20,20]))
  col.add_child(BorderBox("Body Mods")).add_child(MODS_TABLE)

  larm = col.add_child(BorderBox("Left Arm")).add_child(FlexGrid([1],[2,1,7]))
  rarm = col.add_child(BorderBox("Right Arm")).add_child(FlexGrid([1],[2,1,7]))
  lleg = col.add_child(BorderBox("Left Leg")).add_child(FlexGrid([1],[2,1,7]))
  rleg = col.add_child(BorderBox("Right Leg")).add_child(FlexGrid([1],[2,1,7]))


  col = page.r_col.add_child(FlexGrid([1],[20,20,20,20,20]))

  col.add_child(BorderBox("Notes")).add_child(NOTES_TABLE)
  col.add_child(BorderBox("Geneware")).add_child(GENE_TABLE)
  col.add_child(BorderBox("Nanoware")).add_child(NANO_TABLE)
  col.add_child(BorderBox("Other Cyberware")).add_child(CYBERWARE_TABLE)
  col.add_child(BorderBox("Other Bioware")).add_child(BIOWARE_TABLE)

  for x in (torso, larm, rarm, lleg, rleg):
    row = x.add_child(FlexGrid([1,1],[1,1]))
    
    row.add_child(WriteIn("Type"))
    row.add_child(WriteIn("Grade"))
    row.add_child(WriteIn("Ess Cost"))
    row.add_child(WriteIn("Capacity"))
    
    row = x.add_child(FlexGrid([1,1,1],[1]))
    row.add_child(WriteIn("Agi"))
    row.add_child(WriteIn("Bod"))
    row.add_child(WriteIn("Str"))

    add_aug_table(x)
    
  for x in (head, eyes, ears):
    row = x.add_child(FlexGrid([1,1],[1,1]))
    
    row.add_child(WriteIn("Type"))
    row.add_child(WriteIn("Grade"))
    row.add_child(WriteIn("Ess Cost"))
    row.add_child(WriteIn("Capacity"))
    
    add_aug_table(x)


  page.update()
  
  print("Writing SVG file...")
  with open(SVG_FILENAME, "w") as fh:
    page.draw(fh)
  
  print("Converting to PDF...")
  call(["inkscape","-T","-A",PDF_FILENAME,SVG_FILENAME])

ESSENCE_TABLE = Table(
  columns = (8,8),
  headings = ("Implant Type","Essence Loss"),
  anchors = ("middle","middle"),
  data = (
    ("Bioware",      None),
    ("Cyberware",   None),
    ("Combined",   None),
  )
)

def add_aug_table(parent):
  return parent.add_child(Table(
    columns = (8,2,3,3),
    headings = ("Augmentation","Rtg","Grade","Ess/Cap"),
    anchors = ("start","middle","middle","middle"),
    data = ()
  ))

GENE_TABLE = Table(
  columns = (11,2,3),
  headings = ("Augmentation","Rtg","Essence"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

NANO_TABLE = Table(
  columns = (8,2,3,3),
  headings = ("Augmentation","Rtg","Grade","Essence"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

CYBERWARE_TABLE = Table(
  columns = (8,2,3,3),
  headings = ("Augmentation","Rtg","Grade","Essence"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

BIOWARE_TABLE = Table(
  columns = (8,2,3,3),
  headings = ("Augmentation","Rtg","Grade","Essence"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

MODS_TABLE = Table(
  columns = (1,),
  headings = None,
  anchors = ("start",),
  data = ()
)

NOTES_TABLE = Table(
  columns = (1,),
  headings = None,
  anchors = ("start",),
  data = ()
)
   

if __name__ == "__main__": main()
