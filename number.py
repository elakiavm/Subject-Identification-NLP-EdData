import nltk
import re
from nltk.metrics import edit_distance

nltk.download('punkt')  

# def calculate_dynamic_threshold(subject, word):
#     max_length = max(len(subject), len(word))
#     return 1.0 - (edit_distance(subject.lower(), word.lower()) / max_length)

def find_and_replace_subjects(test_cases, primary_subjects):
    modified_test_cases = []

    for test_case in test_cases:
        lines = test_case.split('\n')
        replaced_lines = []

        for line in lines:
            line_upper = line.upper()  # Convert line to uppercase
            replaced_words = []
            
            line_upper = re.sub(r"GENERALSCIENCE", "GENERAL SCIENCE", line_upper)
            line_upper = re.sub(r"01MARATHI", "MARATHI", line_upper)

            # Fallback to word tokenization and edit distance first
            words = nltk.word_tokenize(line_upper)
            for word in words:
                matched_subject = None

                for primary_subject in primary_subjects:
                    threshold = calculate_dynamic_threshold(primary_subject, word)

                    if threshold > 0.5:  # Adjust threshold for desired accuracy
                        if primary_subject == "HINDI COURSE" or primary_subject == "HINDI COURSE B":
                            matched_subject = "HINDI "
                        elif primary_subject == "SCIENCE & TECHNOLOGY" or primary_subject == "SCIENCE TECHNO" or primary_subject == "SCIENCE THEORY":
                            matched_subject = "SCIENCE "
                        elif primary_subject == "SOCIALSCIENCE":
                            matched_subject = "SOCIAL SCIENCE "
                        elif primary_subject == "GENERAL SCIENCE" :
                            matched_subject = "GENERAL SCIENCE"
                        else:
                            matched_subject = " "+primary_subject+" "
                        break

                if matched_subject:
                    replaced_words.append(matched_subject)
                else:
                    replaced_words.append(word)

            # Reconstruct the line and apply regular expressions
            replaced_line = ' '.join(replaced_words)
            replaced_line = re.sub(r"HINDI COURSE(-A|B|-B|-COURSE|-COURSE-A)", "HINDI", replaced_line)
            replaced_line = re.sub(r"SCIENCE (& TECHNOLOGY|THEORY|TECHNO)", "SCIENCE", replaced_line)
            replaced_line = re.sub(r"MATHEMATICS STANDARD", "MATHEMATICS", replaced_line)
            replaced_line = re.sub(r"ENGLISHLNG&LIT\.|ENGLISH COMM", "ENGLISH", replaced_line)
            replaced_line = re.sub(r"ENGLISH & LIT", "ENGLISH", replaced_line)
            replaced_line = re.sub(r"(LANGUAGE)", r" \1 ", replaced_line)
            replaced_line = re.sub(r"(SOCIAL SCIENCE)", r" \1 ", replaced_line)
            replaced_line = re.sub(r"(ENGLISH)", r" \1 ", replaced_line)
            replaced_line = re.sub(r"(MATHEMATICS)", r" \1 ", replaced_line)
            replaced_line = re.sub(r"(SCIENCE)", r" \1 ", replaced_line)

            replaced_lines.append(replaced_line)

        modified_test_cases.append('\n'.join(replaced_lines))

    return modified_test_cases

def calculate_dynamic_threshold(subject, word):
    max_length = max(len(subject), len(word))
    return 1.0 - (edit_distance(subject.lower(), word.lower()) / max_length)

# def find_and_replace_subjects(test_cases, primary_subjects):
#     modified_test_cases = ""

#     for test_case in test_cases:
#         lines = test_case.split('\n')
#         modified_test_case = ""

#         for line in lines:
#             line_upper = line.upper()  # Convert line to uppercase
#             replaced_words = ""

#             line_upper = re.sub(r"GENERALSCIENCE", "GENERAL SCIENCE", line_upper)
#             line_upper = re.sub(r"01MARATHI", "MARATHI", line_upper)

#             # Fallback to word tokenization and edit distance first
#             words = nltk.word_tokenize(line_upper)
#             if words:  # Check if words list is not empty
#                 replaced_words = words[0]  # Initialize with the first word
#             for i in range(1, len(words)):
#                 word = words[i]
#                 matched_subject = None

#                 for primary_subject in primary_subjects:
#                     threshold = calculate_dynamic_threshold(primary_subject, word)

#                     if threshold > 0.5:  # Adjust threshold for desired accuracy
#                         matched_subject = get_matched_subject(primary_subject)  # Using a function for clarity
#                         if matched_subject:
#                             break

