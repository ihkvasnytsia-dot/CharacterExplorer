from tkinter import ttk


class TableView(ttk.Frame):
    def __init__(self, parent, data, translations):
        super().__init__(parent)

        self.data = data
        self.translations = translations

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
       # Контейнер таблиці
        table_frame = ttk.Frame(self)

        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # Дозволяємо Treeview займати весь доступний простір
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)


        # ==================================================
        # Таблиця
        # ==================================================

        self.tree = ttk.Treeview(
            table_frame,
            columns=(
                "code",
                "symbol",
                "name",
                "hex",
                "binary",
                "octal",
                "unicode"
            ),
            show="headings"
        )


        # ==================================================
        # Заголовки
        # ==================================================

        self.tree.heading("code", text=self.translations.t("code_column"))
        self.tree.heading("symbol", text=self.translations.t("symbol_column"))
        self.tree.heading("name", text=self.translations.t("name_column"))
        self.tree.heading("hex", text=self.translations.t("hex_column"))
        self.tree.heading("binary", text=self.translations.t("binary_column"))
        self.tree.heading("octal", text=self.translations.t("octal_column"))
        self.tree.heading("unicode", text=self.translations.t("unicode_column"))


        # ==================================================
        # Ширина колонок
        # ==================================================

        self.tree.column(
            "code",
            width=60,
            minwidth=50,
            anchor="center"
        )

        self.tree.column(
            "symbol",
            width=80,
            minwidth=60,
            anchor="center"
        )

        self.tree.column(
            "name",
            width=250,
            minwidth=120,
            anchor="w"
        )

        self.tree.column(
            "hex",
            width=70,
            minwidth=60,
            anchor="center"
        )

        self.tree.column(
            "binary",
            width=100,
            minwidth=80,
            anchor="center"
        )

        self.tree.column(
            "octal",
            width=70,
            minwidth=60,
            anchor="center"
        )

        self.tree.column(
            "unicode",
            width=90,
            minwidth=70,
            anchor="center"
        )


        # ==================================================
        # Вертикальний scrollbar
        # ==================================================

        vertical_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )


        # ==================================================
        # Горизонтальний scrollbar
        # ==================================================

        horizontal_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )


        # ==================================================
        # Функція керування вертикальним scrollbar
        # ==================================================

        def vertical_scrollbar_set(first, last):

            first = float(first)
            last = float(last)

            # Якщо всі рядки видно
            if first <= 0.0 and last >= 1.0:
                vertical_scrollbar.grid_remove()

            # Якщо потрібна прокрутка
            else:
                vertical_scrollbar.grid(
                    row=0,
                    column=1,
                    sticky="ns"
                )

            vertical_scrollbar.set(first, last)


        # ==================================================
        # Функція керування горизонтальним scrollbar
        # ==================================================

        def horizontal_scrollbar_set(first, last):

            first = float(first)
            last = float(last)

            # Якщо всі колонки видно
            if first <= 0.0 and last >= 1.0:
                horizontal_scrollbar.grid_remove()

            # Якщо потрібна прокрутка
            else:
                horizontal_scrollbar.grid(
                    row=1,
                    column=0,
                    sticky="ew"
                )

            horizontal_scrollbar.set(first, last)


        # ==================================================
        # Підключаємо scrollbar до Treeview
        # ==================================================

        self.tree.configure(
            yscrollcommand=vertical_scrollbar_set,
            xscrollcommand=horizontal_scrollbar_set
        )


        # ==================================================
        # Розміщення
        # ==================================================

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        vertical_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        horizontal_scrollbar.grid(
            row=1,
            column=0,
            sticky="ew"
        )


    def update_language(self):
        self.tree.heading(
            "code",
            text=self.translations.t("code_column")
        )

        self.tree.heading(
            "symbol",
            text=self.translations.t("symbol_column")
        )

        self.tree.heading(
            "name",
            text=self.translations.t("name_column")
        )

        self.tree.heading(
            "hex",
            text=self.translations.t("hex_column")
        )

        self.tree.heading(
            "binary",
            text=self.translations.t("binary_column")
        )
        
        self.tree.heading(
            "octal",
            text=self.translations.t("octal_column")
        )

        self.tree.heading(
            "unicode",
            text=self.translations.t("unicode_column")
        )


    def load_data(self):
        for character in self.data.characters:
            self.add_character(character)


    def add_character(self, character):
        self.tree.insert(
            "",
            "end",
            values=(
                character.code,
                character.symbol,
                character.name,
                character.hex,
                character.binary,
                character.octal,
                character.unicode
            )
        )


    def update_data(self, data):

        # Очистити таблицю
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Додати нові дані
        for item in data:
            self.tree.insert(
                "",
                "end",
                values=(
                    item.code,
                    item.symbol,
                    item.name,
                    item.hex,
                    item.binary,
                    item.octal,
                    item.unicode
                )
            )

