import random
import sys
from codebreaker_lib import codebreaker
import output_cli

class codebreaker_wrapper(object):
    def __init__(self, input=sys.stdin, output=output_cli.OutputCli(sys.stdout)):
        self.input = input
        self.output = output
        self.isPlaying=False

        self.cb = codebreaker(self.output)

    def new_game(self):
        self.isPlaying=True
        self.cb.start(self.generate_secret())
        return self

    def start(self):
        while self.isPlaying:
            self.next_guess()

    def next_guess(self):
        guess = self.input.readline()
        self.cb.guess(guess)
        if self.cb.has_won(guess):
            self.output.report_win()
            self.isPlaying = False

    def generate_secret(self):
        choices = list("123456")
        secret = ""
        for _ in xrange(0, 4):
            r = self.randrange(len(choices))
            secret += choices[r]
            del choices[r]
        return secret

    def randrange(self, size):
        return random.randrange(size)