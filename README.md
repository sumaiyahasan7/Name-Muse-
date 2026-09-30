# Name Muse

**Discover the meaning and vibe behind a name.**

Name Muse is a small Python program. You type a name and it tells you what the name means. It also gives the name a matching **flower, color, gemstone and animal**, each with a short description of its personality. It comes in two versions: a **console version** and a **graphical (Tkinter) version**. Both share the same logic.

Author: Sumaiya Hasan, B.Tech CSE, Vellore Institute of Technology (VIT)

---

## Features

- Looks up the meaning of 12 built-in names (Sumaiya, Arjun, Priya, Ananya, Kabir, Meera, Aditya, Ishaan, Diya, Rohan, Zara, Aryan).
- For any other name, it builds a meaning from the name's first and last letters, for example *"A name that opens kind and closes admirable."*
- Gives every name a flower, color, gemstone and animal. The same name always gives the same result.
- Cleans the input by removing digits and symbols and fixing capitalisation.
- Handles empty input and input with no letters without crashing.
- GUI version: theme cards, a color swatch, a "Recent names" bar, and Reveal and Clear buttons.

## Concepts used

| Concept | Where it appears |
|---|---|
| Lists | The pools of flowers, colors, gemstones and animals |
| Tuples | Each pool entry is `(item, description)` |
| Dictionaries | Name meanings, letter traits, the profile, the color codes |
| Strings | Input cleaning, `.title()`, `.lower()`, formatted output |
| Abstract class (interface) | `NameAssociation` and, in the GUI, `NameMuseView` |
| Inheritance and polymorphism | `HashedAssociation` implements `NameAssociation`, and all themes are used through the same interface |
| Encapsulation | Each class keeps its own data (`pool`, `theme`, `icon`) |
| Loops and conditionals | Input loop, validation, fallback logic |
| MVC-style separation | Model, controller and view are separate classes in the GUI |

## Project structure

```
name-muse/
├── name_muse.py       # console version
├── name_muse_gui.py   # Tkinter GUI version
├── README.md
└── Project_Report.docx
```

## Requirements

- Python 3.8 or newer
- Nothing to install. Everything uses the standard library (`abc`, `tkinter`).

Tkinter comes with Python on Windows and macOS. On some Linux systems install it with `sudo apt install python3-tk`.

## How to run

```bash
# Console version
python name_muse.py

# GUI version
python name_muse_gui.py
```

In the console, type a name and press Enter. Type `quit`, `exit` or `q` to leave.
In the GUI, type a name and press Enter or click **Reveal**.

## Sample output (console)

```
Name Muse - discover the meaning and vibe behind a name.

Enter a name (or 'quit' to exit): Sumaiya

==========================================
  Sumaiya
==========================================
Meaning : one who is elevated, exalted 

Flower   : Lotus - rises clean out of the mud; resilience and purity
Color    : Coral - warm, sociable, full of energy
Gemstone : Pearl - understated, earned elegance
Animal   : Dolphin - playful intelligence
==========================================
```

## How it works

1. **Clean.** `clean_name()` keeps only letters and spaces.
2. **Meaning.** `get_meaning()` looks the name up in the `name_meanings` dictionary. If the name is not there, `fallback_meaning()` uses the traits of its first and last letters.
3. **Associations.** Each theme is a `HashedAssociation`. It adds up the character codes of the letters, `total = sum(ord(letter))`, and picks the item at position `total % len(pool)`. So the same name always gives the same flower, color, gemstone and animal.

Worked example for "Sumaiya": the letter codes add up to 761. `761 % 10 = 1` gives the flower at index 1 (Lotus). `761 % 8 = 1` gives Coral. `761 % 7 = 5` gives Pearl and Dolphin.

## Limitations

- The associations are for fun. They come from a simple formula and are not a real linguistic or astrological analysis.
- Only 12 names have real meanings. Every other name gets a letter-based description.
- Meanings are looked up by the full text, so "Sumaiya Hasan" will not match "sumaiya".
- Names that share the same letters (anagrams) get the same associations, because the formula only adds up letter codes.

## Future improvements

- A larger name-meaning database in a JSON file or an online source.
- Look up only the first name when a full name is typed.
- A "save my profile" or "compare two names" option.
- Handle "a" versus "an" in the fallback sentence.

## License

Made for academic purposes. Free to read, run and learn from.
