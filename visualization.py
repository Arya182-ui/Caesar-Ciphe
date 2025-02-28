import matplotlib.pyplot as plt
from collections import Counter

def plot_frequency(text):
    counter = Counter(c.lower() for c in text if c.isalpha())
    plt.bar(counter.keys(), counter.values())
    plt.title("Character Frequency")
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.show()
