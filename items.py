class Item:
    def __init__(self, name, description, hpRecovered, mpRecovered):
        self.name = name
        self.description = description
        self.hpRecovered = hpRecovered
        self.mpRecovered = mpRecovered


class potion(Item):
    pass

potion.name = "Potion"
potion.description = "its a fucking Potion"
potion.hpRecovered = 5
potion.mpRecovered = 0

