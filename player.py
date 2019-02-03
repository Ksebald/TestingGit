from character import Character
class Player(Character):
    """
    The player class is where heros are made
    They inherit common traits from the Character class
    """

    def __init__(self, name, health, defense, str, int):
        Character.__init__(self, name, health, defense)
        self.str = str
        self.int = int
