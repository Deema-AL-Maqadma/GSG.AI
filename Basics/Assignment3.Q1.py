#  *** Deema Mohammed AL-Maqadma ***
# ---->>> Assignment 1: Word Counter
# Ask the user for a file name.
# Count and display the number of words in the file.
# Also, identify the most frequent word and how many times it appears.

with open("data.txt","w") as f:
    f.write("Deema Mohammed AL-Maqadma\nlerninng Python with GSG\npython is a high level languagh")
print("*******************************************\n")
def Word_Counter():
    try:
        with open(input("Enter file name : ")) as f:
            words=f.read().lower().split()
        if not words:
            print("File is empty ...")
            return
        most_frequent=words[0]
        max_count=1
        for word in words:
            count=words.count(word)
            if count>max_count:
                max_count=count
                most_frequent=word
        print("Total words in the file : ",len(words))
        print("Most frequent word : ",most_frequent," -> ",max_count," times")
    except FileNotFoundError:
        print("Error ! file not found ...")

Word_Counter()
print("*******************************************\n")
# حل اخر من احمد 
filename = input("Enter The File Name: ")

with open(filename, "r") as file:
    text = file.read()

words = text.split()

clean_words = []
for word in words:
    word = word.strip()
    clean_words.append(word)

total_words = len(clean_words)
print("Number Of Words In The File: ", total_words)

word_count = {}
for word in clean_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_common = max(word_count, key=word_count.get)
max_count = word_count[most_common]
if max_count>1:
 print("Most Frequent Word: ", most_common)
 print("Repeated: ", word_count[most_common], "Time")
else :
    print("No Frequent ....")
print("\n**************************************\n")
