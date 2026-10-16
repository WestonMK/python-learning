def analyze_sentence(sentence):
    sentence = sentence.strip()

sentence = input("Enter a sentence: ")
total_chars = len(sentence)
words = sentence.split()
total_words = len(words)
vowels = set("aeiouAEIOU")
non_space_chars = sum(1 for ch in sentence if ch !=' ')
avg_word_length = non_space_chars / total_words if total_words > 0 else 0
first_word = words[0] if total_words > 0 else ""
last_word = words[-1] if total_words > 0 else ""
reverse = sentence[::-1]

print("\nSentence Analysis:")
print(f"Total Chars: {total_chars}")
print (f"Total words: {total_words}")
print (f"Vowels: {vowels}")
print (f"Non-Space Chars: {non_space_chars}")
print (f"Average Word Lenght: {avg_word_length}")
print (f"First Word: {first_word}")
print (f"Last Word: {last_word}")
print (f"Reversed: {reverse}")

if __name__ == "__main__":
    try:
        sentence = input("Enter a multi-word sentence: ")
        analyze_sentence(sentence)
    except Exception as e:
        print(f"An error occurred: {e}")
