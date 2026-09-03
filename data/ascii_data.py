
from data.ascii_character import ASCIICharacter


class ASCIIData:
    """Працює зі списком ASCII-символів."""

    def __init__(self):
        self.characters = self.create_characters()

    def create_characters(self):
        return [
            ASCIICharacter(code)
            for code in range(128)
        ]