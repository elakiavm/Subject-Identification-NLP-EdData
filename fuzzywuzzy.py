import nltk
from fuzzywuzzy import process
import re

# Function to identify CBSE subjects
def identify_cbse_subjects(text, cbse_subjects):
    # Tokenize the input text into words
    words = nltk.word_tokenize(text.upper())  # Convert to uppercase for case-insensitive matching

    # Use fuzzy string matching to find best matches
    identified_subjects = set()
    for word in words:
        matches = process.extract(word, cbse_subjects, limit=1)
        best_match, score = matches[0]
        if score > 80:  # Adjust the threshold as needed
            identified_subjects.add(best_match)

    return list(identified_subjects)




# Sample text
sample_text = """
300
Oujarat ecodary &Highereeondary oation Banra,Oandlnagar
Examinntion Wing,Vadodara  0716246
STATEMENT OF MARKS
Chis is to certifu that
MODI JAINAM RAJNIKANT
lasaquiatfoltownggraden tlSemarySehool CetifieateCamiation
MONDHAYEAIOF THE EXAM  SEATNO.  CENTRE NUNEER  SCHOOLINDEXO  S.NO.OFSTATEMENT
MARCH-2O18  A1122938  081  55.068  0168294
 ORTAREU  DETABIEO EUSJECT  SUBAECT
NAME OF THE SUBJECT WITHCODE NO.  WEXTES  MARKS OTAINED N WORDS
BOARO  SGHOG  TOTAK  WISE
GRADE
OUTOEN  DUL.OM  GITOF100
04  ENGLISH FL  49  24  073  SEVEN THREE  B1
 10 SOCIAL SCIENCE  43  25  068  SIX EIGHT  B2
11  SCIENCE  TECHNO  41  23  064  SIX FOUR  B2
12  MATHEMATICS  4日  25  073  SEVEN THREE  B1
13  GUJARATI SL  47  24  071  SEVEN ONE  B1
17  SANSKRIT SL  30  24  054  FIVE FOUR  C1
Total:  403
GRANO TOTAL OF MAAKS OBTAIHED  FOUR HUNDRED THREE
PERFORMANCE IN THE SUBJECTS OF SCHOOL BASED EXAMINATION
NAME OF THE SUBJECT WITH CODE NO  GRADE  CO-SCHOLASTIC EVALUATION  GRADI
 24 COMPUTER EDU.-T  B2  Values  A
51  COMPUTER EDU.-P  A2  Skills  A
GRADE  PERCENTILERANK  B.LD.NO
B2  82.55  18S-55-06519
RESULT  QUALIFIED FOR SECONDARY SCHDOL CERTIFICATE
IMPORTANT:Any change inthisdocumentexcept
by the Issuing Authority wil resultin cancelletion of
the documont and sfall also invoke imposition ot
appropriate legal action.
（xO:dkateiExemption(33）
AQincl'Absent  EXAMINATION SECRETAY
Toquity torsubfectacantdafe has tocoremh  110muutef 30.In
"""

# CBSE subjects array
cbse_subjects = [
    "ENGLISH",
    "HINDI",
    "MATHEMATICS",
    "SCIENCE",
    "SOCIAL SCIENCE",
    "PHYSICS",
    "CHEMISTRY",
    "BIOLOGY",
    "COMPUTER SCIENCE",
    "INFORMATICS PRACTICES",
    "PHYSICAL EDUCATION",
    "ECONOMICS",
    "ACCOUNTANCY",
    "BUSINESS STUDIES",
    "POLITICAL SCIENCE",
    "HISTORY",
    "GEOGRAPHY",
    "PSYCHOLOGY",
    "SOCIOLOGY",
    "PHILOSOPHY",
    "HOME SCIENCE",
    "PHYSICAL EDUCATION",
    "ENTREPRENEURSHIP",
    "BIOTECHNOLOGY",
    "MULTIMEDIA AND WEB TECHNOLOGY",
    "ENGINEERING GRAPHICS",
    "INFORMATICS PRAC. (OLD)",
    "COMPUTER SCIENCE (OLD)",
    "MATHS",
    "ENGLISH CORE",
    "ENGLISH ELECTIVE",
    "HINDI CORE",
    "HINDI ELECTIVE",
    "FRENCH",
    "GERMAN",
    "SPANISH",
    "SANSKRIT CORE",
    "SANSKRIT ELECTIVE",
    "ARABIC",
    "TAMIL",
    "TELUGU",
    "MALAYALAM",
    "ODIA",
    "ASSAMESE",
    "BENGALI",
    "GUJARATI",
    "KANNADA",
    "MARATHI",
    "PUNJABI",
    "URDU CORE",
    "URDU ELECTIVE",
    "SOCIAL SCIENCES",
    "SCIENCE & TECHNOLOGY",
    "HEALTH & PHYSICAL EDUCATION",
    "SCOUTING/GUIDING",
    "SELFDEVELOPMENT & ART APPRE."
    # Add more subjects or languages as needed
]


# Identify CBSE subjects in the sample text
identified_cbse_subjects = identify_cbse_subjects(sample_text, cbse_subjects)
print("Identified CBSE Subjects:", identified_cbse_subjects)
