from tkinter import ttk


class AboutView(ttk.Frame):
    def __init__(self, parent, translations):
        super().__init__(parent)

        self.translations = translations
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        self.title = ttk.Label(
            self,
            text=self.translations.t("about"),
            font=("Arial", 18)
        )

        self.title.pack(
            pady=10
        )

        # Опис
        self.description = ttk.Label(
            self,
            text=self.translations.t("about_description"),
            justify="left",
            anchor="w"
        )

        self.description.pack(
            fill="x",
            padx=30,
            pady=20
        )

        self.bind(
            "<Configure>",
            lambda event: self.description.configure(
                wraplength=max(1, event.width - 60)
            )
        )

    def update_language(self):
        self.title.config(
            text=self.translations.t("about")
        )
        
        self.description.config(
            text=self.translations.t("about_description")
        )

