# from difflib import get_close_matches
import nltk
from nltk.metrics import edit_distance
import re

def calculate_dynamic_threshold(subject, word):
    max_length = max(len(subject), len(word))
    return 1.0 - (edit_distance(subject.lower(), word.lower()) / max_length)

def find_and_replace_subjects(input_text, primary_subjects_array):
    output_text = ""

    for line in input_text.split("\n"):
        line_upper = line.upper()  # Convert line to uppercase
        replaced_words = []

        line_upper = re.sub(r"GENERALSCIENCE", "GENERAL SCIENCE", line_upper)
        line_upper = re.sub(r"01MARATHI", "MARATHI", line_upper)
        line_upper = re.sub(r"MATHEMATICS STANDARD", "MATHEMATICS", line_upper)
        line_upper = re.sub(r"ENGLISHLNG&LIT\.|ENGLISH COMM", "ENGLISH", line_upper)
        line_upper = re.sub(r"ENGLISH & LIT", "ENGLISH", line_upper)
        line_upper = re.sub(r"HINDI COURSE(-A|B|-B|-COURSE|-COURSE-A)", "HINDI", line_upper)
        line_upper = re.sub(r"SCIENCE (& TECHNOLOGY|THEORY|TECHNO)", "SCIENCE", line_upper)
        line_upper = re.sub(r"(LANGUAGE)", r" \1 ", line_upper)
        # Fallback to word tokenization and edit distance first
        words = nltk.word_tokenize(line_upper)
        for word in words:
            matched_subject = None

            for primary_subject in primary_subjects_array:
                threshold = calculate_dynamic_threshold(primary_subject, word)

                if threshold > 0.5:  # Adjust threshold for desired accuracy
                    if primary_subject == "HINDI COURSE" or primary_subject == "HINDI COURSE B" or primary_subject == "HINDI COURSE-A":
                        matched_subject = "HINDI "
                    elif primary_subject == "SCIENCE & TECHNOLOGY" or primary_subject == "SCIENCE TECHNO" or primary_subject == "SCIENCE THEORY":
                        matched_subject = "SCIENCE "
                    elif primary_subject == "SOCIALSCIENCE":
                        matched_subject = "SOCIAL SCIENCE "
                    elif primary_subject == "GENERAL SCIENCE":
                        matched_subject = "GENERAL SCIENCE"
                    else:
                        matched_subject = " " + primary_subject + " "
                    break

            if matched_subject:
                replaced_words.append(matched_subject)
            else:
                replaced_words.append(word)

        # Reconstruct the line and apply regular expressions
        replaced_line = ' '.join(replaced_words)
        # replaced_line = re.sub(r"HINDI COURSE(-A|B|-B|-COURSE|-COURSE-A)", "HINDI", replaced_line)
        # replaced_line = re.sub(r"SCIENCE (& TECHNOLOGY|THEORY|TECHNO)", "SCIENCE", replaced_line)
        # replaced_line = re.sub(r"MATHEMATICS STANDARD", "MATHEMATICS", replaced_line)
        # replaced_line = re.sub(r"ENGLISHLNG&LIT\.|ENGLISH COMM", "ENGLISH", replaced_line)
        # replaced_line = re.sub(r"ENGLISH & LIT", "ENGLISH", replaced_line)
        # replaced_line = re.sub(r"(LANGUAGE)", r" \1 ", replaced_line)
        # replaced_line = re.sub(r"(SOCIAL SCIENCE)", r" \1 ", replaced_line)
        # replaced_line = re.sub(r"(ENGLISH)", r" \1 ", replaced_line)
        # replaced_line = re.sub(r"(MATHEMATICS)", r" \1 ", replaced_line)
        # replaced_line = re.sub(r"(SCIENCE)", r" \1 ", replaced_line)

        output_text += replaced_line + "\n"

    return output_text

# Test case
input_text = """
(5) Gujarat – 12523
中 CUJAAATI FL 25 078 SEVEN EIOHT
10 SOCIALSCIENCE 53 2S O70 SEVEN ELGHT
SEIEMCL TECHNO 48 76 OT4 SEVEH TOUR
1E PATHEHATICE 57 3 EIGHT ZERD
店 ENOLISH SL 45 25 070 SEVEN ZEHO
BANSKRIT BL 4 26 075 SEVEN FIVE 中
"""
def main(test_cases):
    primary_subjects_array = ["HINDI COURSE", "HINDI COURSE B", "HINDI COURSE A", "SCIENCE TECHNO", "HINDI",
                                "ENGLISH",  "MATHEMATICS","SOCIAL SCIENCE", "SCIENCE", "GENERAL SCIENCE", 
                                "SCIENCE THEORY", "SCIENCE & TECHNO","SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC","TAMIL", 
                                "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA",
                                "MARATHI", "PUNJABI", "URDU"]


    output_text = find_and_replace_subjects(test_cases, primary_subjects_array)
    return (output_text)
