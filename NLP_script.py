# -*- coding: utf-8 -*-

import re

#Tokenize the text using whitespace and punctuation
def tokenize(text):
    return re.findall(r'\b[\u0D80-\u0DFF]+\b', text)

#Remove common Sinhala suffixes from a word
def remove_suffixes(word, suffixes):
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

#Remove suffixes to get the root form of Sinhala words
def stemming(words):
    suffixes = [
           "වෙන්නට", "වෙන්න", "වෙන්ම", "වෙමින", "වෙද්ද", "වෙන්", "වෙල", "කරන්න",
        "වලින", "වලට", "යකට", "යටට", "යටින්", "වීම", "කිරීම", "පහිරිය",
        "වල", "වලි", "යක", "යට", "යකම", "යටුව", "යෙහි", "යෙනු", "යෝ", "යො",
        "යෙහ", "යෙද", "යෙඩ", "යක්ම", "යව", "යෙ", "යෙන", "යා",
        "වා", "යේ", "යන්", "ලේය", "ලෝය", "ලය", "කම", "කර", "ත", "න", "ට", "ව",
        "කාර", "යා", "යාට", "යග", "යෙන", "නිය", "ග", "තුම", "වක්", "යෙක", "යග",
        "යෙන්", "යද", "යෙ", "යෙම", "ය", "යය", "ල", "ලම", "ක", "ක්ම", "ම", "මමය",
        "මෙක", "මිය", "මු", "මම", "මය", "යෙක", "යක්ද", "යෙද" ,"ය", "යි" ,"න්"
        ]

    stems = []
    original_words_map = {}

    for word in words:
        stem = remove_suffixes(word, suffixes)
        if stem not in original_words_map:
            original_words_map[stem] = word
            stems.append(stem)

    # Remove 'eya' suffix from words ending with it
    stems = [stem[:-2] if stem.endswith('එය') else stem for stem in stems]

    return stems, original_words_map

def process_text(text):
    # Step 1: Tokenize the text
    words = tokenize(text)

    # Step 2: Perform stemming
    stems, original_words_map = stemming(words)

    # Step 3: Sort the stems and remove duplicates
    final_stems = sorted(set(stems))

    return final_stems, original_words_map

def save_stems_to_file(stems, original_words_map, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for stem in stems:
            original_word = original_words_map[stem]
            f.write(f"{stem} ({original_word})\n")

# Sinhala text
sinhala_text = """ ### text ### """

# Process the Sinhala text
stems, original_words_map = process_text(sinhala_text)

# Save the final sorted stems to a file
save_stems_to_file(stems, original_words_map, 'sinhala_stems.txt')
