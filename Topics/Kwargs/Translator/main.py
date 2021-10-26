def translate(**kwargs):
    for word, translation in kwargs.items():
        print(word, ":", translation)


words = {"mother": "madre", "father": "padre", 
         "grandmother": "abuela", "grandfather": "abuelo"}

translate(**words)
