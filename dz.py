import matplotlib.pyplot as plt

def price_ways(n, d):
    if n <= 0:
        return 0
    price = [0] * (n + 1)
    for i in range(1, n + 1):
        price[i] = price[i - 1] + d
    return price

def find_optimal_path(n, d, forward_steps, multiplier_steps):
    if n <= 0:
        return 0
    price = [0] * (n + 1)
    for i in range(1, n + 1):
        price[i] = price[i - 1] + d
    cost = [float('inf')] * (n + 1)
    cost[0] = 0  

    prev_step = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(len(forward_steps)):
            if i - forward_steps[j] >= 0:
                current_cost = cost[i - forward_steps[j]] + d
                if current_cost < cost[i]:
                    cost[i] = current_cost
                    prev_step[i] = i - forward_steps[j]

        for j in range(len(multiplier_steps)):
            if i % multiplier_steps[j] == 0:
                current_cost = cost[i // multiplier_steps[j]] + d
                if current_cost < cost[i]:
                    cost[i] = current_cost
                    prev_step[i] = i // multiplier_steps[j]

    optimal_path = []
    current_step = n
    while current_step > 0:
        optimal_path.append(current_step)
        current_step = prev_step[current_step]

    optimal_path.reverse()
    
    return optimal_path, cost[n]

n = int(input("Введите число ступенек: "))
d = int(input("Введите шаг повышения цены: "))

forward_steps = []
print("Введите шаг для движения вперед (введите 0 для завершения ввода):")
while True:
    step = int(input())
    if step == 0:
        break
    forward_steps.append(step)

multi_steps = []
print("Введите множители для индекса ступеньки (введите 0 для завершения ввода):")
while True:
    multiplier = int(input())
    if multiplier == 0:
        break
    multi_steps.append(multiplier)
price = price_ways(n,d)
optimal_path, steps = find_optimal_path(n, d, forward_steps, multi_steps)
full_price=[0]*len(optimal_path)

for i in range (len(optimal_path)):
    full_price[i] = price[optimal_path[i]]+full_price[i-1]
print("Минимальная сумма: ", full_price[len(full_price)-1])
print("Оптимальный путь:", optimal_path)
print("Изменение цены от выбора ступеньки:",full_price)
print("Кол-во шагов:", steps)

x = optimal_path
y = full_price

plt.plot(x, y)  
plt.scatter(x, y, color='red', marker='o', label='Выбранные ступеньки')
plt.xlabel('Индексы ступенек') 
plt.ylabel('Минимальная цена') 
plt.title('Оптимальное решение') 
plt.legend()
plt.show()  