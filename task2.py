import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Функція
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# 1. Метод Монте-Карло
N = 100_000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
f_values = f(x_random)
monte_carlo_integral = (b - a) * np.mean(f_values)

# 2. Аналітичний результат (для f(x) = x^2: ∫x^2 dx = x^3/3)
analytical_integral = (b**3 - a**3) / 3

# 3. Використання SciPy (quad)
quad_integral, quad_error = spi.quad(f, a, b)

# Виведення результатів
print("🔹 Монте-Карло інтеграл:", monte_carlo_integral)
print("🔹 Аналітичний інтеграл:", analytical_integral)
print("🔹 Quad інтеграл:", quad_integral, "| Похибка:", quad_error)

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', label='f(x) = x^2', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Площа під кривою')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Інтегрування f(x) = x^2 від 0 до 2')
ax.legend()
plt.grid()
plt.show()