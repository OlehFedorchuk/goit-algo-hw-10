from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value

# Створюємо модель задачі максимізації
model = LpProblem("Drink_Production_Optimization", LpMaximize)

# Змінні: кількість одиниць лимонаду (x) та фруктового соку (y)
x = LpVariable("Lemonade", lowBound=0, cat='Integer')
y = LpVariable("FruitJuice", lowBound=0, cat='Integer')

# Цільова функція: максимізувати суму вироблених продуктів
model += x + y, "Total_Products"

# Обмеження на ресурси:
model += 2*x + 1*y <= 100, "Water_limit"            # Вода
model += 1*x <= 50, "Sugar_limit"                   # Цукор
model += 1*x <= 30, "Lemon_juice_limit"             # Лимонний сік
model += 2*y <= 40, "Fruit_puree_limit"             # Фруктове пюре

# Розв'язуємо задачу
model.solve()

# Виводимо результати
print("Статус розв'язку:", LpStatus[model.status])
print("Кількість лимонаду:", x.value())
print("Кількість фруктового соку:", y.value())
print("Загальна кількість вироблених продуктів:", value(model.objective))