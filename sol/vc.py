import numpy as np


def equilibrium(rv=1.05, rc=1.5, p=2, ac=0.5):
    A = np.array([[rv * p, -rv],
                  [p, 1 - rc]])
    b = np.array([0, ac])
    v, c = np.linalg.solve(A, b)
    return v, c
