import nltk
from nltk.metrics import edit_distance

nltk.download('punkt')  # Download the NLTK punkt tokenizer data

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
            words = nltk.word_tokenize(line_upper)
            replaced_words = []

            for word in words:
                matched_subject = None

                for primary_subject in primary_subjects:
                    threshold = calculate_dynamic_threshold(primary_subject, word)
                    if threshold > 0.5:
                        # print("-----testing-----\n",primary_subject)
                        if primary_subject == "HINDI COURSE" or primary_subject == "HINDI COURSE B":
                            matched_subject = "HINDI"
                            print("-------101----",matched_subject)

                            # print("******** matched word *******", matched_subject)
                        # Append "SCIENCE" for both "SCIENCE THEORY" and "SCIENCE & TECHNOLOGY"
                        elif primary_subject == "SCIENCE & TECHNOLOGY" or primary_subject == "SCIENCE THEORY" or primary_subject=="SCIENCE TECHNO":
                            matched_subject = "SCIENCE"
                            print("-------202----",matched_subject)
                        elif primary_subject == "ENGLISH COMM":
                            matched_subject = "ENGLISH"
                            print("-------303----",matched_subject)
                        else:
                            matched_subject = primary_subject
                            print("-------common----",matched_subject)
                if matched_subject:
                    replaced_words.append(matched_subject)
                    print("*** no Change ***",replaced_words)
                else:
                    replaced_words.append(word)
                    print("*** no Change 101 ***",replaced_words)


            replaced_line = ' '.join(replaced_words)
            replaced_lines.append(replaced_line)

        modified_test_cases.append('\n'.join(replaced_lines))

    return modified_test_cases

test_cases = [

    """
    (2) Delhi – 12200
      020  086  EIGHTY SIX A2
      184 ENGLISHLNG&LIT.  066
      002  HINDI COURSE-A  075  020  095 NINETY FIVE  A1
      041  MATHEMATICS STANDARD 079  020  099  NINETY NINE  A1
      020  095  NINETY FIVE A1
      086 SCIENCE-THEORY  075
      075 NINETY FIVE  A1
      087 SOCIAL SCIENCE  020  095
    """,
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


primary_subjects_array = ["HINDI COURSE", "HINDI COURSE B","HINDI COURSE A","SCIENCE TECHNO","HINDI", "ENGLISH COMM", "ENGLISH", "SCIENCE & TECHNOLOGY", "SCIENCE THEORY", "MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

modified_test_cases = find_and_replace_subjects(test_cases, primary_subjects_array)

for i, modified_test_case in enumerate(modified_test_cases):
    print(f"\nModified Test Case {i + 1}:\n{modified_test_case}")
