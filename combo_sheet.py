#!/usr/bin/env python3

import sys
from subprocess import call

from common import *

SVG_FILENAME = "SR4_Charsheet_2017v3_P000_Combo.svg"
PDF_FILENAME = "SR4_Charsheet_2017v3_P000_Combo.pdf"

def add_commlink(parent, margin=(0.0,0.25,0.0,0.25)):
  cl = parent.add_child(Margin(margin)).add_child(FlexGrid([1],[1,1,1,4]))

  cl.add_child(WriteIn("Model"))
  cl.add_child(WriteIn("OS"))
  row = cl.add_child(FlexGrid([1,1,1,1],[1]))
  row.add_child(WriteIn("Rsp"))
  row.add_child(WriteIn("Sig"))
  row.add_child(WriteIn("Sys"))
  row.add_child(WriteIn("FW"))
  cl.add_child(Table(
    columns = (1,),
    headings = ("Programs",),
    anchors = ("start",),
    data = ()
  ))

def add_armor_set(parent, margin=0.0):
  armor = parent.add_child(Margin(margin))

  armor.add_child(Table(
    columns = (10,3,3,12),
    headings = ("Armor","B","I","Notes"),
    anchors = ("start","middle","middle","middle"),
    data = (
      (None, None, None, None),
      (None, None, None, None),
      (None, None, None, None),
      (None, None, None, None),
      ("Combined", None, None, None),
      ("Plus Body", None, None, None),
    )
  ))

def main():
  print("Creating sheet...")
  
  page = Page(margin=10)

  temp = page.add_child(FlexGrid([1],[10,90]))
  
  header = temp.add_child(FlexGrid([33,66],[1]))
  columns = temp.add_child(FlexGrid([33,33,33],[1]))
  
  header.add_child(make_info_box("SR4 Character - Combo Sheet"))
  add_identity(header.add_child(BorderBox("SIN")), margin=0.0)

  page.l_col = columns.add_child(Margin(0))
  page.m_col = columns.add_child(Margin(0))
  page.r_col = columns.add_child(Margin(0))



  col = page.l_col.add_child(FlexGrid([1],[16,12,10,5,21,26]))
  information = col.add_child(BorderBox("General Information")).add_child(FlexGrid([5,4],[1,1,1,1,1,1,1]))
  col.add_child(BorderBox("Standard Attributes")).add_child(ATTRIBUTE_TABLE)
  col.add_child(BorderBox("Special Attributes")).add_child(SPECIAL_ATTRIBUTE_TABLE)
  karma = col.add_child(BorderBox("Karma")).add_child(FlexGrid((1,1),(1,)))
  col.add_child(BorderBox("Qualities")).add_child(QUALITY_TABLE)
  col.add_child(BorderBox("Augs/Forms/Powers/Spells/Notes")).add_child(SPELLS_ETC_TABLE)



  col = page.m_col.add_child(FlexGrid([1],[38,26,14,12]))
  col.add_child(BorderBox("Active Skills")).add_child(ACTIVE_SKILLS_TABLE)
  col.add_child(BorderBox("Knowledge &amp; Language Skills")).add_child(KNOWLEDGE_SKILLS_TABLE)
  col.add_child(BorderBox("Contacts")).add_child(CONTACT_TABLE)
  col.add_child(BorderBox("Assets")).add_child(ASSETS_TABLE)



  col = page.r_col.add_child(FlexGrid([1],[16,22,18,16,18]))
  add_commlink(col.add_child(BorderBox("Commlink")).add_child(FlexGrid([1],[7])))
  ranged_weapons = col.add_child(BorderBox("Ranged Weapons")).add_child(FlexGrid([1],[1,1]))
  melee_weapons = col.add_child(BorderBox("Melee Weapons")).add_child(FlexGrid([1],[1,1]))
  add_armor_set(col.add_child(BorderBox("Armor")))
  col.add_child(BorderBox("Other Gear")).add_child(OTHER_GEAR_TABLE)


  for l,r in INFO_DATA:
    information.add_child(WriteIn(l))
    information.add_child(WriteIn(r))

  karma.add_child(WriteIn("Total"))
  karma.add_child(WriteIn("Spent"))

  add_ranged_weapon(ranged_weapons, margin=(0.0,0.0,0.3,0.0))
  add_ranged_weapon(ranged_weapons, margin=(0.3,0.0,0.0,0.0))

  add_melee_weapon(melee_weapons, margin=(0.0,0.0,0.3,0.0))
  add_melee_weapon(melee_weapons, margin=(0.3,0.0,0.0,0.0))

