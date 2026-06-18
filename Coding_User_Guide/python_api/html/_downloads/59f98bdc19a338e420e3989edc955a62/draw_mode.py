import ansa
from ansa import base
from ansa import constants

def impactor_draw_mode():

  # Create DrawMode
  draw_mode = base.DrawMode("Impactor - area")

  impactor = base.GetEntity(constants.ABAQUS, 'SET', 1403)
  area = base.GetEntity(constants.ABAQUS, 'SET', 1404)

  imp_ents = base.CollectEntities(constants.ABAQUS, impactor, 'SHELL', True)
  area_ents = base.CollectEntities(constants.ABAQUS, area, 'SHELL', True)

  index = draw_mode.add_category(entities=imp_ents, label='Impactor', color=0xFF000000)
  index = draw_mode.add_category(entities=area_ents, label='Impact area', color=0x00FF0000)

  draw_mode.enable()
