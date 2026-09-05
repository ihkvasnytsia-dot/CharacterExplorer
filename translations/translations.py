class Translations:
    def __init__(self):
        self.current_language = "uk"

        self.translations = {
            "en": {
                # Window
                "title": "Character Explorer",

                # Tabs
                "catalog": "Catalog",
                "settings": "Settings",
                "about": "About",

                # Catalog tab
                "catalog_title": "Character Catalog",

                # Search type
                "search_by": "Search by:",
                "symbol": "Symbol",
                "decimal": "DEC",
                "hexadecimal": "HEX",
                "binary": "BIN",
                "octal": "OCT",
                "unicode": "Unicode",
                "name": "Name",

                # Table
                "code_column": "DEC",
                "symbol_column": "Symbol",
                "name_column": "Name",
                "hex_column": "HEX",
                "binary_column": "BIN",
                "octal_column": "OCT",
                "unicode_column": "Unicode",

                # Settings tab
                "settings_title": "Settings",

                # Language
                "language_label": "Language:",
                "ukrainian": "Ukrainian",
                "english": "English",

                # About tab
                "about_title": "About",

                # About program
                "about_description": (
                    "Character Explorer is a program for viewing "
                    "and exploring ASCII and Unicode characters.\n\n"
                    "The program allows you to view character codes "
                    "in decimal, hexadecimal, binary, and octal number systems.\n\n"
                    "You can also search for characters by code, "
                    "name, or the character itself.\n\n"
                    "The program is designed for learning, practice, "
                    "and exploring character encoding systems.\n\n"
                    "Version: 1.0"
                ),
            },
            
            "uk": {
                # Вікно
                "title": "Character Explorer",

                # Вкладки
                "catalog": "Каталог",
                "settings": "Налаштування",
                "about": "Про програму",

                # Вкладка каталог
                "catalog_title": "Каталог символів",
                
                # Тип пошуку
                "search_by": "Шукати за:",
                "symbol": "Символ",
                "decimal": "DEC",
                "hexadecimal": "HEX",
                "binary": "BIN",
                "octal": "OCT",
                "unicode": "Unicode",
                "name": "Назва",

                # Таблиця
                "code_column": "DEC",
                "symbol_column": "Символ",
                "name_column": "Назва",
                "hex_column": "HEX",
                "binary_column": "BIN",
                "octal_column": "OCT",
                "unicode_column": "Unicode",

                # Вкладка налаштування
                "settings_title": "Налаштування",

                # Мова
                "language_label": "Мова:",
                "ukrainian": "Українська",
                "english": "Англійська",

                # Вкладка про програму
                "about_title": "Про програму",
                
                # Про програму
                "about_description": (
                    "Character Explorer — це програма для перегляду "
                    "та дослідження символів ASCII і Unicode.\n\n"
                    "Програма дозволяє переглядати коди символів "
                    "у десятковій, шістнадцятковій, двійковій та "
                    "вісімковій системах числення.\n\n"
                    "Також можна виконувати пошук символів за кодом, "
                    "назвою або самим символом.\n\n"
                    "Програма призначена для навчання, практики "
                    "та дослідження систем кодування символів.\n\n"
                    "Версія: 1.0"
                ),
            },
        }

    def t(self, key, **kwargs):
        text = self.translations[self.current_language][key]
        return text.format(**kwargs)

    def change_language(self, language):
        self.current_language = language
