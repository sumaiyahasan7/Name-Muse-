
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


# ===============================================================
# DATA
# ===============================================================

name_meanings = {
    "sumaiya": "one who is elevated, exalted",
    "arjun": "bright, shining, white",
    "priya": "beloved, dear one",
    "ananya": "unique, incomparable",
    "kabir": "great, powerful",
    "meera": "devoted, prosperous",
    "aditya": "the sun",
    "ishaan": "the sun, protector of the earth",
    "diya": "lamp, light",
    "rohan": "ascending, rising",
    "zara": "blooming flower, princess",
    "aryan": "noble one",
}

flowers = [
    ("Jasmine", "delicate, fragrant, a symbol of grace"),
    ("Lotus", "rises clean out of the mud; resilience and purity"),
    ("Marigold", "warm, bright, tied to celebration"),
    ("Orchid", "rare, refined, a little mysterious"),
    ("Sunflower", "always turning toward the light"),
    ("Tulip", "simple elegance, a fresh start"),
    ("Lavender", "calm, steady, quietly confident"),
    ("Rose", "classic warmth, depth under the petals"),
    ("Hibiscus", "bold color, short bloom, lived fully"),
    ("Daffodil", "new beginnings, the first sign of spring"),
]

colors = [
    ("Indigo", "deep, thoughtful, a little mysterious"),
    ("Coral", "warm, sociable, full of energy"),
    ("Emerald", "grounded, growth-minded"),
    ("Amber", "glowing, comforting, old-soul"),
    ("Teal", "balanced between calm and bold"),
    ("Crimson", "intense, passionate, hard to ignore"),
    ("Gold", "confident, a little regal"),
    ("Lilac", "gentle, soft-spoken strength"),
]

gemstones = [
    ("Sapphire", "wisdom and loyalty"),
    ("Moonstone", "intuition, quiet change"),
    ("Garnet", "steady passion, protection"),
    ("Topaz", "clarity of purpose"),
    ("Amethyst", "calm under pressure"),
    ("Pearl", "understated, earned elegance"),
    ("Opal", "many-sided, hard to define in one word"),
]

animals = [
    ("Fox", "clever, adaptable, quick on its feet"),
    ("Swan", "graceful, calm on the surface"),
    ("Falcon", "focused, sharp, aims high"),
    ("Deer", "gentle, alert, quietly strong"),
    ("Owl", "observant, wise beyond the noise"),
    ("Dolphin", "playful intelligence"),
    ("Tiger", "bold, self-assured, hard to overlook"),
]

letter_traits = {
    "a": "admirable", "b": "bold", "c": "creative", "d": "determined",
    "e": "energetic", "f": "faithful", "g": "graceful", "h": "honest",
    "i": "imaginative", "j": "joyful", "k": "kind", "l": "lively",
    "m": "meticulous", "n": "noble", "o": "optimistic", "p": "patient",
    "q": "quick-witted", "r": "resilient", "s": "spirited", "t": "thoughtful",
    "u": "unique", "v": "vibrant", "w": "warm", "x": "extraordinary",
    "y": "youthful", "z": "zealous",
}

# Used only to paint a small swatch in the GUI for the Color theme
color_hex = {
    "Indigo": "#4B0082", "Coral": "#FF7F50", "Emerald": "#2E9E5B",
    "Amber": "#FFBF00", "Teal": "#008080", "Crimson": "#DC143C",
    "Gold": "#E6B800", "Lilac": "#C8A2C8",
}


# ===============================================================
# MODEL: interface for associations (same idea as your original)
# ===============================================================

class NameAssociation(ABC):
    """Interface: every theme must say its name and pick an item for a name."""

    @property
    @abstractmethod
    def theme(self):
        pass

    @property
    @abstractmethod
    def icon(self):
        pass

    @abstractmethod
    def associate(self, name):
        pass


class HashedAssociation(NameAssociation):
    def __init__(self, theme, icon, pool):
        self._theme = theme
        self._icon = icon
        self.pool = pool

    @property
    def theme(self):
        return self._theme

    @property
    def icon(self):
        return self._icon

    def associate(self, name):
        total = 0
        for ch in name.lower():
            if ch.isalpha():
                total += ord(ch)
        index = total % len(self.pool)
        return self.pool[index]


ASSOCIATIONS = [
    HashedAssociation("Flower", "🌸", flowers),
    HashedAssociation("Color", "🎨", colors),
    HashedAssociation("Gemstone", "💎", gemstones),
    HashedAssociation("Animal", "🦊", animals),
]


