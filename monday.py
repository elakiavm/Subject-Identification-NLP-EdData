# from difflib import get_close_matches

# def replace_subjects(input_text, primary_subjects_array, language_subjects_array):
#     output_text = ""
    
#     for line in input_text.split("\n"):
#         words = line.split()
#         replaced_words = []
        
#         for word in words:
#             if word.isalpha():
#                 # Check if the word is a primary subject
#                 if word.upper() in primary_subjects_array:
#                     replaced_words.append(word.upper())
#                 else:
#                     # Find the closest match in the language subjects array
#                     closest_match = get_close_matches(word.upper(), language_subjects_array, n=1, cutoff=0.5)
#                     if closest_match:
#                         replaced_words.append(closest_match[0])
#                     else:
#                         replaced_words.append(word)
#             else:
#                 replaced_words.append(word)
        
#         output_text += " ".join(replaced_words) + "\n"
    
#     return output_text

# # Test case
# input_text = """
# (5) Gujarat – 12523
# 中 CUJAAATI FL 25 078 SEVEN EIOHT
# 10 SOCIALSCIENCE 53 2S O70 SEVEN ELGHT
# SEIEMCL TECHNO 48 76 OT4 SEVEH TOUR
# 1E PATHEHATICE 57 3 EIGHT ZERD
# 店 ENOLISH SL 45 25 070 SEVEN ZEHO
# BANSKRIT BL 4 26 075 SEVEN FIVE 中
# """

# primary_subjects_array = ["MATHEMATICS", "SCIENCE","SCIENCE TECHNO", "SOCIAL SCIENCE"]
# language_subjects_array = ["ENGLISH","HINDI COURSE", "HINDI", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

# output_text = replace_subjects(input_text, primary_subjects_array, language_subjects_array)
# print(output_text)

# # input_text = """
# (5) Gujarat – 12523
# 中 CUJAAATI FL 25 078 SEVEN EIOHT
# 10 SOCIALSCIENCE 53 2S O70 SEVEN ELGHT
# SEIEMCL TECHNO 48 76 OT4 SEVEH TOUR
# 1E PATHEHATICE 57 3 EIGHT ZERD
# 店 ENOLISH SL 45 25 070 SEVEN ZEHO
# BANSKRIT BL 4 26 075 SEVEN FIVE 中
# """

# primary_subjects_array = ["MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE"]
# language_subjects_array = ["ENGLISH","HINDI COURSE", "HINDI", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]


# def jaccard_similarity(str1, str2):
#     set1 = set(str1)
#     set2 = set(str2)
#     intersection = len(set1.intersection(set2))
#     union = len(set1) + len(set2) - intersection
#     return intersection / union


# output_text = ""
# lines = input_text.split("\n")
# for line in lines:
#     words = line.split()
#     output_line = ""
#     for word in words:
#         max_similarity = 0
#         identified_subject = ""
#         for subject in primary_subjects_array + language_subjects_array:
#             similarity = jaccard_similarity(word, subject)
#             if similarity > max_similarity:
#                 max_similarity = similarity
#                 identified_subject = subject
#         output_line += identified_subject + " "
#     output_text += output_line.strip() + "\n"

# print(output_text)


# from difflib import get_close_matches
# from collections import Counter


# def replace_subjects_jaccard(input_text, primary_subjects_array, language_subjects_array):
#     output_text = ""

#     for line in input_text.split("\n"):
#         words = line.split()
#         replaced_words = []

#         for word in words:
#             if word.isalpha():
#                 # Check if the word is a primary subject
#                 if word.upper() in primary_subjects_array:
#                     replaced_words.append(word.upper())
#                 else:
#                     # Find the closest match in the language subjects array using Jaccard similarity
#                     max_similarity = 0
#                     closest_match = None
#                     for subject in language_subjects_array:
#                         intersection = len(Counter(word.upper()) & Counter(subject))
#                         union = len(Counter(word.upper()) | Counter(subject))
#                         similarity = intersection / union if union else 0
#                         if similarity > max_similarity:
#                             max_similarity = similarity
#                             closest_match = subject

#                     if closest_match:
#                         replaced_words.append(closest_match)
#                     else:
#                         replaced_words.append(word)
#             else:
#                 replaced_words.append(word)

#         output_text += " ".join(replaced_words) + "\n"

#     return output_text


# # Test case
# input_text = """
# (5) Gujarat – 12523
# 中 CUJAAATI FL 25 078 SEVEN EIOHT
# 10 SOCIALSCIENCE 53 2S O70 SEVEN ELGHT
# SEIEMCL TECHNO 48 76 OT4 SEVEH TOUR
# 1E PATHEHATICE 57 3 EIGHT ZERD
# 店 ENOLISH SL 45 25 070 SEVEN ZEHO
# BANSKRIT BL 4 26 075 SEVEN FIVE 中
# """

# primary_subjects_array = ["MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE","ENGLISH"]
# language_subjects_array = [ "HINDI COURSE", "HINDI", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

# output_text = replace_subjects_jaccard(input_text, primary_subjects_array, language_subjects_array)
# print(output_text)



import re
from difflib import get_close_matches

def replace_subjects(input_text, primary_subjects_array, language_subjects_array):
    output_text = ""
    
    for line in input_text.split("\n"):
        replaced_line = line

        # Add your subject replacement code here
        replaced_line = re.sub(r"HINDI COURSE(-A|B|-B|-COURSE|-COURSE-A)", "HINDI", replaced_line)
        replaced_line = re.sub(r"SCIENCE (& TECHNOLOGY|THEORY|TECHNO)", "SCIENCE", replaced_line)
        replaced_line = re.sub(r"MATHEMATICS STANDARD", "MATHEMATICS", replaced_line)
        replaced_line = re.sub(r"ENGLISHLNG&LIT\.|ENGLISH COMM", "ENGLISH", replaced_line)
        replaced_line = re.sub(r"ENGLISH & LIT", "ENGLISH", replaced_line)

        words = replaced_line.split()
        replaced_words = []
        
        for word in words:
            if word.isalpha():
                # Check if the word is a primary subject
                if word.upper() in primary_subjects_array:
                    replaced_words.append(word.upper())
                else:
                    # Find the closest match in the language subjects array
                    closest_match = get_close_matches(word.upper(), language_subjects_array, n=1, cutoff=0.7)
                    if closest_match:
                        replaced_words.append(closest_match[0])
                    else:
                        replaced_words.append(word)
            else:
                replaced_words.append(word)
        
        output_text += " ".join(replaced_words) + "\n"
    
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

primary_subjects_array = ["MATHEMATICS", "SCIENCE", "SCIENCE TECHNO", "SOCIAL SCIENCE"]
language_subjects_array = ["ENGLISH", "HINDI COURSE", "HINDI", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

output_text = replace_subjects(input_text, primary_subjects_array, language_subjects_array)
print(output_text)
