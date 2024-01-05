def levenshtein_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[m][n]

def find_subject(text, subjects):
    words = text.split()
    identified_subjects = []

    for subject in subjects:
        distances = [levenshtein_distance(word, subject) for word in words]
        min_distance = min(distances)
        if min_distance < 3:  # Adjust the threshold as needed
            identified_subjects.append(subject)

    return identified_subjects

text = """
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
"""
cbse_subjects = ["ENGLISH", "HINDI", "MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE", "PHYSICS", "CHEMISTRY", "BIOLOGY", "COMPUTER SCIENCE", "INFORMATICS PRACTICES", "PHYSICAL EDUCATION", "ECONOMICS", "ACCOUNTANCY", "BUSINESS STUDIES", "POLITICAL SCIENCE", "HISTORY", "GEOGRAPHY", "PSYCHOLOGY", "SOCIOLOGY", "PHILOSOPHY", "HOME SCIENCE", "PHYSICAL EDUCATION", "ENTREPRENEURSHIP", "BIOTECHNOLOGY", "MULTIMEDIA AND WEB TECHNOLOGY", "ENGINEERING GRAPHICS", "INFORMATICS PRAC. (OLD)", "COMPUTER SCIENCE (OLD)", "MATHS", "ENGLISH CORE", "ENGLISH ELECTIVE", "HINDI CORE", "HINDI ELECTIVE", "FRENCH", "GERMAN", "SPANISH", "SANSKRIT CORE", "SANSKRIT ELECTIVE", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU CORE", "URDU ELECTIVE", "SOCIAL SCIENCES", "SCIENCE & TECHNOLOGY", "HEALTH & PHYSICAL EDUCATION", "SCOUTING/GUIDING", "SELFDEVELOPMENT & ART APPRE."]

identified_subjects = find_subject(text, cbse_subjects)
for subject in identified_subjects:
    print(subject)
