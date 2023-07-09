import random, time

class Guessing_game:
    def __init__(self, start_range, end_range, no_of_attempts):
        self.start_range = start_range
        self.end_range = end_range
        self.no_of_attempts = no_of_attempts
        self.random_num = None

    def generate_random_num(self):
        self.random_num = random.randint(self.start_range, self.end_range )
        print(f'the generated random number is: {self.random_num}')

    def user_input(self):
        return int(input(f'Enter a Guess between {self.start_range} and {self.end_range}\n'))
           
        

    

    def play_game(self):
        self.generate_random_num()    #to use the random funct, this was called 
        Attempt = 0
        remain_attempt = 3

        while True:
            guess = Game.user_input()
            Attempt += 1
            remain_attempt -= 1
            print(f'you have {remain_attempt} Rounds to guess the correct Number')
            


            if guess == self.random_num:
                print(f'Congratulations')
                break

            elif guess > self.random_num:
                print(f'guess too high')

            else:
                print(f'guess too low')

            if Attempt == self.no_of_attempts:
                break






Game = Guessing_game(0, 5, 3)
guess = Game.play_game()