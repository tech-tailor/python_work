import random

class Guessing_game:
    def __init__(self, start_range, end_range):
        self.start_range = start_range
        self.end_range = end_range
        self.no_of_attempts = 0
        self.random_num = 0

    def generate_random_num(self):
        self.random_num = random.randint(self.start_range, self.end_range )
        print(f'the generated random number is: {self.random_num}')

    def user_input(self):
        return int(input(f'Enter a Guess between {self.start_range} and {self.end_range}\n'))

    

    def play_game(self):
        self.generate_random_num()
        while True:
            guess = Game.user_input()
            self.no_of_attempts += 1
            print(self.no_of_attempts)
            print(self.random_num)

            if guess == self.random_num:
                print(f'Congratulations')






Game = Guessing_game(15, 16)
guess = Game.play_game()