def clean_name(raw):
    cleaned = ""
    for ch in raw.strip():
        if ch.isalpha() or ch.isspace():
            cleaned += ch
    return cleaned


def get_meaning(name):
    key = name.lower()
    if key in name_meanings:
        return name_meanings[key]
    return fallback_meaning(name)


def fallback_meaning(name):
    letters = [ch.lower() for ch in name if ch.isalpha()]
    if len(letters) == 0:
        return "A name yet to reveal its story."

    first = letter_traits.get(letters[0], "unique")
    last = letter_traits.get(letters[-1], "memorable")

    if first == last:
        return "A name that carries a " + first + " spirit through and through."
    return "A name that opens " + first + " and closes " + last + "."


def build_profile(raw_name):
    name = clean_name(raw_name)

    results = []
    for association in ASSOCIATIONS:
        item, description = association.associate(name)
        results.append({
            "theme": association.theme,
            "icon": association.icon,
            "item": item,
            "description": description,
        })

    return {
        "name": name.title(),
        "meaning": get_meaning(name),
        "results": results,
    }


# ===============================================================
# VIEW: interface for anything that can display Name Muse
# ===============================================================

class NameMuseView(ABC):
    @abstractmethod
    def show_profile(self, profile):
        pass

    @abstractmethod
    def show_error(self, message):
        pass

    @abstractmethod
    def show_history(self, names):
        pass

    @abstractmethod
    def reset(self):
        pass


# ===============================================================
# CONTROLLER: connects the model to whichever view is used
# ===============================================================

class NameMuseController:
    MAX_HISTORY = 6

    def __init__(self, view):
        self.view = view
        self.history = []

    def submit(self, raw):
        if raw.strip() == "":
            self.view.show_error("Please type a name.")
            return

        if clean_name(raw).strip() == "":
            self.view.show_error("A name can only contain letters.")
            return

        profile = build_profile(raw)
        self.view.show_profile(profile)
        self.remember(profile["name"])

    def remember(self, name):
        if name in self.history:
            self.history.remove(name)
        self.history.insert(0, name)
        self.history = self.history[:self.MAX_HISTORY]
        self.view.show_history(self.history)

    def clear(self):
        self.view.reset()


# ===============================================================
# TKINTER VIEW
# ===============================================================

BG = "#f7f3ee"
CARD = "#ffffff"
ACCENT = "#6b4ea0"
TEXT = "#2b2b2b"
MUTED = "#7a7a7a"
BORDER = "#e6dfd3"
ERROR = "#b3261e"

THEME_STRIPES = {
    "Flower": "#e58fb0",
    "Color": "#5fa8d3",
    "Gemstone": "#8e7cc3",
    "Animal": "#e0a458",
}


