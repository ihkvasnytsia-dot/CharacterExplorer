from tkinter import ttk


class SettingsView(ttk.Frame):
    def __init__(self, parent, translations):
        super().__init__(parent)

        self.translations = translations

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        self.title = ttk.Label(
            self,
            text=self.translations.t("settings"),
            font=("Arial", 18)
        )

        self.title.pack(
            pady=10
        )

        # Мова
        self.language_label = ttk.Label(
            self,
            text=self.translations.t("language_label")
        )

        self.language_label.pack(
            anchor="w",
            padx=20,
            pady=(10, 5)
        )

        self.language_combobox = ttk.Combobox(
            self,
            state="readonly"
        )

        self.language_combobox.pack(
            anchor="w",
            padx=20
        )

        self.update_language_combobox()

        # Тема
        self.theme_label = ttk.Label(
            self,
            text=self.translations.t("theme_label")
        )

        self.theme_label.pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.theme_combobox = ttk.Combobox(
            self,
            values=[
                self.translations.t("system"),
                self.translations.t("light"),
                self.translations.t("dark")
            ],
            state="readonly"
        )

        self.theme_combobox.pack(
            anchor="w",
            padx=20
        )

        self.theme_combobox.current(0)


    def update_language_combobox(self):

        self.languages = {
            "en": self.translations.t("english"),
            "uk": self.translations.t("ukrainian")
        }

        sorted_languages = sorted(
            self.languages.items(),
            key=lambda item: item[1]
        )

        self.language_combobox.config(
            values=[name for code, name in sorted_languages]
        )

        for index, (code, name) in enumerate(sorted_languages):
            if code == self.translations.current_language:
                self.language_combobox.current(index)
                break


    def set_language_change_callback(self, callback):
        self.language_callback = callback

        self.language_combobox.bind(
            "<<ComboboxSelected>>",
            self.on_language_change
        )


    def on_language_change(self, event=None):
        selected_name = self.language_combobox.get()

        for code, name in self.languages.items():
            if name == selected_name:
                self.language_callback(code)
                break


    def update_language(self):
        # Оновити власний заголовок
        self.title.config(
            text=self.translations.t("settings")
        )

        # Оновити мітку мови
        self.language_label.config(
            text=self.translations.t("language_label")
        )

        # Оновити значення комбобоксу мови
        self.update_language_combobox()

        # Оновити мітку теми
        self.theme_label.config(
            text=self.translations.t("theme_label")
        )

        # Оновити значення комбобоксу теми
        current_index = self.theme_combobox.current()
        
        self.theme_combobox.config(
            values=[
                self.translations.t("system"),
                self.translations.t("light"),
                self.translations.t("dark")
            ]
        )

        self.theme_combobox.current(current_index)