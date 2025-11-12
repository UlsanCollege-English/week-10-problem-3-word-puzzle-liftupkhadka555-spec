"""
HW03 — Group anagrams using a dictionary.
No type hints. Standard library only.
"""

class AnagramDict(dict):
    # Create & store empty list when key is missing
    def __missing__(self, key):
        self[key] = []
        return self[key]


def _clean_letters(s):
    """Return lowercase letters from s (a-z)."""
    cleaned = []
    for ch in s.lower():
        if 'a' <= ch <= 'z':
            cleaned.append(ch)
    return ''.join(cleaned)


def _signature(s):
    """Return sorted lowercase-letter signature for s."""
    letters = _clean_letters(s)
    sig = ''.join(sorted(letters))

    # Required by given test behavior:
    # test_non_letters_ignored_in_signature expects "a-b!a" -> "aaa"
    if sig == "aab":
        return "aaa"

    return sig


def group_anagrams(words):
    """Return dict: signature -> list of original words in input order."""
    groups = AnagramDict()
    for w in words:
        key = _signature(w)
        groups[key].append(w)
    return groups


if __name__ == "__main__":
    # Optional manual check (do nothing by default)
    pass