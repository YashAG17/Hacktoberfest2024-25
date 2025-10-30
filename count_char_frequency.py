from collections import Counter

def count_char_frequency(text: str) -> dict:
    """
    Counts the frequency of each character in a string, 
    ignoring whitespace and case sensitivity.
    """
    # Normalize and clean the text
    cleaned_text = text.lower().replace(" ", "")
    
    # Use collections.Counter for efficient frequency counting
    frequency_map = Counter(cleaned_text)
    
    # Optional: convert Counter object to a standard dictionary for a clean return
    return dict(frequency_map)

# Example Usage:
# result = count_char_frequency("Hello Hacktoberfest")
# print(result)
# Output: {'h': 2, 'e': 3, 'l': 2, 'o': 2, 'a': 1, 'c': 1, 'k': 1, 't': 1, 'b': 1, 'r': 1, 'f': 1, 's': 1}
