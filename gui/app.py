import tkinter as tk
from tkinter import ttk

from data.ascii_data import ASCIIData
from gui.views.about_view import AboutView
from gui.views.catalog_view.catalog_view import CatalogView
from gui.views.settings_view import SettingsView
from translations.translations import Translations
from logic.character_search import CharacterSearch


class App:
    def __init__(self):

        self.data = ASCIIData()
        self.translations = Translations()
        
        self.search_engine = CharacterSearch(
            self.data.characters
        )
        self.window = tk.Tk()

        self.window.title(self.translations.t("title"))

        width = 850
        height = 500

        # Розмір екрана
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Координати верхнього лівого кута
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.window.geometry(
            f"{width}x{height}+{x}+{y}"
        )

        self.window.minsize(400, 300)

        self.create_notebook()

    def create_notebook(self):
        self.notebook = ttk.Notebook(self.window)

        self.notebook.pack(
            fill="both",
            expand=True
        )

        # Вкладки
        self.catalog_view = CatalogView(self.notebook, self.data, self.search_engine, self.translations)
        self.settings_view = SettingsView(self.notebook, self.translations)
        self.about_view = AboutView(self.notebook, self.translations)

        self.settings_view.set_language_change_callback(
            self.change_language
        )

        # Додаємо вкладки
        self.notebook.add(
            self.catalog_view,
            text=self.translations.t("catalog")
        )

        self.notebook.add(
            self.settings_view,
            text=self.translations.t("settings")
        )

        self.notebook.add(
            self.about_view,
            text=self.translations.t("about")
        )


    def change_language(self, language):
        self.translations.change_language(language)
        self.update_language()

    
    def update_language(self):
        # Оновити назви вкладок
        self.notebook.tab(
            self.catalog_view,
            text=self.translations.t("catalog")
        )

        self.notebook.tab(
            self.settings_view,
            text=self.translations.t("settings")
        )

        self.notebook.tab(
            self.about_view,
            text=self.translations.t("about")
        )

        # Оновити вміст View
        self.catalog_view.update_language()
        self.settings_view.update_language()
        self.about_view.update_language()


    def run(self):
        self.window.mainloop()