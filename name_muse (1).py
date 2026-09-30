from abc import ABC, abstractmethod


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


class NameAssociation(ABC):
    @abstractmethod
    def associate(self, name):
        pass


class HashedAssociation(NameAssociation):
    def __init__(self, pool):
        self.pool = pool

    def associate(self, name):
        total = 0
        for ch in name.lower():
            if ch.isalpha():
                total += ord(ch)
        index = total % len(self.pool)
        return self.pool[index]


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

    themes = {
        "Flower": HashedAssociation(flowers),
        "Color": HashedAssociation(colors),
        "Gemstone": HashedAssociation(gemstones),
        "Animal": HashedAssociation(animals),
    }

    associations = {}
    for theme in themes:
        associations[theme] = themes[theme].associate(name)

    profile = {
        "name": name.title(),
        "meaning": get_meaning(name),
        "associations": associations,
    }
    return profile


def print_profile(profile):
    print("\n" + "=" * 42)
    print("  " + profile["name"])
    print("=" * 42)
    print("Meaning :", profile["meaning"], "\n")

    for theme in profile["associations"]:
        item, description = profile["associations"][theme]
        print(f"{theme:<9}: {item} - {description}")
    print("=" * 42 + "\n")


def main():
    print("Name Muse - discover the meaning and vibe behind a name.")
    while True:
        raw = input("\nEnter a name (or 'quit' to exit): ")

        if raw.strip().lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        if raw.strip() == "":
            print("Please type a name.")
            continue

        profile = build_profile(raw)
        print_profile(profile)


main()
