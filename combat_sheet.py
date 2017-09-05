#!/usr/bin/env python3

import sys
from subprocess import call

from common import *

SVG_FILENAME = "SR4_Charsheet_2017v3_P003_Combat.svg"
PDF_FILENAME = "SR4_Charsheet_2017v3_P003_Combat.pdf"

def main():
  print("Creating sheet...")

  page = ThreeColumnPage("SR4 Character - Combat Sheet")

  col = page.l_col.add_child(FlexGrid([1],[10,60,20]))
  col.add_child(BorderBox("Martial Arts")).add_child(MARTIAL_ARTS_TABLE)

  close_combat = col.add_child(BorderBox("Close Combat")).add_child(FlexGrid([1],[1,1,1,1,1,1,1,1]))
  for x in range(8):
    add_melee_weapon(close_combat, margin=(0.25,0.0,0.25,0.0))

  col.add_child(BorderBox("Grenades")).add_child(GRENADE_TABLE)

  col = page.m_col.add_child(FlexGrid([1],[80,20]))
  ranged_weapons = col.add_child(BorderBox("Ranged Weapons")).add_child(FlexGrid([1],[1,1,1,1,1,1,1,1]))
  col.add_child(BorderBox("Ammunition")).add_child(AMMUNITION_TABLE)

  col = page.r_col.add_child(FlexGrid([1],[20,60,20]))
  col.add_child(BorderBox("Notes")).add_child(NOTES_TABLE)
  armor_sets = col.add_child(BorderBox("Armor Sets")).add_child(FlexGrid([1],[1,1,1,1]))
  #col.add_child(BorderBox("Combat Modifiers")).add_child(MODIFIER_TABLE)
  col.add_child(BorderBox("Notes")).add_child(NOTES_TABLE_TWO)

  for x in range(8):
    add_ranged_weapon(ranged_weapons, margin=(0.25,0.0,0.25,0.0))
    
    
  for x in range(4):
    add_armor_set(armor_sets)

  page.update()

  print("Writing SVG file...")
  with open(SVG_FILENAME, "w") as fh:
    page.draw(fh)
  
  print("Converting to PDF...")
  call(["inkscape","-T","-A",PDF_FILENAME,SVG_FILENAME])

CHAR_INFO_TABLE = Table(
  columns = (3,9),
  headings = None,
  anchors = ("start","end"),
  data = (
    ("Name", None),
    ("Alias", None),
    ("Concept", None),
    ("Player", None)
  )
)

MARTIAL_ARTS_TABLE = Table(
  columns = (1,),
  headings = None,
  anchors = ("start",),
  data = ()
)

AMMUNITION_TABLE = Table(
  columns = (6,6,3),
  headings = ("Weapon Type","Ammo Type","Qty"),
  anchors = ("start","middle","middle"),
  data = ()
)

GRENADE_TABLE = Table(
  columns = (8,2,2,3,3),
  headings = ("Grenade Type","DV","AP","AOE","Qty"),
  anchors = ("start","middle","middle","middle","middle"),
  data = ()
)

MODIFIER_TABLE = Table(
  columns = (6,5),
  headings = None,
  anchors = ("start","middle"),
  data = (
    ("Any Attacker",None),
    ("- using off-hand","-2"),
    ("- wounded","wound pen"),
    (None, None, None),
    ("Any Defender",None),
    ("- multiple defenses","-1 per"),
    ("- unaware of attack","no defense"),
    ("- wounded","wound pen"),
    (None, None, None),
    ("Ranged Attacker",None),
    ("- running","-2"),
    ("- in melee","-3"),
    ("- in a moving vehicle","-3"),
    ("- firing from cover","-2"),
    ("- firing blind","-6"),
    ("- using a laser sight","+1"),
    ("- using a smartlink","+2"),
    ("- aiming","+1 per aim action"),
    ("- dual-weilding","split pool"),
    ("- at point blank","+2"),
    ("- at short range","-0"),
    ("- at medium range","-1"),
    ("- at long range","-3"),
    ("- at extreme range","-6"),
    ("- using magnification","no range pen"),
    (None, None, None),
    ("Ranged Defender",None),
    ("- running","+2"),
    ("- in melee","-3"),
    ("- in a moving vehicle","+3"),
    ("- vs area attack","-2"),
    ("- in partial cover","+2"),
    ("- in good cover","+4"),
    (None, None, None),
    ("Melee Attacker",None),
    ("- charging attack","+2"),
    ("- has superior position","+2"),
    ("- only requires touch","+2"),
    ("- outnumbering","+1 to +4"),
    ("- multiple targets","split pool"),
    (None, None, None),
    ("Melee Defender",None),
    ("- prone","-2"),
    ("- set to receive charge","+1"),
    ("- outnumbering","+1 to +4"),
  )
)

NOTES_TABLE = Table(
  columns = (1,),
  headings = None,
  anchors = ("start",),
  data = ()
)

NOTES_TABLE_TWO = Table(
  columns = (1,),
  headings = None,
  anchors = ("start",),
  data = ()
)

if __name__ == "__main__": main()
