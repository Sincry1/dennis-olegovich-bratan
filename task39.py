#39
import re
from collections import Counter

text = "Ваш заданный текст здесь..."
words = re.findall(r"\w+", text.lower())
word_count = Counter(words)
for word, count in word_count.most_common():
    print(f"{word}: {count}")