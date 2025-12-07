import random
import matplotlib.pyplot as plt

def farmer_strategy(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [2,2]
    elif n == 3:
        return [2,2]
    else:
        return list(range(2, n)) + list(range(n-1, 1, -1))

def game(n):
    F_strategy = farmer_strategy(n)
    m = len(F_strategy)
    day_t = 0
    fox=random.randint(1, n)
    fox_positions = []
    farmer_positions = []

    while True:
        day_t += 1
        farmer = F_strategy[(day_t-1) % m]
        fox_positions.append(fox)
        farmer_positions.append(farmer)

        if fox == farmer:
            break
        if fox == 1:
            fox = 2
        elif fox == n:
            fox = n - 1
        else:
            fox += random.choice([-1, 1])
    return fox_positions, farmer_positions

# Parameters : 
n = 5

fox_pos, farmer_pos = game(n)
days = list(range(1, len(fox_pos) + 1))

plt.figure(figsize=(10,6))
plt.plot(days, farmer_pos, color="blue", linewidth=2, label="Farmer positions")
plt.plot(days, fox_pos, color="orange" , linewidth=2, label="Fox positions")
plt.scatter(days, fox_pos, color="orange", s=50, zorder=3)
plt.scatter(days, farmer_pos, color="blue", s=50, zorder=3)
plt.xlabel("Days")
plt.ylabel("Holes")
plt.title(f"Movement of Fox and Farmer over time (n={n})")
plt.grid(True)
plt.legend()
plt.xlim(1,days[-1]+0.2)
plt.xticks(days)
plt.ylim(0.8, n+0.2)
plt.yticks(list(range(1,n+1)))
plt.show()