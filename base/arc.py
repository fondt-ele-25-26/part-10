import numpy as np
from matplotlib import pyplot as plt

def fit_curve(x0, x1, x2, y0, y2):
    A = np.array([[x0**2, x0, 1],
              [x2**2, x2, 1],
              [2*x1, 1, 0]])

    b = np.array([y0, y2, 0])
    alpha_2, alpha_1, alpha_0 = np.linalg.solve(A, b)
    return alpha_2, alpha_1, alpha_0


def draw_curve(alpha_2, alpha_1, alpha_0, x0, x2):
    # Definisco i punti da disegnare
    x = np.linspace(x0, x2, 100) # Uso 100 punti
    y = alpha_2 * x**2 + alpha_1 * x + alpha_0
    # Disegno il grafico
    plt.figure(figsize=(20, 5))
    plt.plot(x, y)
    plt.grid()
    plt.show()
