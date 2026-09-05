class CharacterSearch:
    def __init__(self, characters):
        self.characters = characters


    def by_symbol(self, query):
        query = query.strip()

        if not query:
            return self.characters

        results = []

        for character in self.characters:
            if character.code < 32 or character.code == 127:
                continue

            if character.symbol == query:
                results.append(character)

        return results


    def by_decimal(self, query):
        query = query.strip()

        if not query:
            return self.characters

        if not query.isdigit():
            return []

        code = int(query)

        for character in self.characters:
            if character.code == code:
                return [character]

        return []


    def by_hexadecimal(self, query):
        query = query.strip().upper()

        if not query:
            return self.characters

        try:
            code = int(query, 16)
        except ValueError:
            return []

        for character in self.characters:
            if character.code == code:
                return [character]

        return []


    def by_binary(self, query):
        query = query.strip()

        if not query:
            return self.characters

        if not all(char in "01" for char in query):
            return []

        code = int(query, 2)

        for character in self.characters:
            if character.code == code:
                return [character]

        return []


    def by_octal(self, query):
        query = query.strip()

        if not query:
            return self.characters

        if not all(char in "01234567" for char in query):
            return []

        code = int(query, 8)

        for character in self.characters:
            if character.code == code:
                return [character]

        return []


    def by_unicode(self, query):
        query = query.strip().upper()

        if not query:
            return self.characters

        if not query.startswith("U+"):
            return []

        try:
            code = int(query[2:], 16)
        except ValueError:
            return []

        for character in self.characters:
            if character.code == code:
                return [character]

        return []


    def by_name(self, query):
        query = query.strip().lower()

        if not query:
            return self.characters

        results = []

        for character in self.characters:
            if query in character.name.lower():
                results.append(character)

        return results