from tkinter import ttk


class SearchView(ttk.Frame):
    def __init__(self, parent, data, search_engine, translations):
        super().__init__(parent)

        self.data = data
        self.search_engine = search_engine
        self.translations = translations

        self.search_types = [
            "symbol",
            "decimal",
            "hexadecimal",
            "binary",
            "octal",
            "unicode",
            "name"
        ]

        self.create_widgets()


    def create_widgets(self):
        search_frame = ttk.Frame(self)
        search_frame.pack(pady=10)

        self.search_label = ttk.Label(
            search_frame,
            text=self.translations.t("search_by")
        )

        self.search_label.grid(
            row=0,
            column=0,
            padx=5
        )

        self.search_type = ttk.Combobox(
            search_frame,
            values=self.get_search_type_names(),
            state="readonly"
        )

        self.search_type.grid(
            row=0,
            column=1,
            padx=5
        )

        self.search_type.current(0)

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


    def get_search_type_names(self):
        return [
            self.translations.t(search_type)
            for search_type in self.search_types
        ]


    def update_language(self):
        self.search_label.config(
            text=self.translations.t("search_by")
        )

        current_index = self.search_type.current()

        self.search_type.config(
            values=self.get_search_type_names()
        )

        self.search_type.current(current_index)


    def set_update_callback(self, method):
        self.update_table = method


    def search(self, event=None):
        query = self.search_entry.get()

        search_methods = {
            0: self.search_engine.by_symbol,
            1: self.search_engine.by_decimal,
            2: self.search_engine.by_hexadecimal,
            3: self.search_engine.by_binary,
            4: self.search_engine.by_octal,
            5: self.search_engine.by_unicode,
            6: self.search_engine.by_name
        }

        method = search_methods.get(self.search_type.current())

        if method:
            results = method(query)
            self.update_table(results)


    