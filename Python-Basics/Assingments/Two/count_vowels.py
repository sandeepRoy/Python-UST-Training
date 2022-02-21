def vowels_counter(word):
    vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count_vowels = 0
    for index in word:
        if index in vowel:
            count_vowels += 1
    return count_vowels

def each_vowel_counter(word, vowel_choice):
   count_vowels = 0
   vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
   if vowel_choice in vowel:
       for index in word:
           if index == vowel_choice:
               count_vowels = count_vowels + 1
   else:
       count_vowels = "0"
   return count_vowels

if __name__ == "__main__":
    word = input()
    count_vowels = vowels_counter(word)
    print("Total Vowels:",count_vowels)
    vowel_choice = input("Vowel: ")
    count_each_vowel = each_vowel_counter(word, vowel_choice)
    print("Count of",vowel_choice,":",count_each_vowel,"times")