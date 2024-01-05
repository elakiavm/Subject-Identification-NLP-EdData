import re
import nltk
from nltk.metrics import jaccard_distance

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

def process_test_cases(test_cases, primary_subjects):
    for i, test_case in enumerate(test_cases, start=1):
        print(f"\nProcessing Test Case {i}:")
        
        # Process the current test case
        identified_primary_subjects = find_primary_subject(test_case, primary_subjects)

        # Display results only if subjects are identified
        if identified_primary_subjects:
            print("Primary Subjects:")
            for subject in identified_primary_subjects:
                print(subject)

# Test cases as an array
test_cases_array = [
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
    """
    # Add more test cases as needed
]

# Define primary subjects
primary_subjects_array = ["MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE"]

# Process test cases
process_test_cases(test_cases_array, primary_subjects_array)
