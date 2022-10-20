import random
from utils import Status
from Display import Display


class Wordle:

    def __init__(self):
        with open("data/words.txt") as f:
            self.words = set(f.read().upper().splitlines())
            self.word = random.choice(tuple(self.words)).upper()
            self.guesses = []

    def show(self):
        print(self.word)

    def check_correct(self, guess):
        res = []
        word = [[letter, False] for letter in self.word]

        for i in range(len(word)):
            status = Status.WRONG

            if word[i][0] == guess[i]:
                status = Status.CORRECT
                word[i][1] = True

            elif guess[i] in self.word:
                index = self.word.index(guess[i])
                if self.word[index] != guess[index]:
                    for j in range(len(word)):
                        if guess[i] == word[j][0] and not word[j][1]:
                            status = Status.MISPLACED
                            word[j][1] = True

            res.append((guess[i], status))
        return res

    def won(self):
        if len(self.guesses) > 0:
            if self.word.upper() == self.guesses[-1].upper():
                return True
            return False

    def play(self):
        d = Display()
        d.clear()

        while not self.won() and len(self.guesses) < 6:
            accepted_guess = False
            new_guess = ""
            while not accepted_guess:
                new_guess = input("Type your guess: ")
                if len(new_guess) == 5 and new_guess.upper() in self.words:
                    accepted_guess = True
                else:
                    print("Invalid guess")

            self.guesses.append(new_guess.upper())
            d.clear()
            for g in self.guesses:
                d.show(self.check_correct(g))

        if self.won():
            print("Congrats!🎉")
        else:
            print(f"Better luck next time! The word was {self.word}")

    def guess(self, word):
        d = Display()
        d.clear()
        if word.upper() not in self.words:
            print("Error: guess not allowed")
            return
        self.guesses.append(word.upper())
        d.clear()
        for g in self.guesses:
            d.show(self.check_correct(g))
        return self.check_correct(word.upper())
