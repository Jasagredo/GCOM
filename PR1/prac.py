from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np

__author__ = "Carlos Armero Canto, Miguel Benito Parejo & Javier Sagredo Tamayo"


class LeastSquares(object):

    def __init__(self):
        self.w_tilde = None

    def train(self, X, t):
        x_tilde = np.vstack([np.ones_like(X[0]), X])

        A = np.dot(x_tilde, x_tilde.T)
        b = np.dot(x_tilde, t.T)

        self.w_tilde = np.linalg.solve(A, b)

        return self.w_tilde

    def classify(self, x):
        if self.w_tilde is None:
            print("No has entrenado el metodo")
        else:
            return (self.w_tilde[1:].T.dot(x) + self.w_tilde[0]).argmax(axis=0)


class LDA(object):

    def __init__(self):
        self.w = None

    def train(self, X, t):
        # Generacion del vector de medias
        mi_arr = []
        for i in range(0, t.shape[0]):
            media_i = np.mean(X[:, t[i] == 1], axis=1)
            mi_arr.append(media_i)
        mean = np.vstack(mi_arr)

        # Generacion de x_cent
        mi_arr = []
        for i in range(0, t.shape[0]):
            x_i_m_i = X[:, t[i] == 1].T - mean[i]
            mi_arr.append(x_i_m_i)
        x_cent = np.vstack(mi_arr).T

        # Definicion de s_w
        s_w = x_cent.dot(x_cent.T)

        b = mean[0] - mean[1]

        self.w = np.linalg.solve(s_w, b)
        return self.w

    def classify(self, x):
        if self.w is None:
            print("No has entrenado el metodo")
        else:
            return (self.w[1:].T.dot(x) + self.w[0]).argmax(axis=0)


if __name__ == '__main__':

    x = np.array([[0.1, 0.15, 0.2, 0.3, 0.4, 0.35, 0.6, 0.65, 0.7, 0.8],
                  [0.8, 0.7, 0.5, 0.6, 0.3, 0.8, 0.7, 0.5, 0.6, 0.3]])
    t = np.array([[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]])
    ls = LDA()
    ls.train(x, t)
    print(ls.w)

    plt.scatter(x[0], x[1])
    plt.show()
