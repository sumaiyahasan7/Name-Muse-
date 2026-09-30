# Problem Statement: Name Muse

## Background

A name is one of the first things people ask about each other, and many are curious about what their own name means. Most tools that answer this are either plain lookup lists or long web pages full of ads. They rarely make the result feel personal or fun to explore, and they usually fail when a name is not in their list.

## Problem

There is no simple, lightweight tool that lets a user type any name and immediately get:

1. a meaning for the name, even when the name is not in a database, and
2. a small, memorable "personality profile" that makes the result enjoyable to read and share.

Existing solutions depend on large databases or internet access, return nothing for unknown names, and do not give consistent results.

## Objective

Build **Name Muse**, a Python program that takes a name as input and returns its meaning together with a matching **flower, color, gemstone and animal**, each with a short description of its personality.

## Scope

**In scope**

- Meanings for 12 built-in names, with a letter-based fallback meaning for every other name.
- Deterministic associations: the same name always gives the same flower, color, gemstone and animal.
- Input cleaning (removes digits and symbols, fixes capitalisation) and safe handling of empty or invalid input.
- Two interfaces sharing the same logic: a **console version** and a **Tkinter GUI version** with theme cards, a color swatch, a recent-names bar, and Reveal and Clear buttons.

**Out of scope**

- Real linguistic, etymological or astrological analysis.
- Online lookups or a large name database.
- Storing user profiles between sessions.

## Proposed Solution

- Store name meanings in a dictionary and the four themes as lists of `(item, description)` tuples.
- For each theme, add up the character codes of the letters in the name and pick the item at position `total % len(pool)`.
- Use an abstract class (`NameAssociation`) with `HashedAssociation` implementing it, so every theme is used through one interface.
- In the GUI, separate model, controller and view (`NameMuseView`, `NameMuseController`) so the display can change without touching the logic.

## Expected Outcome

A dependency-free program (standard library only, Python 3.8+) that:

- returns a result for any valid name without crashing,
- gives repeatable output for the same input, and
- is easy to read, run and extend.

## Constraints and Limitations

- Associations are for fun and come from a simple formula, not real analysis.
- Only 12 names have true meanings; all others get a generated description.
- Full names such as "Sumaiya Hasan" do not match a single first-name entry.
- Names that are anagrams of each other receive the same associations.

## Future Work

- A larger name database (JSON file or online source).
- First-name extraction from full names.
- Save-profile and compare-two-names features.
- Correct "a" versus "an" in the fallback sentence.

---

**Author:** Sumaiya Hasan, B.Tech CSE, Vellore Institute of Technology (VIT)
