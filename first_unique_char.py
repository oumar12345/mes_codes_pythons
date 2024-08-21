from collections import Counter
def first_unique_characters(s):
    word = s.lower()
    count = Counter(word)
    
    for idx, ch in enumerate(word):
        if count[ch] == 1:
            return (idx, ch)
        
print(first_unique_characters("orytvonavirus"))