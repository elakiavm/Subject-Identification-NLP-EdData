import re
import nltk
from nltk.metrics import edit_distance

def remove_numbers(text):
    return re.sub(r'\d', '', text)

def correct_spacing(input_text):
    # Add space between camel-case words
    input_text = re.sub('([a-z])([A-Z])', r'\1 \2', input_text)
    
    # Define patterns for subjects and numerical values
    subject_pattern = re.compile(r'\b(MARATHI|HINDI|ENGLISH|MATH|SCIENCE&TECHNOLOGY|SOCIAL SCIENCES|HEALTH&PHYSICALEDUCATION|SCOUTING/GUIDING|SELF DEVELOPMENT&ART APPRE|SANSKRIT)\b', re.IGNORECASE)
    numerical_value_pattern = re.compile(r'\b(\d{2,3})\b')

    # Replace missing spaces for subjects and numerical values while preserving existing spaces
    corrected_text = re.sub(numerical_value_pattern, r' \1 ', input_text)
    corrected_text = re.sub(subject_pattern, r' \1 ', corrected_text)

    # Remove extra spaces and trim the text
    corrected_text = ' '.join(corrected_text.split())
    
    return corrected_text
def calculate_jaccard_similarity(set1, set2):
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))
    return 1.0 - (intersection_size / union_size) if union_size != 0 else 0.0

def find_primary_subject(text, primary_subjects):
    text_without_numbers = remove_numbers(text)
    corrected_text = correct_spacing(text_without_numbers.upper())  # Convert to uppercase
    
    words = nltk.word_tokenize(corrected_text)
    identified_primary_subjects = set()

    for primary_subject in primary_subjects:
        primary_subject_words = set(nltk.word_tokenize(primary_subject))
        
        # Check if the subject is already identified
        if primary_subject in identified_primary_subjects:
            continue
        
        for i in range(len(words) - len(primary_subject_words) + 1):
            word_subset = words[i:i + len(primary_subject_words)]
            subset_set = set(word_subset)
            
            # Calculate Jaccard similarity as Jaccard distance (1 - similarity)
            similarity = calculate_jaccard_similarity(primary_subject_words, subset_set)
            
            # If the similarity is above a certain value, consider it a match
            if similarity > 0.7:
                identified_primary_subjects.add(primary_subject)
                break  # Break the inner loop to avoid rechecking for the same subject

    return list(identified_primary_subjects)

def calculate_dynamic_threshold(subject, word):
    max_length = max(len(subject), len(word))
    return 1.0 - (edit_distance(subject, word) / max_length)

def find_language_subjects(text, language_subjects):
    text_without_numbers = remove_numbers(text)
    corrected_text = correct_spacing(text_without_numbers.upper())  # Convert to uppercase
    
    words = nltk.word_tokenize(corrected_text)
    identified_subjects = set()

    for primary_subject in language_subjects:
        primary_subject_words = nltk.word_tokenize(primary_subject)
        for word in words:
            threshold = calculate_dynamic_threshold(primary_subject, word)
            if threshold > 0.5:  # Adjust the threshold for better accuracy
                identified_subjects.add(primary_subject)

    return list(identified_subjects)

def process_test_cases(test_cases, primary_subjects, language_subjects):
    for i, test_case in enumerate(test_cases, start=1):
        print(f"\nProcessing Test Case {i}:")
        
        # Process the current test case
        identified_primary_subjects = find_primary_subject(test_case, primary_subjects)
        identified_language_subjects = find_language_subjects(test_case, language_subjects)

        # Display results only if subjects are identified
        if identified_primary_subjects:
            print("Primary Subjects:")
            for subject in identified_primary_subjects:
                print(subject)

        if identified_language_subjects:
            print("\nLanguage Subjects:")
            for subject in identified_language_subjects:
                print(subject)

