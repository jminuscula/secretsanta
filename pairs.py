
import abc
import random


class Pairer(abc.ABC):

    @abc.abstractmethod
    def get_pairs(self, population, seed):
        pass


class CircularRandomPairer(Pairer):

    def get_pairs(self, population, seed):
        random.seed(seed)
        participants = list(population)
        random.shuffle(participants)
        size = len(participants)
        return ((participants[i], participants[(i + 1) % size]) for i in range(size))
