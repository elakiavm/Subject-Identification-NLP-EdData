import re
import nltk
from nltk.metrics import jaccard_distance

def correct_spacing(input_text):
    # Define patterns for subjects and numerical values
    subject_pattern = re.compile(r'\b(MARATHI|HINDI|ENGLISH|MATH|SCIENCE&TECHNOLOGY|SOCIALSCIENCES|HEALTH&PHYSICALEDUCATION|SCOUTING/GUIDING|SELFDEVELOPMENT&ARTAPPRE.)\b', re.IGNORECASE)
    numerical_value_pattern = re.compile(r'\b(\d{2,3})\b')

    # Replace missing spaces for subjects and numerical values while preserving existing spaces
    corrected_text = re.sub(r'(?<!\s)(\d{2,3})(?!\s)', r' \1', input_text)
    corrected_text = re.sub(r'(?<!\s)(MARATHI|HINDI|ENGLISH|MATH|SCIENCE&TECHNOLOGY|SOCIALSCIENCES|HEALTH&PHYSICALEDUCATION|SCOUTING/GUIDING|SELFDEVELOPMENT&ARTAPPRE.)(?!\s)', r' \1', corrected_text)

    return corrected_text

def find_subject(text, subjects):
    corrected_text = correct_spacing(text)
    words = nltk.word_tokenize(corrected_text.lower())  # Tokenize using NLTK, convert to lowercase
    identified_subjects = set()

    for subject in subjects:
        subject_words = nltk.word_tokenize(subject.lower())  # Convert subject to lowercase
        for word in words:
            distance = jaccard_distance(set(subject_words), set([word]))  # Calculate Jaccard distance
            if distance < 0.4:  # Adjust threshold as needed
                identified_subjects.add(subject)

    return list(identified_subjects)

text = """
01MARATHI(1STLANG)  100  083  EIGHTYTHREE
15HINDI(2/3LANG)  100  093  NINETYTHREE
17ENGLISH(2/3LANG)  100  082  EIGHTYTWO
71MATHEMATICS  100  090  NINETY
72SCIENCE&TECHNOLOGY  100  079  SEVENTYNINE
73SOCIALSCIENCES  100  090  NINETY
P1HEALTH&PHYSICALEDUCATION  A
P2SCOUTING/GUIDING  A
R7SELFDEVELOPMENT&ARTAPPRE.  ★  A
88.60  500  $438+05 FOUR HUNDRED AND
"""

cbse_subjects = ["ENGLISH", "HINDI", "MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE", "PHYSICS", "CHEMISTRY", "BIOLOGY", "COMPUTER SCIENCE", "INFORMATICS PRACTICES", "PHYSICAL EDUCATION", "ECONOMICS", "ACCOUNTANCY", "BUSINESS STUDIES", "POLITICAL SCIENCE", "HISTORY", "GEOGRAPHY", "PSYCHOLOGY", "SOCIOLOGY", "PHILOSOPHY", "HOME SCIENCE", "PHYSICAL EDUCATION", "ENTREPRENEURSHIP", "BIOTECHNOLOGY", "MULTIMEDIA AND WEB TECHNOLOGY", "ENGINEERING GRAPHICS", "INFORMATICS PRAC. (OLD)", "COMPUTER SCIENCE (OLD)", "MATHS", "ENGLISH CORE", "ENGLISH ELECTIVE", "HINDI CORE", "HINDI ELECTIVE", "FRENCH", "GERMAN", "SPANISH", "SANSKRIT CORE", "SANSKRIT ELECTIVE", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU CORE", "URDU ELECTIVE", "SOCIAL SCIENCES", "SCIENCE & TECHNOLOGY", "HEALTH & PHYSICAL EDUCATION", "SCOUTING/GUIDING", "SELFDEVELOPMENT & ART APPRE."]

identified_subjects = find_subject(text, cbse_subjects)
print("Identified Subjects:")
for subject in identified_subjects:
    print(subject)
