from classes import Herovalid
from typing import List 
import csv

HEROES : List[Herovalid]=[
    Herovalid(
        id=1,
        name="Aether",
        title="Le Voyageur",
        power="Énergie élémentaire",
        role="DPS",
        image="/images/heroes/aether.jpg",
        rarity=5,
        active=True
    ),

    Herovalid(
        id=2,
        name="Lumine",
        title="La Voyageuse",
        power="Énergie élémentaire",
        role="DPS",
        image="/images/heroes/lumine.jpg",
        rarity=5,
        active=True
    ),

    Herovalid(
        id=3,
        name="Diluc",
        title="Le Chevalier des Ténèbres",
        power="Pyro",
        role="DPS",
        image="/images/heroes/diluc.jpg",
        rarity=5,
        active=True
    ),

    Herovalid(
        id=4,
        name="Jean",
        title="La Grande Maîtresse",
        power="Anémo",
        role="Support",
        image="/images/heroes/jean.jpg",
        rarity=5,
        active=True
    ),

    Herovalid(
        id=5,
        name="Kaeya",
        title="Le Capitaine de Cavalerie",
        power="Cryo",
        role="Support",
        image="/images/heroes/kaeya.jpg",
        rarity=4,
        active=True
    ),

    Herovalid(
        id=6,
        name="Lisa",
        title="La Sorcière de la Foudre",
        power="Électro",
        role="DPS",
        image="/images/heroes/lisa.jpg",
        rarity=4,
        active=True
    ),

    Herovalid(
        id=7,
        name="Amber",
        title="La Championne de Planage",
        power="Pyro",
        role="DPS",
        image="/images/heroes/amber.jpg",
        rarity=4,
        active=True
    ),

    Herovalid(
        id=8,
        name="Barbara",
        title="L'Idole de Mondstadt",
        power="Hydro",
        role="Soigneur",
        image="/images/heroes/barbara.jpg",
        rarity=4,
        active=True
    ),

    Herovalid(
        id=9,
        name="Xiangling",
        title="La Maîtresse du Feu",
        power="Pyro",
        role="DPS",
        image="/images/heroes/xiangling.jpg",
        rarity=4,
        active=True
    ),

    Herovalid(
        id=10,
        name="Zhongli",
        title="Le Seigneur de la Pierre",
        power="Géo",
        role="Support",
        image="/images/heroes/zhongli.jpg",
        rarity=5,
        active=True
    ),

    Herovalid(
        id=11,
        name="Raiden",
        title="L'Archonte Électro",
        power="Électro",
        role="DPS",
        image="/images/heroes/raiden.jpg",
        rarity=5,
        active=True
    ),

    Herovalid(
        id=12,
        name="Nahida",
        title="La Petite Souveraine",
        power="Dendro",
        role="Support",
        image="/images/heroes/nahida.jpg",
        rarity=5,
        active=True
    ),

    Herovalid(
        id=13,
        name="Hu Tao",
        title="La Directrice des Pompes Funèbres",
        power="Pyro",
        role="DPS",
        image="/images/heroes/hutao.jpg",
        rarity=5,
        active=True
    ),

    Herovalid(
        id=14,
        name="Kazuha",
        title="Le Samouraï Errant",
        power="Anémo",
        role="Support",
        image="/images/heroes/kazuha.jpg",
        rarity=5,
        active=True
    ),

    Herovalid(
        id=15,
        name="Furina",
        title="L'Archonte Hydro",
        power="Hydro",
        role="Support",
        image="/images/heroes/furina.jpg",
        rarity=5,
        active=True
    )
]


with open("heroes.csv" , "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id","name","title","power","role","image","rarity","active"])

    for hero in HEROES:
        writer.writerow([hero.id,hero.name,hero.title,hero.power,hero.role,hero.image,hero.rarity,hero.active])