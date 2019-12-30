# Напишите функцию которая находит самою длинную слово в строке"

sentence = "My name is Kanat and surname Nadyrbekov"
print(sentence)
word = sentence.split()
longest = 0

for i in range(0,len(word)):
    if len(word[longest]) < len(word[i]):
        longest = i
print(word[longest])


# str_ = "python java c c++ javascript pascal php"
# print(str)

# listWords = str_.split()

# LongestWord = 0

# for i in range(1,len(listWords)):
#     if len(listWords[LongestWord]) < len(listWords[i]):
#         LongestWord = i

# print(listWords[LongestWord])

