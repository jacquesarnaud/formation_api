
class Herovalid():
    id: int
    name: str
    title: str
    power: str
    role: str
    image: str
    rarity: int
    active: bool

    def __init__(self,id,name,title,power,role,image,rarity,active):
        self.id = id
        self.name = name
        self.title = title
        self.power = power
        self.role = role
        self.image = image
        self.rarity =rarity
        self.active =active