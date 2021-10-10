sentence = input("введите предложение: ")
longest = max(sentence.split(), key=len)
print("Самое длинное слово", longest)
print("Его длина = ", len(longest))