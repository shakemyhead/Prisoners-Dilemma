__author__ = 'kummef'

import Game
import JesusPrisoner
import SatanPrisoner
import Hammurabbi

JC = JesusPrisoner.JesusPrisoner()
Lucifer = SatanPrisoner.SatanPrisoner()
Ham = Hammurabbi.Hammurabbi()



x = Game.Game(Lucifer, Ham)

x.playSet(100)

x.playSet(500)

