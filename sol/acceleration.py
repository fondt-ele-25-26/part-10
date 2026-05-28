import numpy as np
from matplotlib import pyplot as plt

def fit_curve(t0, t1, v0, v1):
    A = np.array([[t0**3, t0**2, t0, 1],
                  [t1**3, t1**2, t1, 1],
                  [3*t0**2, 2*t0, 1, 0],
                  [3*t1**2, 2*t1, 1, 0]])
    b = np.array([v0, v1, 0, 0])
    alpha_3, alpha_2, alpha_1, alpha_0 = np.linalg.solve(A, b)
    return alpha_3, alpha_2, alpha_1, alpha_0


def draw_curve(alpha_3, alpha_2, alpha_1, alpha_0, t0, t1):
    # Definisco i punti da disegnare
    x = np.linspace(t0, t1)
    y = alpha_3* x**3 + alpha_2 * x**2 + alpha_1 * x + alpha_0
    # Disegno il grafico
    plt.figure(figsize=(20, 5))
    plt.plot(x, y)
    plt.grid()
    plt.show()