#  col.add_child(BorderBox("Condition")).add_child(CONDITION_TABLE)
#  col.add_child(BorderBox("Notes")).add_child(NOTES_TABLE)
  
#  gear.add_child(Margin(0.3)).add_child(OTHER_GEAR_TABLE)


  page.update()
  
  print("Writing SVG file...")
  with open(SVG_FILENAME, "w") as fh:
    page.draw(fh)
  
  print("Converting to PDF...")
  call(["inkscape","-T","-A",PDF_FILENAME,SVG_FILENAME])

INFO_DATA = (
    ("Gender",      "Age"   ), 
    ("Metatype",    "Height"),
    ("Ethnicity",   "Weight"),
    ("Nationality", "Build" ),
    ("Allegiance",  "Skin"  ),
    ("Street Cred", "Hair"  ),
    ("Notoriety",   "Eyes"  ),
)

ATTRIBUTE_TABLE = Table(
  columns = (8,4,4,8,4,4),
  headings = ("Attribute","Base","Aug","Attribute","Base","Aug"),
  anchors = ("start","middle","middle","start","middle","middle"),
  data = (
    ("Body",      None, None, "Charisma",  None, None),
    ("Agility",   None, None, "Intuition", None, None),
    ("Reaction",  None, None, "Logic",     None, None),
    ("Strength",  None, None, "Willpower", None, None),
  )
)

SPECIAL_ATTRIBUTE_TABLE = Table(
  columns = (8,8,8,4,4),
  headings = ("Attribute","Rating","Initiative","DP","IP"),
  anchors = ("start","middle","start","middle","middle"),
  data = (
    ("Edge",      None, "Physical", None, None),
    ("Essence",   None, "Astral",   None, None),
    ("Mag/Res",   None, "Matrix",   None, None),
  )
)

MOVEMENT_TABLE = Table(
  columns = (8,6,6,6,6),
  headings = ("Type","m/pass","m/rnd","km/hr","mi/hr"),
  anchors = ("start","middle","middle","middle","middle"),
  data = (
    ("Walking", None, None, None, None),
    ("Running", None, None, None, None),
  )
)

QUALITY_TABLE = Table(
  columns = (7,1),
  headings = ("Quality","BP"),
  anchors = ("start","middle"),
  data = ()
)

