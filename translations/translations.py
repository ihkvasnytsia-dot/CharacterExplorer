class Translations:
    def __init__(self):
        self.current_language = "uk"

        self.translations = {
            "en": {
                # General
                "title": "Character Explorer",
                "catalog_title": "Character Catalog",
                "search": "Search",
                "clear": "Clear",
                
                # Language
                "language_label": "Language:",
                "ukrainian": "Ukrainian",
                "english": "English",
                
                # Theme
                "theme_label": "Theme:",
                "system": "System",
                "light": "Light",
                "dark": "Dark",
                
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
                "code": "DEC",
                "symbol_column": "Symbol",
                "name_column": "Name",
                "hex_column": "HEX",
                "binary_column": "BIN",
                "octal_column": "OCT",
                "unicode_column": "Unicode",
                
                # Messages
                "invalid_search": "Invalid search query",
                "not_found": "Character not found",
                "empty_search": "Enter a value to search",
                
                # Control characters
                "control_character": "Control character",
                "printable_character": "Printable character",
                
                # Tabs
                "catalog": "Catalog",
                "settings": "Settings",
                "about": "About",
                
                # About
                "about_description": (
                    "Character Explorer is an application for viewing "
                    "and exploring ASCII and Unicode characters.\n\n"
                    "The application allows you to view character codes "
                    "in decimal, hexadecimal, binary and octal formats.\n\n"
                    "You can also search for characters by code, "
                    "name or character itself.\n\n"
                    "The application is designed for learning, practicing "
                    "and exploring character encoding systems.\n\n"
                    "Version: 1.0"
                ),
            },
            "uk": {
                # Загальне
                "title": "Character Explorer",
                "catalog_title": "Каталог символів",
                "search": "Пошук",
                "clear": "Очистити",
                
                # Мова
                "language_label": "Мова:",
                "ukrainian": "Українська",
                "english": "Англійська",
                
                # тема
                "theme_label": "Тема:",
                "system": "Системна",
                "light": "Світла",
                "dark": "Темна",
                
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
                "code": "DEC",
                "symbol_column": "Символ",
                "name_column": "Назва",
                "hex_column": "HEX",
                "binary_column": "BIN",
                "octal_column": "OCT",
                "unicode_column": "Unicode",
                
                # Повідомлення
                "invalid_search": "Некоректний пошуковий запит",
                "not_found": "Символ не знайдено",
                "empty_search": "Введіть значення для пошуку",
                
                # Керуючі символи
                "control_character": "Керуючий символ",
                "printable_character": "Друкований символ",
                
                # Вкладки
                "catalog": "Каталог",
                "settings": "Налаштування",
                "about": "Про програму",
                
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
