from numpy import tensordot
from random import randint
from math import sqrt
import numpy as np


class Qubit:
    state = np.array([randint(0, 1), randint(0, 1)])


class EQubit:
    entangled_state = tensordot(Qubit.state, Qubit.state, axes=0)

    @classmethod
    def to_one_zero_basis(cls, entangled_state: np.array(list)) -> np.array(list):
        return np.array([cls.entangled_state[0][0], cls.entangled_state[1][1]])


class QEmulator:

    @staticmethod
    def x(state: np.array(list)) -> np.array(list):
        return np.fliplr([state])

    @staticmethod
    def cnot(entangled_state: np.array(list)) -> np.array(list):
        if entangled_state[0] == 1 and entangled_state[1] == 0:
            return np.array([1, 1])
        if entangled_state[0] == 1 and entangled_state[1] == 1:
            return np.array([1, 0])
        return entangled_state

    @staticmethod
    def hadamard_transform(state: np.array(list)) -> np.array(list):
        return tensordot(np.array([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]]), state, axes=0)

    @staticmethod
    def z(state: np.array(list)) -> np.array(list):
        return tensordot(np.array([[1, 0], [0, -1]]), state, axes=0)
