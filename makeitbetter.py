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
        average_distance = sum(distances) / len(distances) if distances else float('inf')

        # Adjust the threshold as needed
        threshold = min(len(subject) / 2, 3)

        if average_distance <= threshold:
            identified_subjects.append(subject)

    return identified_subjects

text = "101 ENGLISH COMM. 053 019 072 SEVENTYTWO C2 002 HINDI COURSE-A 056 019 075 SEVENTYFIVE C1 041 MATHEMATICS 028 019 047 FORTYSEVEN C2 086 SCIENCE 014 019 033 THIRTY THREE D2 087 SOCIAL SCIENCE 047 019 066 SIXTYSIX C1 ADDITIONAL SUBJECT 034 HIND.MUSICVOCAL 009 074 083 EIGHTYTHREE C2"
cbse_subjects = ["ENGLISH", "HINDI", "MATHEMATICS", "SCIENCE", "SOCIAL SCIENCE", "PHYSICS", "CHEMISTRY", "BIOLOGY", "COMPUTER SCIENCE", "INFORMATICS PRACTICES", "PHYSICAL EDUCATION", "ECONOMICS", "ACCOUNTANCY", "BUSINESS STUDIES", "POLITICAL SCIENCE", "HISTORY", "GEOGRAPHY", "PSYCHOLOGY", "SOCIOLOGY", "PHILOSOPHY", "HOME SCIENCE", "PHYSICAL EDUCATION", "ENTREPRENEURSHIP", "BIOTECHNOLOGY", "MULTIMEDIA AND WEB TECHNOLOGY", "ENGINEERING GRAPHICS", "INFORMATICS PRAC. (OLD)", "COMPUTER SCIENCE (OLD)", "MATHS", "ENGLISH CORE", "ENGLISH ELECTIVE", "HINDI CORE", "HINDI ELECTIVE", "FRENCH", "GERMAN", "SPANISH", "SANSKRIT CORE", "SANSKRIT ELECTIVE", "ARABIC", "TAMIL", "TELUGU", "MALAYALAM", "ODIA", "ASSAMESE", "BENGALI", "GUJARATI", "KANNADA", "MARATHI", "PUNJABI", "URDU CORE", "URDU ELECTIVE", "SOCIAL SCIENCES", "SCIENCE & TECHNOLOGY", "HEALTH & PHYSICAL EDUCATION", "SCOUTING/GUIDING", "SELFDEVELOPMENT & ART APPRE."]

identified_subjects = find_subject(text, cbse_subjects)
print("Identified CBSE Subjects:")
for subject in identified_subjects:
    print(subject)
