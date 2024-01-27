# Number Guessing game
'''
The program will generate a random number, user has to guess the number based on the hints provided. The program will hint if the guessed number is lt or gt the number
'''

from random import randint

desired_num = randint(0, 100)
#
# while True:
#     num = int(input('Enter your guess: '))
#     if num > desired_num:
#         print('Your guess was higher')
#     elif num < desired_num:
#         print('Your guess was lower.')
#     else:
#         print('Your guess was correct.')
#         break


class Game:
    def __init__(self, desired_num):
        self.desired_num = desired_num

    def run(self):
        while True:
            num = int(input('Enter your guess: '))
            is_guess_correct = self.process_guess(num)
            if is_guess_correct:
                break

    def process_guess(self, guessed_num):
        if guessed_num == self.desired_num:
            return True
        elif guessed_num > desired_num:
            print('Your guess was higher')
        elif guessed_num < desired_num:
            print('Your guess was lower.')


if __name__ == '__main__':
    game_obj = Game(desired_num)
    game_obj.run()
