import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz A y el vector b
A = np.array([[0.001, 1, 1], 
              [1, 0.001, 1], 
              [1, 1, 0.001]])

b = np.array([1, 1, 1])

# Calcular el determinante
determinante = np.linalg.det(A)
print('Determinante de A:', determinante)

# Calcular la inversa de la matriz (si es posible)
try:
    A_inv = np.linalg.inv(A)
    print('Matriz Inversa de A:\n', A_inv)
except np.linalg.LinAlgError:
    print("La matriz es singular y no tiene inversa.")

# Calcular el número de condición
condicional = np.linalg.cond(A)
print('Número de condición de A:', condicional)

# Resolver el sistema original
solucion_original = np.linalg.solve(A, b)
print('Solución del sistema original:', solucion_original)

# Hacer un pequeño cambio en el vector b
b_perturbado = b + np.array([0.001, 0, 0])

# Resolver el sistema con el vector b perturbado
solucion_perturbada = np.linalg.solve(A, b_perturbado)
print('Solución del sistema perturbado:', solucion_perturbada)

# Gráfico de las soluciones
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(solucion_original[0], solucion_original[1], solucion_original[2], color='blue', label='Solución Original')
ax.scatter(solucion_perturbada[0], solucion_perturbada[1], solucion_perturbada[2], color='red', label='Solución Perturbada')

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')
plt.title('Comparación de Soluciones del Sistema Mal Condicionado')
plt.legend()
plt.grid(True)
plt.show()
