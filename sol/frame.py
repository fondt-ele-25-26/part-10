import numpy as np
from matplotlib import pyplot as plt

def fit_curve(x0, y0, x1, y1, x2, y2, x3):
    A = np.array([[x0**2, x0, 1,      0,   0,  0],
                  [x1**2, x1, 1,      0,   0,  0],
                  [    0,  0, 0,  x0**2,  x0,  1],
                  [    0,  0, 0,  x2**2,  x2,  1],
                  [x3**2, x3, 1, -x3**2, -x3, -1],
                  [ 2*x0,  1, 0,  -2*x3,  -1, 0]])
    b = np.array([y0, y1, y0, y2, 0, 0])
    alpha2, alpha1, alpha0, beta2, beta1, beta0 = np.linalg.solve(A, b)
    return alpha2, alpha1, alpha0, beta2, beta1, beta0


def draw_curve(alpha2, alpha1, alpha0, beta2, beta1, beta0, x0, x3):
    # Definisco i punti da disegnare
    x = np.linspace(x0, x3)
    y1 = alpha2 * x**2 + alpha1 * x + alpha0
    y2 = beta2 * x**2 + beta1 * x + beta0
    # Disegno il grafico
    plt.figure(figsize=(20, 5))
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.grid()
    plt.show()
