import random
from words_list import words


def get_valid_word():
    word = random.choice(words)
    return str(word).upper()


def hangman():
    chosen_word = get_valid_word()
    print(chosen_word)
    word_letters = set(chosen_word)
    used_letters = set()
    while len(word_letters) > 0:
        guessed_letter = input('guess a letter').upper()
        used_letters.add(guessed_letter)
        print('used letters:: ' + ' '.join(used_letters))
        show_letters = [letter if letter in used_letters else '-' for letter in chosen_word]
        print(' '.join(show_letters))
        if guessed_letter in word_letters:
            word_letters.remove(guessed_letter)
            print(word_letters)

    print('correct guess')


hangman()
