import json
import os
import random


class Vocabulary:
    """
    Handle loading in a JSON file with proper unfinished swears in it!
    """

    def read_json(path, mode='r'):
        with open(path, mode=mode) as handle:
            return json.load(handle)


class EpithetGenerator:
    """
    Generate a random Shakespeare-like insult.
    """

    def __init__(self, path=os.path.join("resources","data.json")):
        self.set_vocab(path)

    def set_vocab(self, path):
        """
        Reads a json file and sets it as the vocabulary for the instance.
        """
        self.vocab = Vocabulary.read_json(path)

    def get_random_words(self):
        """
        Returns a string of one epithet by random choosing one 
        word from each column in the vocabulary. 
        """

        random_word_1 = random.choice(self.vocab['Column 1'])
        random_word_2 = random.choice(self.vocab['Column 2'])
        random_word_3 = random.choice(self.vocab['Column 3'])
        return (f'{random_word_1} {random_word_2} {random_word_3}')

    def get_epithets(self, qty=1):
        """
        Returns a list of epithets.
        """

        result = [''] * qty
        return [self.get_random_words() for item in result]


    def get_random_epithets(self):
        '''
        returns a random amount of epithets.
        '''
        result = [''] * random.choice(range(1, 25))
        return [self.get_random_words() for item in result]