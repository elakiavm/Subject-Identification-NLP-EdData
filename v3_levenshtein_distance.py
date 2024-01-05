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
        for word in words:
            threshold = calculate_dynamic_threshold(primary_subject, word)
            if threshold > 0.7:  # Adjust the threshold for better accuracy
                identified_subjects.add(primary_subject)

    return list(identified_subjects)

test_cases = [    """
    (5) Gujarat – 12523
      中  CUJAAATI FL 25  078  SEVEN EIOHT
      10  SOCIALSCIENCE  53 2S  O70  SEVEN ELGHT
      SEIEMCL  TECHNO  48 76  OT4  SEVEH TOUR
      1E  PATHEHATICE 57  3  EIGHT ZERD
      店  ENOLISH SL 45  25  070  SEVEN ZEHO
      BANSKRIT BL  4  26  075  SEVEN FIVE  中
    """,]
# Define your list of subjects
cbse_subjects = [
    "ENGLISH", "HINDI", "MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE", "PHYSICS", "CHEMISTRY", "BIOLOGY",
    "COMPUTER SCIENCE", "INFORMATICS PRACTICES", "PHYSICAL EDUCATION", "ECONOMICS", "ACCOUNTANCY",
    "BUSINESS STUDIES", "POLITICAL SCIENCE", "HISTORY", "GEOGRAPHY", "PSYCHOLOGY", "SOCIOLOGY", "PHILOSOPHY",
    "HOME SCIENCE", "PHYSICAL EDUCATION", "ENTREPRENEURSHIP", "BIOTECHNOLOGY", "MULTIMEDIA AND WEB TECHNOLOGY",
    "ENGINEERING GRAPHICS", "INFORMATICS PRAC. (OLD)", "COMPUTER SCIENCE (OLD)", "MATHS", "ENGLISH CORE",
    "ENGLISH ELECTIVE", "HINDI CORE", "HINDI ELECTIVE", "FRENCH", "GERMAN", "SPANISH", "SANSKRIT CORE",
    "SANSKRIT ELECTIVE", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI",
    "KANNADA", "MARATHI", "PUNJABI", "URDU CORE", "URDU ELECTIVE", "SOCIAL SCIENCES", "SCIENCE & TECHNOLOGY",
    "HEALTH & PHYSICAL EDUCATION", "SCOUTING/GUIDING", "SELF DEVELOPMENT & ART APPRE", "SANSKRIT"
]

# Process each test case
for i, test_case in enumerate(test_cases, start=1):
    identified_subjects = find_primary_subject(test_case, cbse_subjects)
    print(f"\nPrimary Subjects in Test Case {i}:")
    for subject in identified_subjects:
        print(subject)