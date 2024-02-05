import nltk
import re
from nltk.metrics import edit_distance

nltk.download('punkt')  # Download the NLTK punkt tokenizer data (only needed if using word_tokenize)
 # Download the NLTK punkt tokenizer data (only needed if using word_tokenize)

def calculate_dynamic_threshold(subject, word):
    max_length = max(len(subject), len(word))
    return 1.0 - (edit_distance(subject.lower(), word.lower()) / max_length)

def find_and_replace_subjects(test_cases, primary_subjects):
    modified_test_cases = []

    for test_case in test_cases:
        lines = test_case.split('\n')
        replaced_lines = []

        for line in lines:
            line_upper = line.upper()  # Convert line to uppercase

            # Prioritize regular expressions for specific patterns
            replaced_line = re.sub(r"HINDI COURSE(-A|B|-B|-COURSE|-COURSE-A)", "HINDI", line_upper)
            replaced_line = re.sub(r"SCIENCE (& TECHNOLOGY|THEORY|TECHNO)", "SCIENCE", replaced_line)
            replaced_line = re.sub(r"MATHEMATICS STANDARD", "MATHEMATICS", replaced_line)
            replaced_line = re.sub(r"ENGLISHLNG&LIT\.|ENGLISH COMM", "ENGLISH", replaced_line)

            # Further replace "COURSE" variations if any remain
            replaced_line = re.sub(r"HINDI COURSE", "HINDI", replaced_line)
            replaced_line = re.sub(r"SEIEMCL  TECHNO", "SCIENCE", replaced_line)
            replaced_line = re.sub(r"SCIENCE&TECHNOLOGY", "SCIENCE", replaced_line)
            replaced_line = re.sub(r"SRIENTE & TECHNOLOGY", "SCIENCE", replaced_line) 
            # Fallback to word tokenization and edit distance if needed
            words = nltk.word_tokenize(replaced_line)
            replaced_words = []
            for word in words:
                matched_subject = None

                for primary_subject in primary_subjects:
                    threshold = calculate_dynamic_threshold(primary_subject, word)

                    if threshold > 0.5:  # Adjust threshold for desired accuracy
                        if primary_subject == "HINDI COURSE" or primary_subject == "HINDI COURSE B":
                            matched_subject = "HINDI"
                        elif primary_subject == "SCIENCE & TECHNOLOGY" or primary_subject == "SCIENCE TECHNO" or primary_subject == "SCIENCE THEORY":
                            matched_subject = "SCIENCE"
                        else:
                            matched_subject = primary_subject
                        break

                if matched_subject:
                    replaced_words.append(matched_subject)
                else:
                    replaced_words.append(word)

            replaced_line = ' '.join(replaced_words)
            replaced_lines.append(replaced_line)

        modified_test_cases.append('\n'.join(replaced_lines))

    return modified_test_cases


# List of test cases
test_cases = [
    """
    (12) Maharashtra – 1221
    01MARATHI(1STLANG)  100  083  EIGHTYTHREE
    15HINDI(2/3LANG)  100  093  NINETYTHREE
    17ENGLISH(2/3LANG)  100  082  EIGHTYTWO
    71MATHEMATICS  100  090  NINETY
    72SCIENCE&TECHNOLOGY  100  079  SEVENTYNINE
    73SOCIALSCIENCES  100  090  NINETY
    """,
    """
    (13) Maharashtra – 1281
    03ENGLISH(1STLANG)  100  062  SIXTYTWO
    16MARATHI (2/3LANG)  100  052  FIFTYTWO
    15HINDI(2/3 LANG)  100  075  SEVENTYFIVE
    71MATHEMATICS  100  084  EIGHTYFOUR
    72SCIENCE&TECHNOLOGY  100  063  SIXTYTHREE
    73SOCIALSCIENCES  100  070  SEVENTY
    """,
    """
    (14) Maharashtra – 12606
    01MARATHI(1ST LANG)  100  045  FORTYFIVE
    15HINDI(2/3LANG)  100  068  SIXTYEIGHT
    17 ENGLISH(2/3LANG)  100  072  SEVENTYTWO  1888888881
    71MATHEMATICS  100  089  EIGHTYNINE
    72SCIENCE& TECHNOLOGY  100  087  EIGHTYSEVEN
    73SOCIAL SCIENCES  100  085  EIGHTYFIVE
    """,
    """
    (15) Odisha – 12407
    FLO  FIRST LANGUAGE ODIA  100  74
    SLE  SECONDLANGUAGEENGLISH  100  63
    TLS  THIRD LANGUAGESANSKRIT  100  82
    MTH  MATHEMATICS  100  63
    GSC  GENERALSCIENCE  100  70
    SSC  SOCIAL SCIENCE  100  61
    """,
    """
    (16) Odisha – 12502
    FIRST LANGUAGE ODIA  FULLMARKS
    SLE  SECOND LANGUAGE ENGLISH  MARKS SECURED
    TLS  THIRD LANGUAGE SANSKRIT  100  75
    MTH  MATHEMATICS  100  75
    GSC  GENERAL SCIENCE  100  98
    S3C  SOCIAL SCIENCE  100  96
    """,
    """
    (17) Odisha – 12515
    100  70
    FLO  FIRSTLANGUAGEODIA  49
    100
    SLE  SECOND LANGUAGE ENGLISH
    100 92
    TLS  THIRD LANGUAGESANSKRIT  81
    100
    MTH  MATHEMATICS
    100  55
    GSC  GENERAL SCIENCE
    100  65
    SSC  SOCIALSCIENCE
    """,
    """
    (18) Odisha – 12689
    FLO  FIRST LANGUAGE ODIA  100  33
    SLE  SECOND LANGUAGE ENGLISH  100  33
    TLH  THIRD LANGUAGEHINDI  100  36
    MTH  MATHEMATICS  100  32
    GSC  GENERAL SCIENCE  100  32
    SSC  SOCIAL SCIENCE  100  32
    """,
    """
    (19) Odisha – 12738
    FLO.  FIRST LANGUAGEODIA  100  65
    SLE  SECOND LANGUAGEENGLISH  100  53
    TLS  THIRDLANGUAGE SANSKRIT  100:  68
    MTH  MATHEMATICS  100  80
    GSC  GENERAL SCIENCE  100  42
    SSC  SOCIALSCIENCE  100  36
    """,
    """
    (20) Odisha – 116649
    FLO  FIRSTLANGUAGE ODIA  100  70
    SLE  SECOND LANGUAGEENGLISH  100  56
    TLH  THIRDLANGUAGEHINDI  100  79
    MTH  MATHEMATICS  100  82
    GSC  GENERALSCIENCE  100  65
    SSC  SOCIAL SCIENCE  100  
    """
]

primary_subjects_array = ["HINDI COURSE", "HINDI COURSE B", "HINDI COURSE A", "SCIENCE TECHNO", "HINDI",
                          "ENGLISH",  "MATHEMATICS","SOCIAL SCIENCE", "SCIENCE", "SCIENCE & TECHNOLOGY", 
                          "SCIENCE THEORY", "SCIENCE & TECHNO","SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC","TAMIL", 
                          "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA",
                          "MARATHI", "PUNJABI", "URDU"]

modified_test_cases = find_and_replace_subjects(test_cases, primary_subjects_array)

for i, modified_test_case in enumerate(modified_test_cases):
   print(f"\nModified Test Case {i + 1}:\n{modified_test_case}")