# Test cases as an array
test_cases_array = [
    """
    (I) Bihar – 1264
      101  ENGLISH COMM.  071  020  091 NINETYONE  A2
      069  020  089 EIGHTYNINE  A2
      085  HINDI COURSE-B  020  020  040  FORTY D1
      041  MATHEMATICS  039  020  059 FIFTYNINE  B2
      086  SCIENCE  073  020  093 NINETY THREE  A1
      087  SOCIAL SCIENCE
    """,
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
    """
    (4) Delhi – 12373
      184  ENGLISHLNG&LIT. 039  020  059  FIFTY NINE  D1
      002  HINDI COURSE-A 059  020  079  SEVENTY NINE  B2
      041  MATHEMATICS STANDARD  070 020  090  NINETY  A2
      086  SCIENCE-THEORY  061 020  081  EIGHTY ONE  A2
      087  SOCIAL SCIENCE 060  020  080  EIGHTY  B2
      ADDITIONAL SUBJECT
      402  INFORMATIONTECHNOLOGY 047  050  097  NINETY SEVEN  A1
    """,
    """
    (5) Gujarat – 12523
      中  CUJAAATI FL 25  078  SEVEN EIOHT
      10  SOCIALSCIENCE  53 2S  O70  SEVEN ELGHT
      SEIEMCL  TECHNO  48 76  OT4  SEVEH TOUR
      1E  PATHEHATICE 57  3  EIGHT ZERD
      店  ENOLISH SL 45  25  070  SEVEN ZEHO
      BANSKRIT BL  4  26  075  SEVEN FIVE  中
    """,
    """
    (6) Gujarat – 121663
      083  EIGHT THREE A2
      02 HINDI FL  66  17  A2
      10  SOCIAL SCIENCE  66 19  085  EIGHT FIVE
      EIGHT SIX A2
      11  SCIENCE 68  18  086
      089  EIGHT NINE A2
      12  MATHEMATICS 70  19  B1
      13  GUJARATI SL  56  17 073  SEVEN THREE
      60  18  078  SEVEN EIGHT B1
      16  ENGLISH SL
    """,
    """
    (7) Haryana – 12132
      HINDI 048  33  100  C  03
      2  ENGLISH  056 33  100  B  06
      3  MATHEMATICS  044  33 100  C+  04
      4  SOCIAL SCIENCE  043 33  100  C  03
      062  33  100 B-  05
      5  SCIENCE
      6  SANSKRIT 050  33  100  C+  04
    """,
    """
    (8) HP – 12312
      》 Erglish  98*  100
      12.  Mathematcs  51*  100
      3. Hindi  83  100
      Social 5clence [His.Civ.Geog.)  91*  100
      4
      Sriente & Technology  W/P 67/25  92*  100
      5  (Phy. Chem. Life Scl.)
      Sanskrit 95*  100
      6.
      Computer Stience (Elective)  W/P 47/50 97+  100
      7.
    """,
    """
    (9) HP – 12618
      1  English"  85*  100
      2.  Mathematics 100*  100
      3. Hindi  98*  100
      4 Social Science(His.Civ.Geog.)  98*  100
      Science&Technology  (Phy.Chem.Life Sci.)  W/P73/25  98*  100
      6. Sanskrit  83#  100
      7.  Art(Elective)  W/P65/35  100*  100
    """,
    """
    (10) HP – 121426
      1.  English  47  100
      Mathematics  60  100
      3.  Hindi  50  100
      Social Science (His.Civ.Geog.)  43  100
      4.
      Science&Technology  W/P35/15  50  100
      5.  (Phy.Chem.Life Sci.)
      6. Sanskrit  60  100
      7.  Computer Science(Elective) W/P37/47  84*  100
    """,
    """
    (11) HP – 121757
      1.  English  73  100
      2  Mathematics  53  100
      3.  Hindi  56  100
      4. Social Science(His.Civ.Geog.)  72  100
      Science & Technology  W/P36/24
      5.  (Phy.Chem.Life Sci.)  60  100
      6.  Sanskrit  78*  100
      7. Art(Elective)  W/P53/34  87*  100
    """
    # Add more test cases as needed
]


# Define primary subjects and language subjects
primary_subjects_array = ["MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE"]
language_subjects_array = ["ENGLISH", "HINDI", "SANSKRIT", "FRENCH", "GERMAN", "SPANISH", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU"]

# Process test cases
process_test_cases(test_cases_array, primary_subjects_array, language_subjects_array)
