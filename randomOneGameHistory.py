import random
import matplotlib.pyplot as plt

def game(n=3):
    fox = random.randint(1, n)
    day_t = 0
    history = []  

    while True:
        day_t += 1
        farmer = random.randint(1, n)
        history.append((day_t, fox, farmer))
        if farmer == fox:
            break
        if fox == 1:
            fox = 2
        elif fox == n:
            fox = n - 1
        else:
            fox += random.choice([-1, 1])

    return history

# Parameter :
n=5



history = game(n)


days = [h[0] for h in history]
fox_pos = [h[1] for h in history]
farmer_pos = [h[2] for h in history]


plt.figure(figsize=(10,6))

plt.plot(days, farmer_pos, "-s", label="Farmer position")
plt.plot(days, fox_pos, "-o", label="Fox position")


plt.xlabel("Days")
plt.ylabel("Holes")
plt.title(f"Random Farmer vs random Fox (n={n})")
plt.grid(True)
plt.legend()

plt.xlim(1, days[-1]+0.2)
plt.xticks(days)
plt.ylim(0.5, n+0.5)

plt.show()
