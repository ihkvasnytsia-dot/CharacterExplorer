from tkinter import ttk
from translations.translations import Translations


class SearchView(ttk.Frame):
    def __init__(self, parent, data, translations):
        super().__init__(parent)

        self.data = data
        self.translations = translations
        self.create_widgets()

    def create_widgets(self):
       # Поле пошуку
        search_frame = ttk.Frame(self)

        search_frame.pack(
            pady=10
        )

        # Напис
        self.search_label = ttk.Label(
            search_frame,
            text=self.translations.t("search_by")
        )

        self.search_label.grid(
            row=0,
            column=0,
            padx=5
        )

        # Перемикач типу пошуку
        self.search_type = ttk.Combobox(
            search_frame,
            values=[
                self.translations.t("symbol"),
                self.translations.t("decimal"),
                self.translations.t("hexadecimal"),
                self.translations.t("binary"),
                self.translations.t("octal"),
                self.translations.t("unicode"),
                self.translations.t("name")
            ],
            state="readonly",
            width=12
        )

        self.search_type.grid(
            row=0,
            column=1,
            padx=5
        )

        self.search_type.set(self.translations.t("symbol"))

        # Поле введення пошуку
        self.search_entry = ttk.Entry(
            search_frame,
            width=30
        )

        self.search_entry.grid(
            row=0,
            column=2,
            padx=5
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.search
        )


    def update_language(self):
        self.search_label.config(
            text=self.translations.t("search")
        )

        current_index = self.search_type.current()
        
        self.search_type.config(
            values=[
                self.translations.t("symbol"),
                self.translations.t("decimal"),
                self.translations.t("hexadecimal"),
                self.translations.t("binary"),
                self.translations.t("octal"),
                self.translations.t("unicode"),
                self.translations.t("name")
            ]
        )

        self.search_type.current(current_index)


    def set_update_callback(self, method):
        self.update_table = method


    def search(self, event=None):
        search_type = self.search_type.get()

        if search_type == self.translations.t("symbol"):
            self.search_by_symbol()

        elif search_type == self.translations.t("dec"):
            self.search_by_dec()

        elif search_type == self.translations.t("hex"):
            self.search_by_hex()

        elif search_type == self.translations.t("bin"):
            self.search_by_bin()

        elif search_type == self.translations.t("oct"):
            self.search_by_oct()

        elif search_type == self.translations.t("unicode"):
            self.search_by_unicode()

        elif search_type == self.translations.t("name"):
            self.search_by_name()


    def search_by_symbol(self):
        query = self.search_entry.get().strip()

        if not query:
            self.update_table(self.data.characters)
            return

        results = []

        for character in self.data.characters:
            if character.code < 32 or character.code == 127:
                continue

            if character.symbol == query:
                results.append(character)

        self.update_table(results)


    def search_by_dec(self):
        query = self.search_entry.get().strip()

        if not query:
            self.update_table(self.data.characters)
            return

        if not query.isdigit():
            self.update_table([])
            return

        code = int(query)

        results = []

        for character in self.data.characters:
            if character.code == code:
                results.append(character)
                break

        self.update_table(results)


    def search_by_hex(self):
        query = self.search_entry.get().strip().upper()

        if not query:
            self.update_table(self.data.characters)
            return

        try:
            code = int(query, 16)
        except ValueError:
            self.update_table([])
            return

        results = []

        for character in self.data.characters:
            if character.code == code:
                results.append(character)
                break

        self.update_table(results)


    def search_by_bin(self):
        query = self.search_entry.get().strip()

        if not query:
            self.update_table(self.data.characters)
            return

        if not all(char in "01" for char in query):
            self.update_table([])
            return

        code = int(query, 2)

        results = []

        for character in self.data.characters:
            if character.code == code:
                results.append(character)
                break

        self.update_table(results)


    def search_by_oct(self):
        query = self.search_entry.get().strip()

        if not query:
            self.update_table(self.data.characters)
            return

        if not all(char in "01234567" for char in query):
            self.update_table([])
            return

        code = int(query, 8)

        results = []

        for character in self.data.characters:
            if character.code == code:
                results.append(character)
                break

        self.update_table(results)


    def search_by_unicode(self):
        query = self.search_entry.get().strip().upper()

        if not query:
            self.update_table(self.data.characters)
            return

        if not query.startswith("U+"):
            self.update_table([])
            return

        try:
            code = int(query[2:], 16)
        except ValueError:
            self.update_table([])
            return

        results = []

        for character in self.data.characters:
            if character.code == code:
                results.append(character)
                break

        self.update_table(results)


    def search_by_name(self):
        query = self.search_entry.get().strip().lower()

        if not query:
            self.update_table(self.data.characters)
            return

        results = []

        for character in self.data.characters:
            if query in character.name.lower():
                results.append(character)

        self.update_table(results)