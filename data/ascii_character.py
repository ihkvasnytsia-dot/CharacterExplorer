class ASCIICharacter:
    """Зберігає інформацію про один ASCII-символ."""

    CONTROL_NAMES = {
        0: "NUL — Null",
        1: "SOH — Start of Heading",
        2: "STX — Start of Text",
        3: "ETX — End of Text",
        4: "EOT — End of Transmission",
        5: "ENQ — Enquiry",
        6: "ACK — Acknowledge",
        7: "BEL — Bell",
        8: "BS — Backspace",
        9: "TAB — Horizontal Tab",
        10: "LF — Line Feed",
        11: "VT — Vertical Tab",
        12: "FF — Form Feed",
        13: "CR — Carriage Return",
        14: "SO — Shift Out",
        15: "SI — Shift In",
        16: "DLE — Data Link Escape",
        17: "DC1 — Device Control 1",
        18: "DC2 — Device Control 2",
        19: "DC3 — Device Control 3",
        20: "DC4 — Device Control 4",
        21: "NAK — Negative Acknowledge",
        22: "SYN — Synchronous Idle",
        23: "ETB — End of Transmission Block",
        24: "CAN — Cancel",
        25: "EM — End of Medium",
        26: "SUB — Substitute",
        27: "ESC — Escape",
        28: "FS — File Separator",
        29: "GS — Group Separator",
        30: "RS — Record Separator",
        31: "US — Unit Separator",
        127: "DEL — Delete"
    }

    def __init__(self, code):
        self.code = code
        self.symbol = self.get_symbol()
        self.name = self.get_name()

        self.hex = f"{code:02X}"
        self.binary = f"{code:08b}"
        self.octal = f"{code:03o}"
        self.unicode = f"U+{code:04X}"

    def get_symbol(self):
        if self.code in self.CONTROL_NAMES:
            return f"\\x{self.code:02X}"

        if self.code == 32:
            return "SPACE"

        return chr(self.code)

    def get_name(self):
        if self.code in self.CONTROL_NAMES:
            return self.CONTROL_NAMES[self.code]

        if self.code == 32:
            return "Space — Пробіл"

        return "Printable character"