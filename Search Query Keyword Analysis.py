# Input sentence
query = "Buy mobile phone buy phone online"

# Step 1: Convert to lowercase
query = query.lower()

# Step 2: Remove punctuation
import string
query = query.translate(str.maketrans('', '', string.punctuation))

# Step 3: Split into words
words = query.split()

# Step 4: Count frequency of each keyword
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 5: Filter words appearing more than once
repeated_keywords = {}

for word, count in word_count.items():
    if count > 1:
        repeated_keywords[word] = count

# Step 6: Display result
print(repeated_keywords)
