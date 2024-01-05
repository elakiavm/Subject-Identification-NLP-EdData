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

def find_primary_subject(text, primary_subjects):
    text_without_numbers = remove_numbers(text)
    corrected_text = correct_spacing(text_without_numbers.upper())  # Convert to uppercase
    
    words = nltk.word_tokenize(corrected_text)
    identified_subjects = set()

    for primary_subject in primary_subjects:
        primary_subject_words = nltk.word_tokenize(primary_subject)
        
        # Check for direct matching of tokenized words
        if set(primary_subject_words).intersection(words):
            identified_subjects.add(primary_subject)
        else:
            # If no direct match, perform spacing and spelling corrections
            print(f"Tokenized Words: {words}")
            print(f"Intersection: {set(primary_subject_words).intersection(words)}")
            
            for word in words:
                threshold = calculate_dynamic_threshold(primary_subject, word)
                print(f"Word: {word}, Threshold: {threshold}")
                
                if threshold > 0.5:  # Adjust the threshold for better accuracy
                    identified_subjects.add(primary_subject)

    return list(identified_subjects)



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
    # Add more test cases as needed
]


# Define your list of subjects
language_subjects_array = ["ENGLISH", "HINDI", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

# Process each test case
for i, test_case in enumerate(test_cases_array, start=1):
    identified_subjects = find_primary_subject(test_case, language_subjects_array)
    print(f"\nPrimary Subjects in Test Case {i}:")
    for subject in identified_subjects:
        print(subject)
