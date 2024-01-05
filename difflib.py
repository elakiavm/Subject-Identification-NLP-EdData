from difflib import get_close_matches

def identify_cbse_subjects(input_text, cbse_subjects):
    identified_subjects = []

    for word in input_text.split():
        closest_matches = get_close_matches(word, cbse_subjects, n=1, cutoff=0.8)
        if closest_matches:
            identified_subjects.append(closest_matches[0])

    return identified_subjects

# Example usage
input_text = """

"""

cbse_subjects = ["ENGLISH", "HINDI", "MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE", "PHYSICS", "CHEMISTRY", "BIOLOGY", "COMPUTER SCIENCE", "INFORMATICS PRACTICES", "PHYSICAL EDUCATION", "ECONOMICS", "ACCOUNTANCY", "BUSINESS STUDIES", "POLITICAL SCIENCE", "HISTORY", "GEOGRAPHY", "PSYCHOLOGY", "SOCIOLOGY", "PHILOSOPHY", "HOME SCIENCE", "PHYSICAL EDUCATION", "ENTREPRENEURSHIP", "BIOTECHNOLOGY", "MULTIMEDIA AND WEB TECHNOLOGY", "ENGINEERING GRAPHICS", "INFORMATICS PRAC. (OLD)", "COMPUTER SCIENCE (OLD)", "MATHS", "ENGLISH CORE", "ENGLISH ELECTIVE", "HINDI CORE", "HINDI ELECTIVE", "FRENCH", "GERMAN", "SPANISH", "SANSKRIT CORE", "SANSKRIT ELECTIVE", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU CORE", "URDU ELECTIVE", "SOCIAL SCIENCES", "SCIENCE & TECHNOLOGY", "HEALTH & PHYSICAL EDUCATION", "SCOUTING/GUIDING", "SELFDEVELOPMENT & ART APPRE."]

identified_subjects = identify_cbse_subjects(input_text, cbse_subjects)
print("Identified CBSE Subjects:", identified_subjects)