CONDITION_TABLE = Table(
  columns = (3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
  headings = None,
  anchors = ("start","middle","middle","middle","middle","middle","middle","middle","middle","middle","middle","middle","middle","middle","middle","middle","middle"),
  data = (
    ("Stun",None,None,"-1",None,None,"-2",None,None,"-3",None,None,"-4",None,None,"-5"),
    ("Lethal",None,None,"-1",None,None,"-2",None,None,"-3",None,None,"-4",None,None,"-5"),
  )
)

CONTACT_TABLE = Table(
  columns = (11,3,3,11),
  headings = ("Name","Con","Loy","Type"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

ASSETS_TABLE = Table(
  columns = (17,11),
  headings = ("Description","Value"),
  anchors = ("start","middle"),
  data = (("Certified Creds",),)
)

SPELLS_ETC_TABLE = Table(
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

OTHER_GEAR_TABLE = Table(
  columns = (1,),
  headings = None,
  anchors = ("start",),
  data = ()
)

ACTIVE_SKILLS_TABLE = Table(
  columns = (11,3,3,11),
  headings = ("Skill Name","Att","Rtg","Specialization"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

KNOWLEDGE_SKILLS_TABLE = Table(
  columns = (11,3,3,11),
  headings = ("Skill Name","Att","Rtg","Specialization"),
  anchors = ("start","middle","middle","middle"),
  data = ()
)

GRPD_SKLS_TABLE = Table(
  columns = (11,3,3,11),
  headings = ("Skill Name","Att","Rtg","Specialization"),
  anchors = ("start","middle","middle","middle"),
  data = (
    ("Athletics",           "---", None, None),
    ("- Climbing",          "Str", None, None),
    ("- Gymnastics",        "Agi", None, None),
    ("- Running",           "Str", None, None),
    ("- Swimming",          "Str", None, None),
    ("Biotech",             "---", None, None),
    ("- Cybertech*",        "Log", None, None),
    ("- First Aid",         "Log", None, None),
    ("- Medicine*",         "Log", None, None),
    ("Close Combat",        "---", None, None),
    ("- Blades",            "Agi", None, None),
    ("- Clubs",             "Agi", None, None),
    ("- Unarmed",           "Agi", None, None),
    ("Conjuring",           "---", None, None),
    ("- Banishing",         "Mag", None, None),
    ("- Binding",           "Mag", None, None),
    ("- Summoning",         "Mag", None, None),
    ("Cracking",            "---", None, None),
    ("- Cybercombat",       "Log", None, None),
    ("- E-Warfare*",        "Log", None, None),
    ("- Hacking",           "Log", None, None),
    ("Electronics",         "---", None, None),
    ("- Computer",          "Log", None, None),
    ("- Data Search",       "Log", None, None),
    ("- Hardware*",         "Log", None, None),
    ("- Software*",         "Log", None, None),
    ("Firearms",            "---", None, None),
    ("- Automatics",        "Agi", None, None),
    ("- Longarms",          "Agi", None, None),
    ("- Pistols",           "Agi", None, None),
    ("Influence",           "---", None, None),
    ("- Con",               "Cha", None, None),
    ("- Etiquette",         "Cha", None, None),
    ("- Leadership",        "Cha", None, None),
    ("- Negotiation",       "Cha", None, None),
    ("Mechanic",            "---", None, None),
    ("- Aeronautics*",      "Log", None, None),
    ("- Automotive*",       "Log", None, None),
    ("- Industrial*",       "Log", None, None),
    ("- Nautical*",         "Log", None, None),
    ("Outdoors",            "---", None, None),
    ("- Navigation",        "Int", None, None),
    ("- Survival",          "Wil", None, None),
    ("- Tracking",          "Int", None, None),
    ("Sorcery",             "---", None, None),
    ("- Counterspelling",   "Mag", None, None),
    ("- Ritual Casting",    "Mag", None, None),
    ("- Spellcasting",      "Mag", None, None),
    ("Stealth",             "---", None, None),
    ("- Disguise",          "Int", None, None),
    ("- Infiltration",      "Agi", None, None),
    ("- Palming",           "Agi", None, None),
    ("- Shadowing",         "Int", None, None),
    ("Tasking",             "---", None, None),
    ("- Compiling*",        "Res", None, None),
    ("- Decompiling*",      "Res", None, None),
    ("- Registering*",      "Res", None, None),
  )
)

UGRP_SKLS_TABLE = Table(
  columns = (11,3,3,11),
  headings = ("Skill Name","Att","Rtg","Specialization"),
  anchors = ("start","middle","middle","middle"),
  data = (
    ("Arcana",            "Log", None, None),
    ("Archery",           "Agi", None, None),
    ("Armorer",           "Log", None, None),
    ("Artisan",           "Int", None, None),
    ("Assensing*",        "Int", None, None),
    ("Astral Combat*",    "Wil", None, None),
    ("Chemistry",         "Log", None, None),
    ("Demolitions",       "Log", None, None),
    ("Diving",            "Bod", None, None),
    ("Dodge",             "Rea", None, None),
    ("Enchanting",        "Log", None, None),
    ("Escape Artist",     "Agi", None, None),
    ("Forgery",           "Agi", None, None),
    ("Gunnery",           "Agi", None, None),
    ("Heavy Weapons",     "Agi", None, None),
    ("Instruction",       "Cha", None, None),
    ("Intimidation",      "Cha", None, None),
    ("Locksmith",         "Agi", None, None),
    ("Parachuting",       "Bod", None, None),
    ("Perception",        "Int", None, None),
    ("Pilot Aerospace*",  "Rea", None, None),
    ("Pilot Aircraft*",   "Rea", None, None),
    ("Pilot Anthroform*", "Rea", None, None),
    ("Pilot Groundcraft", "Rea", None, None),
    ("Pilot Watercraft",  "Rea", None, None),
    ("Thrown Weapons",    "Agi", None, None),
    (None,                None,  None, None),
    (None,                None,  None, None),
    (None,                None,  None, None),
    (None,                None,  None, None),
    (None,                None,  None, None),
    (None,                None,  None, "*no defaulting"),
  )
)


if __name__ == "__main__": main()
