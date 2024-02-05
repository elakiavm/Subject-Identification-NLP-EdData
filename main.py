from difflib import get_close_matches
import nltk
from nltk.metrics import edit_distance

def calculate_jaccard_similarity(set1, set2):
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))
    return 1.0 - (intersection_size / union_size) if union_size != 0 else 0.0

def calculate_dynamic_threshold(subject, word):
    max_length = max(len(subject), len(word))
    return 1.0 - (edit_distance(subject, word) / max_length)

def find_primary_subject(text, primary_subjects):
    corrected_text = text.upper()  # Convert to uppercase
    
    words = nltk.word_tokenize(corrected_text)
    identified_primary_subjects = set()

    for primary_subject in primary_subjects:
        primary_subject_words = set(nltk.word_tokenize(primary_subject))
        
        # Check if the subject is already identified
        if primary_subject in identified_primary_subjects:
            continue
        
        for i in range(len(words) - len(primary_subject_words) + 1):
            word_subset = words[i:i + len(primary_subject_words)]
            subset_set = set(word_subset)
            
            # Calculate Jaccard similarity as Jaccard distance (1 - similarity)
            similarity = calculate_jaccard_similarity(primary_subject_words, subset_set)
            
            # If the similarity is above a certain value, consider it a match
            if similarity > 0.7:
                identified_primary_subjects.add(primary_subject)
                break  # Break the inner loop to avoid rechecking for the same subject

    return list(identified_primary_subjects)

def find_language_subjects(text, language_subjects):
    corrected_text = text.upper()  # Convert to uppercase
    
    words = nltk.word_tokenize(corrected_text)
    identified_subjects = set()

    for primary_subject in language_subjects:
        primary_subject_words = nltk.word_tokenize(primary_subject)
        for word in words:
            threshold = calculate_dynamic_threshold(primary_subject, word)
            if threshold > 0.5:  # Adjust the threshold for better accuracy
                identified_subjects.add(primary_subject)
    
        identified_subjects = {"HINDI" if subject == "HINDI COURSE" else subject for subject in identified_subjects}

    return list(identified_subjects)

def replace_subjects(input_text, primary_subjects_array, language_subjects_array):
    output_text = ""

    for line in input_text.split("\n"):
        words = line.split()
        replaced_words = []

        for word in words:
            if word.isalpha():
                # Check if the word is a primary subject
                if word.upper() in primary_subjects_array:
                    replaced_words.append(word.upper())
                else:
                    # Find the closest match in the language subjects array
                    closest_match = get_close_matches(word.upper(), language_subjects_array, n=1, cutoff=0.5)
                    if closest_match:
                        replaced_words.append(closest_match[0])
                    else:
                        # Check if the word is a primary subject using Jaccard similarity
                        identified_primary_subjects = find_language_subjects(word, primary_subjects_array)
                        if identified_primary_subjects:
                            replaced_words.append(identified_primary_subjects[0])
                        else:
                            # Check if the word is a language subject using dynamic threshold
                            identified_language_subjects = find_language_subjects(word, language_subjects_array)
                            if identified_language_subjects:
                                replaced_words.append(identified_language_subjects[0])
                            else:
                                replaced_words.append(word)
            else:
                replaced_words.append(word)

        output_text += " ".join(replaced_words) + "\n"

    return output_text

# Test case
input_text = """
(5) Gujarat – 12523
中 CUJAAATI FL 25 078 SEVEN EIOHT
10 SOCIALSCIENCE 53 2S O70 SEVEN ELGHT
SEIEMCL TECHNO 48 76 OT4 SEVEH TOUR
1E PATHEHATICE 57 3 EIGHT ZERD
店 ENOLISH SL 45 25 070 SEVEN ZEHO
BANSKRIT BL 4 26 075 SEVEN FIVE 中
"""

primary_subjects_array = ["MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE"]
language_subjects_array = ["MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE","ENGLISH", "HINDI COURSE", "HINDI", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

output_text = replace_subjects(input_text, primary_subjects_array, language_subjects_array)
print(output_text)
