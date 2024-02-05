# Subject-Identification-NLP-EdData
<<<<<<< HEAD

**Title: Automated Subject Identification in Educational Test Cases**

**Title: Streamlining Subject Recognition in Educational Test Cases**

**Introduction:**

In the world of educational assessments and exam processing, manually pinpointing subjects within test cases can be a tedious and error-prone endeavor. This Python code addresses this issue by introducing an automated solution tailored for educational test cases, with a special emphasis on subjects outlined by the Central Board of Secondary Education (CBSE) in India.

**Problem Statement:**

Educational test cases often come in various formats, exhibit spelling variations, and feature inconsistent spacing, making manual subject identification laborious. This code aims to tackle these challenges by automating the identification of primary subjects (e.g., Mathematics, Science, Social Science) and language subjects (e.g., English, Hindi, Sanskrit) within CBSE test cases.

**Objective:**

The primary goal of this code is to deliver an efficient and accurate tool for subject identification within the CBSE system. Leveraging techniques like Jaccard similarity and Levenshtein edit distance, the code aims to achieve precise subject identification, even in scenarios with variations in spelling, spacing, or formatting.

**Scope:**

This code is tailored specifically for the CBSE system, accommodating a variety of test case formats and styles. Although the current focus is on CBSE subjects, the underlying techniques are versatile and could potentially be applied to other educational systems.

**Overview of Approach:**

The code utilizes a combination of Jaccard similarity for primary subject identification and Levenshtein edit distance for language subject identification. By tokenizing and comparing words, it adeptly navigates through complexities introduced by variations in spelling and formatting, providing a robust automated solution for subject identification.

**Combined and Modified Report on CBSE Subject Identification**

---

### **Introduction:**
Subject identification from unstructured text poses a unique challenge, given variations in spelling, formatting, and word order. Several attempts have been made to address this challenge, utilizing different libraries and algorithms. In this comprehensive report, we analyze multiple strategies for identifying CBSE subjects from a given text.

---

### **Attempt 1: Using `difflib` Library**

- **Difficulty:**
  - Utilizes the `get_close_matches` function from the `difflib` library.
  - Cutoff parameter set to 0.8 for similarity threshold.
  - May lack robustness to variations.

- **Result:**
  - Identifies subjects based on exact or close matches.
  - Limited handling of variations.

---

### **Attempt 2: Using `fuzzywuzzy` Library**

- **Difficulty:**
  - Utilizes `process.extract` from the `fuzzywuzzy` library.
  - More flexible than `difflib` but may still have limitations.
  - Similarity threshold set to 80.

- **Result:**
  - Improved performance over `difflib`.
  - Handles variations better but not foolproof.

---

### **Attempt 3: Using Levenshtein Distance**

- **Difficulty:**
  - Calculates Levenshtein distance with dynamic threshold.
  - Focuses on edit distance.
  - Threshold may need adjustment.

- **Result:**
  - Resilient to variations.
  - Requires fine-tuning of the threshold.

---

### **Attempt 4: Using Levenshtein Distance with Minimum Distance**

- **Difficulty:**
  - Calculates Levenshtein distance considering minimum distance.
  - Threshold set to 3 for accuracy.
  - Aims to improve identification accuracy.

- **Result:**
  - Improved accuracy compared to previous attempts.
  - Considers minimum distance for each subject.

---

### **Attempt 5: Jaccard Distance and Correct Spacing**

- **Approach:**
  - Uses Jaccard distance.
  - Defines `correct_spacing` function for numerical values.
  - Identifies subjects based on tokenization.

- **Result:**
  - Provides an alternative approach using Jaccard distance.
  - Handles spacing issues.

---

### **Attempt 6: Dynamic Threshold with Jaccard Distance**

- **Enhancement:**
  - Introduces dynamic threshold calculation.
  - Considers subject and word lengths.
  - Uses Jaccard distance for identification.

- **Result:**
  - Adaptive to varying subject lengths.
  - Prints identified subjects.

---

### **Attempt 7: Edit Distance-Based Approach**

