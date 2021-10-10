sentence = input("Введите слова разделенные точкой запятой: ")
longest = max(sentence.split(), key=len)
print("Самое длинное слово с точкой запятой: ", longest)
print("Длина слова = ", len(longest)-1)