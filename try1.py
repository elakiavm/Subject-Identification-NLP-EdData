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
        # print(primary_subject_words) 
        for word in words:
            # print("-----",word)
            threshold = calculate_dynamic_threshold(primary_subject, word)
            # print("--------------------",threshold)

            if threshold > 0.5:  # Adjust the threshold for better accuracy
                print("--------------\n",word,primary_subject)
                identified_subjects.add(primary_subject)
    
        identified_subjects = {"HINDI" if subject == "HINDI COURSE" else subject for subject in identified_subjects}

    return list(identified_subjects)

def process_test_cases(test_cases, language_subjects):
    for i, test_case in enumerate(test_cases, start=1):
        # print(f"\nProcessing Test Case {i}:")

        identified_language_subjects = find_language_subjects(test_case, language_subjects)

        if identified_language_subjects:
            # print("\nLanguage Subjects:")
            for subject in identified_language_subjects:
                print(subject)

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
language_subjects_array = ["MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE","ENGLISH","HINDI COURSE", "HINDI", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

# Process test cases
process_test_cases(test_cases_array, language_subjects_array)