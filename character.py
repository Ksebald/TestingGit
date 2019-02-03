class Character():
    """
    This is the main parents class for creation of
    characters, be they player, NPC or monsters they
    shall all share common traits
    """

    def __init__(self, name, health, defense):
        """Constructor for Character"""
        self.name = name
        self.health = health
        self.defense = defense
