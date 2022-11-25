import random

wordList = list()
with open("words.txt",encoding="utf-8") as file:
    for line in file.readlines():
        word = ""
        for letter in line:
            word += letter
            if(" " in word):
                word = word.strip()
                word = word.strip(",")
                word = word.strip("?")
                word = word.strip('"')
                wordList.append(word)
                word = ""


def writeSong():
    word = 0
    verse = 0

    song = str("\n")
    for i in range(1,40):
        if(word == 4):
            song += "\n"
            word = 0
            verse +=1
        choosenWord = random.choice(wordList)

        if(verse == 4):
            song += "\n"
            verse = 0
        song += choosenWord+" "
        word+=1
    return song

print(writeSong())