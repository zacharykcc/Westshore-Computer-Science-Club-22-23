def calculate_word_value(word, value_of_a):
    total_value = 0
    for letter in word:
        letter_value = ord(letter) - ord('A') + value_of_a
        if letter_value > 26:
            letter_value -= 26
        total_value += letter_value
    return total_value

def main():
    with open("input.txt", "r") as file:
        num_test_cases = int(file.readline().strip())
        
        for test_case_number in range(1, num_test_cases + 1):
            value_of_a, num_words = map(int, file.readline().split())
            winner_found = False
            winner_word = ""
            
            for word_number in range(1, num_words + 1):
                word = file.readline().strip()
                word_value = calculate_word_value(word, value_of_a)
                
                if word_value == 100:
                    winner_found = True
                    winner_word = word
            
            if winner_found:
                print(f"WINNER {word_number}: {winner_word}")

if __name__ == "__main__":
    main()