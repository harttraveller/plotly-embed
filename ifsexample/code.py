import random
import numpy as np
from .env import SIMPLEX


def sierpinski(n: int, dim: int) -> np.matrix:
    e, p = SIMPLEX[dim], [np.zeros(dim)]
    for i in range(n):
        p.append(((p[i] + random.choice(e)) / 2))
    return np.matrix(p)