#                 if matched_subject:
#                     replaced_words += matched_subject
#                 else:
#                     replaced_words += " " + word

#             # Apply regular expressions directly on the string
#             replaced_line = re.sub(r"HINDI COURSE(-A|B|-B|-COURSE|-COURSE-A)", "HINDI", replaced_words)
#             replaced_line = re.sub(r"SCIENCE (& TECHNOLOGY|THEORY|TECHNO)", "SCIENCE", replaced_line)
#             replaced_line = re.sub(r"MATHEMATICS STANDARD", "MATHEMATICS", replaced_line)
#             replaced_line = re.sub(r"ENGLISHLNG&LIT\.|ENGLISH COMM", "ENGLISH", replaced_line)
#             replaced_line = re.sub(r"ENGLISH & LIT", "ENGLISH", replaced_line)
#             replaced_line = re.sub(r"(LANGUAGE)", r" \1 ", replaced_line)
#             replaced_line = re.sub(r"(SOCIAL SCIENCE)", r" \1 ", replaced_line)


#             modified_test_case += replaced_line + "\n"

#         modified_test_cases += modified_test_case

#     return modified_test_cases

# def get_matched_subject(primary_subject):
#     if primary_subject == "HINDI COURSE" or primary_subject == "HINDI COURSE B":
#         return "HINDI "
#     elif primary_subject == "SCIENCE & TECHNOLOGY" or primary_subject == "SCIENCE TECHNO" or primary_subject == "SCIENCE THEORY":
#         return "SCIENCE "
#     elif primary_subject == "SOCIALSCIENCE":
#         return "SOCIAL SCIENCE "
#     elif primary_subject == "GENERAL SCIENCE":
#         return "GENERAL SCIENCE"
#     else:
        # return primary_subject 

def format_modified_test_cases(modified_test_cases):
    return '\n\n'.join(modified_test_cases)

def main(test_cases):
    primary_subjects_array = ["HINDI COURSE", "HINDI COURSE B", "HINDI COURSE A", "SCIENCE TECHNO", "HINDI",
                            "ENGLISH",  "MATHEMATICS","SOCIAL SCIENCE", "SCIENCE", "GENERAL SCIENCE", 
                            "SCIENCE THEORY", "SCIENCE & TECHNO","SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC","TAMIL", 
                            "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA",
                            "MARATHI", "PUNJABI", "URDU"]

    modified_test_cases = find_and_replace_subjects(test_cases, primary_subjects_array)
    formatted_text = format_modified_test_cases(modified_test_cases)

# Print or use the formatted_text as needed
    print(formatted_text)
    # str(modified_test_cases)
    # print(modified_test_cases)
    # result=""
    # result.join(modified_test_cases)
    # result = ''.join(char for char in modified_test_cases if char != '')
    # result = ' '.join(char if char != '' else ' ' for char in modified_test_cases)
    # result = [' ' if s == '' else s for s in modified_test_cases]
    # result_line =''.join(modified_test_cases)
    # print(result)

    # for modified_test_case in enumerate(modified_test_cases):
    #     # result += modified_test_case + '\n'

    #     # strResult.append(modified_test_case)
    #     # print(modified_test_case)        # print(result)
    #     lines = modified_test_case.split('\n')
    #     for line in lines:
    #             print("-", line)


    return modified_test_cases
    
test_cases = """
    Mlabarashtra State Board f
Setondarp amd Digher Setondary Couration,Pume
UTfTS/PUNEDIVISIONALBOARD
SECONDARYSCHOOLCERTIFICATEEXAMINATION-STATEMENTOFMARKS
SEATNO.  CENTRENO.  DIST.&SCHOOLNO.  MONTH&YEAROFEXAM.  SR.NO.OF STATEMENT
C224724  3035  24.09.037  MARCH-2019  252399
BRTU(3II)/CANDIDATE'SFULLNAME(SURNAMEFIRST)
Chougule Kundalik Abarao
 GAGIRII/CANDIDATE'SMOTHER'SNAME Vanita
/MaksorGradeObtained
Subject Code No.and Subject Name  Max.  /InWords
Marks  InFigures
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
Percentage  Total Marks  FORTYTHREE
Result/f PASS
AdditionalMarksCategory/3faRJuyfDRAWiNG
S191252399
4925577265672
See overleaf for lmportant,Notes,Grades In
School Sublects and meaning of speclal  fmqa/Divisional Secretary
characters.
    """


main(test_cases)