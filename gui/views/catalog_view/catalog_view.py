from tkinter import ttk

from gui.views.catalog_view.search_view import SearchView
from gui.views.catalog_view.table_view import TableView


class CatalogView(ttk.Frame):
    def __init__(self, parent, data, search_engine, translations):
        super().__init__(parent)
        
        self.data = data
        self.search_engine = search_engine    
        self.translations = translations

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        self.title = ttk.Label(
            self,
            text=self.translations.t("catalog_title"),
            font=("Arial", 18)
        )

        self.title.pack(pady=10)
        
        # # Верхня частина — пошук
        self.search_view = SearchView(
            self, self.data, self.search_engine, self.translations
            )

        self.search_view.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # # Нижня частина — таблиця
        self.table_view = TableView(self, self.data, self.translations)

        self.table_view.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        self.search_view.set_update_callback(
            self.table_view.update_data
            )

    def update_language(self):
        
        # Оновити власний заголовок
        self.title.config(
            text=self.translations.t("catalog_title")
        )
        
        self.search_view.update_language()
        self.table_view.update_language()
