from pulp import *

# Створення задачі
model = LpProblem("Maximize_Drink_Production", LpMaximize)

# Змінні
lemonade = LpVariable("Lemonade", lowBound=0, cat=LpInteger)
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat=LpInteger)

# Ціль
model += lemonade + fruit_juice

# Обмеження
model += 2 * lemonade + fruit_juice <= 100
model += lemonade <= 50
model += lemonade <= 30
model += 2 * fruit_juice <= 40

# Вказуємо явно використання CBC-солвера
solver = getSolver("PULP_CBC_CMD", msg=True)
model.solve(solver)

# Результати
print("Status:", LpStatus[model.status])
print("Lemonade:", lemonade.varValue)
print("Fruit Juice:", fruit_juice.varValue)
print("Total:", value(model.objective))