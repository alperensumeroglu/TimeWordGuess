"""
Project Name: Timed Word Guessing Game
Project Description:
The Timed Word Guessing Game is a fun and interactive game where players must guess the hidden word within a limited time. Players select words from different categories and earn points for correct guesses while losing points for incorrect ones. The time-limited mode adds an extra challenge, and the scoring system motivates players to achieve high scores by making accurate guesses.
Features:
Timed Mode: Players have a limited amount of time to guess each word. If the word is not guessed before time runs out, the game ends.
Scoring System: Players earn points for correct guesses and lose points for wrong ones. The score resets with each new game.
Word Categories: Players can choose from different word categories (Animals, Fruits, Countries, etc.) to play the game.
User-Friendly Interface: The game provides helpful feedback and error messages, ensuring players are guided through their guesses in an intuitive and engaging way.
This description highlights your project as a competitive, educational, and entertaining game!
"""
import random
import time

word_categories = {
    'Animals': ['lion', 'tiger', 'elephant', 'giraffe', 'penguin'],
    'Fruits': ['apple', 'banana', 'grape', 'watermelon', 'pineapple'],
    'Countries': ['Turkey', 'Germany', 'India', 'Australia', 'Brazil'],
}

def choose_category():
    print('Categories: ', ', '.join(word_categories.keys()))
    while True:
        category = input('Choose a category: ')
        if category in word_categories:
            return random.choice(word_categories[category])
        else:
            print('Invalid category. Please choose again.')

    
def choose_word():
    words = ['python', 'java', 'kotlin', 'javascript', 'typescript']
    return random.choice(words)

def display_word(word, guesses):
    displayed = ''.join(letter if letter in guesses else '_' for letter in word)
    return displayed

def calculate_score(attempts_left, word_length):
    return attempts_left * word_length

def play_game():
    word = choose_word()
    attempts = 6
    guessed_letters = []
    score = 0
    time_limit = 30

    print('Welcome to the Word Guessing Game!')
    print('You have {attempts} attempts to guess the word and 30 seconds to finish the game..')

    start_time = time.time()
    
    while attempts > 0:
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print(f"Time's up! The word was: {word}")
            break

        print('\n' + display_word(word, guessed_letters))
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print('Good guess !')
            score += 10
        else:
            attempts -= 1
            print(f'Wrong guess! You have {attempts} attempts left.')
            score -= 5
        if all(letter in guessed_letters for letter in word):
            score += calculate_score(attempts, len(word))
            print(f"Congratulations! You've guessed the word: {word}")
            print(f"Your final score is: {score}")
            break
    else:
         print(f'Game over! The word was: {word}')
         print(f'Your final score is: {score}')
if __name__ ==  "__main__":
    play_game()