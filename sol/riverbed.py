import numpy as np
from matplotlib import pyplot as plt

def fit_curve(x0, x1, d0, d1, s1):
    A = np.array([[x0**2, x0, 1],
                  [x1**2, x1, 1],
                  [1/3 * (x1**3 - x0**3), 1/2 * (x1**2 - x0**2), x1 - x0]])
    b = np.array([d0, d1, s1])
    alpha_2, alpha_1, alpha_0 = np.linalg.solve(A, b)
    return alpha_2, alpha_1, alpha_0


def draw_curve(alpha_2, alpha_1, alpha_0, x0, x1):
    # Definisco i punti da disegnare
    x = np.linspace(x0, x1)
    y = alpha_2 * x**2 + alpha_1 * x + alpha_0
    # Disegno il grafico
    plt.figure(figsize=(20, 5))
    plt.plot(x, y)
    plt.grid()
    plt.show()
