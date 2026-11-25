#!/usr/bin/env python3
"""The Tired Dark Lord — a ~100-word villain monologue.

Entry for make.fun competition
u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.
"""
import os

MONOLOGUE = (
    "They call me the Dark Lord, as if the title came with rest. It did not. "
    "I have conquered kingdoms before breakfast and still the bards want a sequel. "
    "My generals send ravens at dawn; my enemies send assassins at noon; "
    "my accountant sends ledgers at midnight. "
    "I have a scheme, yes — a beautiful one, years in the making — "
    "but tonight I only want the fire low, the map folded, and one quiet hour "
    "where no one asks me to end the world before tea. "
    "The crown is heavy, the throne is cold, and the prophecy "
    "could wait until morning."
)

def main():
    print(MONOLOGUE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(MONOLOGUE + "\n")
    except OSError:
        pass

if __name__ == "__main__":
    main()
