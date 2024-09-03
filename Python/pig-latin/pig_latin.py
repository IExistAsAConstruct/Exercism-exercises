vowels = ['a', 'e', 'i', 'o', 'u']

def rule_1(word) -> str:
    return word + "ay"

def rule_2(word) -> str:
    for i in range(len(word)):
        if word[i] in vowels:
            print(word[i])
            stripped_word = word[i:]
            return stripped_word + word[:i] + "ay"

def rule_3(word) -> str:
    characters = "qu"
    index = word.find(characters)
    if index != -1:
        stripped_word = word[index + 2:]
        return stripped_word + word[:index + 2] + "ay"

def rule_4(word) -> str:
    for i in range(len(word)):
        if word[i] in vowels or (word[i] == "y" and i > 0):
            return word[i:] + word[:i] + "ay"

def translate(text):
    words = text.split() if " " in text else [text]
    answer = []
    for word in words:
        if word[0] in vowels or word[0:2] == "xr" or word[0:2] == "yt":
            pig_latin = rule_1(word)
            print("rule 1:", pig_latin)
            answer.append(pig_latin)
            continue
        if word[0] not in vowels and "qu" not in word and "y" not in word:
            pig_latin = rule_2(word)
            print("rule 2:", pig_latin)
            answer.append(pig_latin)
            continue
        if "qu" in word:
            pig_latin = rule_3(word)
            print("rule 3:", pig_latin)
            answer.append(pig_latin)
            continue
        if "y" in word and word[0] not in vowels:
            pig_latin = rule_4(word)
            print("rule 4:", pig_latin)
            answer.append(pig_latin)
            continue
    print(answer)
    answer = " ".join(answer) if len(answer) > 1 else answer[0]
    return answer