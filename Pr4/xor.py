from Red import *

a = multilayer_perceptron(2, 1, [2], activation='sigmoid', coste='multiclase')
X = np.array([[1,0,1,0], [1,1,0,0]])
T = np.array([0,1,1,0])
a.train(X, T, 0.05, epochs=4000)
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
fondo = np.mgrid[-2:2:0.05, -2:2:0.05].reshape(2, 6400)
g = map(a.classify, fondo.T)
clase_fondo = map((lambda x: 'C' + str(x)), map((lambda x: 1 if x > 0.5 else 0), g))
ax.scatter(fondo[0], fondo[1], color=clase_fondo, alpha=0.2, s=5)
ax.scatter(X[0], X[1], color='k')
fig.canvas.draw()
plt.show()
