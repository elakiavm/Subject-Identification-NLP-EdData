from difflib import get_close_matches

def identify_cbse_subjects(input_text, cbse_subjects):
    identified_subjects = []

    for word in input_text.split():
        closest_matches = get_close_matches(word, cbse_subjects, n=1, cutoff=0.8)
        if closest_matches:
            identified_subjects.append(closest_matches[0])

    return identified_subjects

# Example usage
input_text = """

"""

identified_subjects = identify_cbse_subjects(input_text, cbse_subjects)
print("Identified CBSE Subjects:", identified_subjects)