class TkNameMuseView(NameMuseView):
    def __init__(self, root):
        self.root = root
        self.controller = None
        self.theme_cards = {}

        root.title("Name Muse")
        root.geometry("620x720")
        root.minsize(560, 660)
        root.configure(bg=BG)

        self.build_header()
        self.build_input()
        self.build_history_bar()
        self.build_result_area()

    def set_controller(self, controller):
        self.controller = controller

    # ----- building the layout -----

    def build_header(self):
        tk.Label(
            self.root, text="Name Muse", font=("Georgia", 30, "bold"),
            bg=BG, fg=ACCENT,
        ).pack(pady=(22, 0))
        tk.Label(
            self.root, text="discover the meaning and vibe behind a name",
            font=("Helvetica", 11), bg=BG, fg=MUTED,
        ).pack(pady=(0, 14))

    def build_input(self):
        row = tk.Frame(self.root, bg=BG)
        row.pack(padx=32, fill="x")

        self.name_var = tk.StringVar()
        self.entry = ttk.Entry(row, textvariable=self.name_var, font=("Helvetica", 14))
        self.entry.pack(side="left", fill="x", expand=True, ipady=5)
        self.entry.focus()
        self.entry.bind("<Return>", lambda event: self.controller.submit(self.name_var.get()))

        ttk.Button(
            row, text="Reveal",
            command=lambda: self.controller.submit(self.name_var.get()),
        ).pack(side="left", padx=(8, 0))
        ttk.Button(row, text="Clear", command=lambda: self.controller.clear()).pack(
            side="left", padx=(6, 0)
        )

        self.error_label = tk.Label(
            self.root, text="", font=("Helvetica", 10), bg=BG, fg=ERROR
        )
        self.error_label.pack(pady=(6, 0))

    def build_history_bar(self):
        self.history_frame = tk.Frame(self.root, bg=BG)
        self.history_frame.pack(padx=32, fill="x")

    def build_result_area(self):
        self.result = tk.Frame(
            self.root, bg=CARD, highlightthickness=1, highlightbackground=BORDER
        )
        self.result.pack(padx=32, pady=(10, 20), fill="both", expand=True)

        self.name_label = tk.Label(
            self.result, text="", font=("Georgia", 24, "bold"), bg=CARD, fg=TEXT
        )
        self.name_label.pack(pady=(18, 2))

        self.meaning_label = tk.Label(
            self.result, text="Type a name above and press Reveal.",
            font=("Helvetica", 11, "italic"), bg=CARD, fg=MUTED,
            wraplength=480, justify="center",
        )
        self.meaning_label.pack(padx=20, pady=(0, 14))

        grid = tk.Frame(self.result, bg=CARD)
        grid.pack(padx=18, pady=(0, 18), fill="both", expand=True)
        grid.columnconfigure(0, weight=1, uniform="col")
        grid.columnconfigure(1, weight=1, uniform="col")
        grid.rowconfigure(0, weight=1, uniform="row")
        grid.rowconfigure(1, weight=1, uniform="row")

        # One card per association, built from the same interface
        for i, association in enumerate(ASSOCIATIONS):
            r, c = divmod(i, 2)
            self.theme_cards[association.theme] = self.make_theme_card(grid, association, r, c)

    def make_theme_card(self, parent, association, row, col):
        card = tk.Frame(
            parent, bg=CARD, highlightthickness=1, highlightbackground=BORDER
        )
        card.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

        tk.Frame(card, bg=THEME_STRIPES.get(association.theme, ACCENT), height=5).pack(fill="x")

        tk.Label(
            card, text=association.icon + "  " + association.theme.upper(),
            font=("Helvetica", 9, "bold"), bg=CARD, fg=MUTED, anchor="w",
        ).pack(fill="x", padx=12, pady=(10, 0))

        item_row = tk.Frame(card, bg=CARD)
        item_row.pack(fill="x", padx=12, pady=(2, 0))

        swatch = tk.Frame(item_row, bg=CARD, width=16, height=16)
        item_label = tk.Label(
            item_row, text="-", font=("Helvetica", 16, "bold"),
            bg=CARD, fg=TEXT, anchor="w",
        )
        item_label.pack(side="left")

        desc_label = tk.Label(
            card, text="", font=("Helvetica", 10), bg=CARD, fg=MUTED,
            anchor="nw", justify="left", wraplength=210,
        )
        desc_label.pack(fill="both", expand=True, padx=12, pady=(2, 12))

        return {"swatch": swatch, "item": item_label, "desc": desc_label}

    # ----- NameMuseView interface -----

    def show_profile(self, profile):
        self.error_label.config(text="")
        self.name_label.config(text=profile["name"])
        self.meaning_label.config(
            text=profile["meaning"], fg=TEXT, font=("Helvetica", 12, "italic")
        )

        for result in profile["results"]:
            card = self.theme_cards[result["theme"]]
            card["item"].config(text=result["item"])
            card["desc"].config(text=result["description"])

            # Only the Color theme has a swatch colour to show
            if result["theme"] == "Color" and result["item"] in color_hex:
                card["swatch"].config(bg=color_hex[result["item"]])
                card["swatch"].pack(side="left", padx=(0, 8), before=card["item"])
            else:
                card["swatch"].pack_forget()

    def show_error(self, message):
        self.error_label.config(text=message)

    def show_history(self, names):
        for widget in self.history_frame.winfo_children():
            widget.destroy()

        if not names:
            return

        tk.Label(
            self.history_frame, text="Recent:", font=("Helvetica", 9),
            bg=BG, fg=MUTED,
        ).pack(side="left", padx=(0, 6))

        for name in names:
            ttk.Button(
                self.history_frame, text=name, width=max(6, len(name) + 1),
                command=lambda n=name: self.use_history(n),
            ).pack(side="left", padx=2)

    def reset(self):
        self.name_var.set("")
        self.error_label.config(text="")
        self.name_label.config(text="")
        self.meaning_label.config(
            text="Type a name above and press Reveal.",
            fg=MUTED, font=("Helvetica", 11, "italic"),
        )
        for card in self.theme_cards.values():
            card["item"].config(text="-")
            card["desc"].config(text="")
            card["swatch"].pack_forget()
        self.entry.focus()

    # ----- small helper -----

    def use_history(self, name):
        self.name_var.set(name)
        self.controller.submit(name)


def main():
    root = tk.Tk()
    view = TkNameMuseView(root)
    controller = NameMuseController(view)
    view.set_controller(controller)
    root.mainloop()


if __name__ == "__main__":
    main()
