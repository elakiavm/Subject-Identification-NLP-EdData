import nltk
from nltk.metrics import edit_distance

nltk.download('punkt')  # Download the NLTK punkt tokenizer data

def calculate_dynamic_threshold(subject, word):
    max_length = max(len(subject), len(word))
    return 1.0 - (edit_distance(subject.lower(), word.lower()) / max_length)

def find_and_replace_subjects(test_case, primary_subjects):
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

                if threshold > 0.5:  # Adjust the threshold for better accuracy
                    # Append "HINDI" if "HINDI COURSE" is matched
                    print("----\n",primary_subject)
                    print("-----\n",word)

                    if primary_subject == "HINDI COURSE" or primary_subject == "HINDI COURSE-B":
                        print("----\n",word)
                        matched_subject = "HINDI"
                    # Append "SCIENCE" for both "SCIENCE THEORY" and "SCIENCE & TECHNOLOGY"
                    elif primary_subject == "SCIENCE & TECHNOLOGY" or primary_subject == "SCIENCE THEORY":
                        matched_subject = "SCIENCE"
                    else:
                        matched_subject = primary_subject

            if matched_subject:
                replaced_words.append(matched_subject)
            else:
                replaced_words.append(word)

        replaced_line = ' '.join(replaced_words)
        replaced_lines.append(replaced_line)

    return '\n'.join(replaced_lines)

# Sample usage
test_case = """    (3) Delhi – 12272
      184 ENGLISHLNG&LIT.  061  019  080  EIGHTY  B2
      085  HINDI COURSE-B  049  020  069  SIXTYNINE  C2
      041  MATHEMATICSSTANDARD  073  020  093  NINETYTHREE  A1
      0B6  SCIENCE-THEORY  059  020  079  SEVENTY NINE  A2
      087  SOCIALSCIENCE  054  019  073  SEVENTYTHREE  C1"""

primary_subjects_array = ["HINDI COURSE", "HINDI COURSE","HINDI", "ENGLISH", "SCIENCE & TECHNOLOGY", "SCIENCE THEORY", "MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

replaced_test_case = find_and_replace_subjects(test_case, primary_subjects_array)
print(replaced_test_case)
