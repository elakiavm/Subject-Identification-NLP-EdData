import re
import nltk
from nltk.metrics import edit_distance

def remove_numbers(text):
    return re.sub(r'\d', '', text)

def correct_spacing(input_text):
    # Add space between camel-case words
    input_text = re.sub('([a-z])([A-Z])', r'\1 \2', input_text)
    
    # Define patterns for subjects and numerical values
    subject_pattern = re.compile(r'\b(MARATHI|HINDI|ENGLISH|MATH|SCIENCE&TECHNOLOGY|SOCIAL SCIENCES|HEALTH&PHYSICALEDUCATION|SCOUTING/GUIDING|SELF DEVELOPMENT&ART APPRE|SANSKRIT)\b', re.IGNORECASE)
    numerical_value_pattern = re.compile(r'\b(\d{2,3})\b')

    # Replace missing spaces for subjects and numerical values while preserving existing spaces
    corrected_text = re.sub(numerical_value_pattern, r' \1 ', input_text)
    corrected_text = re.sub(subject_pattern, r' \1 ', corrected_text)

    # Remove extra spaces and trim the text
    corrected_text = ' '.join(corrected_text.split())
    
    return corrected_text
def calculate_jaccard_similarity(set1, set2):
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))
    return 1.0 - (intersection_size / union_size) if union_size != 0 else 0.0

def find_primary_subject(text, primary_subjects):
    text_without_numbers = remove_numbers(text)
    corrected_text = correct_spacing(text_without_numbers.upper())  # Convert to uppercase
    
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

def calculate_dynamic_threshold(subject, word):
    max_length = max(len(subject), len(word))
    return 1.0 - (edit_distance(subject, word) / max_length)

def find_language_subjects(text, language_subjects):
    text_without_numbers = remove_numbers(text)
    corrected_text = correct_spacing(text_without_numbers.upper())  # Convert to uppercase
    
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

# def process_test_cases(test_cases, primary_subjects, language_subjects):
#     for i, test_case in enumerate(test_cases, start=1):
#         print(f"\nProcessing Test Case {i}:")
        
#         # Process the current test case
#         identified_primary_subjects = find_primary_subject(test_case, primary_subjects)
#         identified_language_subjects = find_language_subjects(test_case, language_subjects)

#         # Display results only if subjects are identified
#         if identified_primary_subjects:
#             print("Primary Subjects:")
#             for subject in identified_primary_subjects:
#                 print(subject)

#         if identified_language_subjects:
#             print("\nLanguage Subjects:")
#             for subject in identified_language_subjects:
#                 print(subject)
def process_test_cases(test_cases, primary_subjects, language_subjects):
    for i, test_case in enumerate(test_cases, start=1):
        processed_lines = []
        lines = test_case.splitlines()

        for line in lines:
            words = line.split()
            corrected_words = []

            for word in words:
                corrected_word = word

                # Check for primary subjects
                for primary_subject in primary_subjects:
                    if edit_distance(word, primary_subject) <= 2:  # Adjust threshold if needed
                        corrected_word = primary_subject
                        break

                # Check for language subjects
                if corrected_word == word:
                    for language_subject in language_subjects:
                        if edit_distance(word, language_subject) <= 2:  # Adjust threshold if needed
                            corrected_word = language_subject
                            break

                corrected_words.append(corrected_word)

            processed_line = " ".join(corrected_words)
            processed_lines.append(processed_line)

        output = "\n".join(processed_lines)
        print(f"\nProcessing Test Case {i}:\n{output}")
# Test cases as an array
test_cases_array = [
    """
    (3) Delhi – 12272
      184 ENGLISHLNG&LIT.  061  019  080  EIGHTY  B2
      085  HINDICOURSE-B  049  020  069  SIXTYNINE  C2
      041  MATHEMATICSSTANDARD  073  020  093  NINETYTHREE  A1
      0B6  SCIENCE-THEORY  059  020  079  SEVENTY NINE  A2
      087  SOCIALSCIENCE  054  019  073  SEVENTYTHREE  C1
    """,
]


# Define primary subjects and language subjects
primary_subjects_array = ["MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE"]
language_subjects_array = ["ENGLISH","HINDI COURSE", "HINDI", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

# Process test cases
process_test_cases(test_cases_array, primary_subjects_array, language_subjects_array)


