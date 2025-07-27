def word_count(text):
    """Count the number of words in the given text."""
    return len(text.split())


def character_count(text):
    """Count the number of characters in the given text."""
    return len(text)


def avg_word_length(text):
    """Calculate the average length of words in the given text."""
    words = text.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)


if __name__ == "__main__":
    sample = "Git is amazing for version control!"
    print(f"Text: '{sample}'")
    print(f"Words: {word_count(sample)}")
    print(f"Characters: {character_count(sample)}")
    print(f"Average word length: {avg_word_length(sample):.2f}")
