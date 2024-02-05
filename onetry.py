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
            words = line_upper.split()  # Tokenize the line

            replaced_words = []  # Store replaced words

            # Handle special cases with separate loop (more efficient)
            for i, word in enumerate(words):
                if word == "MATHEMATICS" and i + 1 < len(words) and words[i + 1] == "STANDARD":
                    replaced_words.extend(["MATHEMATICS", "**"])  # Mark with double asterisk for later removal
                elif word == "SCIENCE" and i + 1 < len(words):
                    if words[i + 1] in ("& TECHNOLOGY", "THEORY", "& TECHNO"):
                        replaced_words.extend(["SCIENCE", "**"])
                else:
                    replaced_words.append(word)

            # Clean up double asterisks and handle remaining words
            replaced_line = " ".join([word for word in replaced_words if word != "**"])
            replaced_words = []

            for word in nltk.word_tokenize(replaced_line):
                matched_subject = None

                # Check for subject followed by specific terms
                if word == "HINDI" and i + 1 < len(words):
                    if words[i + 1] in ("COURSE", "COURSE-A", "COURSE-B"):
                        matched_subject = "HINDI"

                elif word == "ENGLISH" and i + 1 < len(words):
                    if words[i + 1] in ("& LIT.", "COMM"):
                        matched_subject = "ENGLISH"

                # Fallback to primary subjects if not matched already
                if not matched_subject:
                    for primary_subject in primary_subjects:
                        threshold = calculate_dynamic_threshold(primary_subject, word)

                        if threshold > 0.75:  # Adjust threshold as needed
                            matched_subject = primary_subject
                            break

                if matched_subject:
                    replaced_words.append(matched_subject)
                else:
                    replaced_words.append(word)

            replaced_line = " ".join(replaced_words)
            replaced_lines.append(replaced_line)

        modified_test_cases.append("\n".join(replaced_lines))

    return modified_test_cases


# Sample usage
test_case = """(4) Delhi – 12373
      184  ENGLISHLNG&LIT. 039  020  059  FIFTY NINE  D1
      002  HINDI COURSE-A 059  020  079  SEVENTY NINE  B2
      041  MATHEMATICS STANDARD  070 020  090  NINETY  A2
      086  SCIENCE-THEORY  061 020  081  EIGHTY ONE  A2
      087  SOCIAL SCIENCE 060  020  080  EIGHTY  B2
      ADDITIONAL SUBJECT
      402  INFORMATIONTECHNOLOGY 047  050  097  NINETY SEVEN  A1"""

primary_subjects_array = ["HINDI COURSE","HINDI", "ENGLISH", "SCIENCE & TECHNOLOGY","SCIENCE THEORY","MATHEMATICS STANDARD,""MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

replaced_test_case = find_and_replace_subjects(test_case, primary_subjects_array)
print(replaced_test_case)
