"""
Name: Ei Htoo Khaing
Student Number: 115400244
"""

import string

def preprocess_text(text):
    #lowercase, remove punctuation, split into words
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words

def count_word_frequencies(words):
    #Return a dictionary mapping words → frequency.
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def count_bigram_frequencies(words):
    #Return a dictionary mapping bigrams → frequency.
    bigram_freq = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_freq:
            bigram_freq[bigram] += 1
        else:
            bigram_freq[bigram] = 1
    return bigram_freq


def print_top_words(freq, n=20):
    print("\nTop 20 Word Frequencies")
    print("{:<15} {}".format("Word", "Frequency"))
    print("-" * 25)

    for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]:
        print(f"{word:<15} {count}")


def print_top_bigrams(bigram_freq, n=10):
    print("\nTop 10 Bigrams")
    print("{:<20} {}".format("Bigram", "Frequency"))
    print("-" * 35)

    for (w1, w2), count in sorted(bigram_freq.items(), key=lambda x: x[1], reverse=True)[:n]:
        bigram = f"{w1} {w2}"
        print(f"{bigram:<20} {count}")


def main():
    # Load the text file
    with open("adventures_of_huckleberry_finn.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Preprocess
    words = preprocess_text(text)

    # Word frequencies
    word_freq = count_word_frequencies(words)

    # Print top 20 words
    print_top_words(word_freq)

    # BONUS: Bigram frequencies
    bigram_freq = count_bigram_frequencies(words)

    # Print top 10 bigrams
    print_top_bigrams(bigram_freq)


if __name__ == "__main__":
    main()