- **Innovation:**
  - Utilizes edit distance.
  - Dynamic threshold calculation using `calculate_dynamic_threshold`.
  - Identifies subjects with a new approach.

- **Result:**
  - Offers a unique method for subject identification.
  - Considers edit distance for robustness.

---

### **Attempt 8: Jaccard Similarity with Sliding Window**

- **Exploration:**
  - Introduces a sliding window for Jaccard similarity.
  - Considers word order for subject identification.

- **Result:**
  - Useful in scenarios where word order matters.
  - Prints primary subjects.

---

### **Attempt 9: Dynamic Threshold with Edit Distance and Language Subjects**

- **Extension:**
  - Introduces `calculate_dynamic_threshold` with edit distance.
  - Adds `find_language_subjects` for language subjects.
  - Prints both primary and language subjects.

---

### **Summary and Recommendations:**
- Each attempt employs a distinct approach with varying degrees of success.
- Consideration of subject characteristics, input data, and specific requirements is crucial.
- Fine-tuning of parameters, dynamic threshold calculations, and combining methods may enhance accuracy.
- The choice of technique depends on the context, and further experimentation may lead to an optimal solution.

---

**Code Repository:**
The complete code is available on GitHub. You can access it [here](link-to-github-repository).

---

**Code Explanation:**

This Python code, available on [GitHub](link-to-github-repository), is designed to identify subjects from a given set of test cases, resembling student examination results. The identification is based on a predefined list of primary subjects and language subjects. The code employs text processing, tokenization, and similarity metrics for this purpose.

**Functions and Their Functionality:**

1. **`remove_numbers` function:**
   - Utilizes a regular expression to remove numerical digits from the input text.

2. **`correct_spacing` function:**
   - Corrects spacing issues in the input text.
   - Adds spaces between camel-case words.
   - Handles specific patterns related to subjects and numerical values.
   - Removes extra spaces and trims the text.

3. **`calculate_jaccard_similarity` function:**
   - Computes the Jaccard similarity between two sets.
   - Used for calculating the similarity between sets of words.

4. **`find_primary_subject` function:**
   - Identifies primary subjects based on Jaccard similarity.
   - Tokenizes the corrected text and compares sets of words with sets of primary subject words.
   - Uses a dynamic threshold for similarity to identify subjects.

5. **`calculate_dynamic_threshold` function:**
   - Dynamically calculates the Jaccard similarity threshold based on the length of the subject and word.

6. **`find_language_subjects` function:**
   - Identifies language subjects based on edit distance.
   - Uses a dynamic threshold calculated by the `calculate_dynamic_threshold` function.
   - Tokenizes the corrected text and compares each word with sets of language subject words.

7. **`process_test_cases` function:**
   - Processes a set of test cases.
   - Calls the `find_primary_subject` and `find_language_subjects` functions for each test case.
   - Prints the identified primary and language subjects.

**Test Cases and Subject Lists:**

- Test cases are provided as an array of strings, each representing an examination result.
- Primary subjects and language subjects are defined in separate arrays.

**Processing:**

- The code processes each test case, identifies primary and language subjects, and prints the results.

**Methodology:**

- The methodology involves preprocessing the input text, correcting spacing issues, and applying different similarity metrics for identifying subjects.
- Jaccard similarity is used for primary subjects, while edit distance is used for language subjects.
- Dynamic thresholds are calculated to adapt to varying subject and word lengths.

**Recommendations:**

1. **Threshold Adjustments:**
   - Experiment with adjusting the similarity thresholds in `find_primary_subject` and `find_language_subjects` functions for optimal results.

2. **Additional Subjects:**
   - Extend the code to handle additional subjects if needed, considering variations in subject names.

3. **Performance Tuning:**
   - Fine-tune parameters and consider additional techniques for improved accuracy based on specific input characteristics.

4. **Error Handling:**
   - Implement error handling to gracefully handle unexpected input patterns.

This code provides a foundation for subject identification but may require further refinement based on specific use cases and input variations.
=======
Run final.py 
>>>>>>> 0cfddaaff406d1b80a73671f08628b62688e3bfc
