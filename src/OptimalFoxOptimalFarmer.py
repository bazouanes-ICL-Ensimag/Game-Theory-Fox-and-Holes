import matplotlib.pyplot as plt 


def fox_strategy(n):
    if n == 1:
        return [1]
    else: # n must be greater than or equal to 4
        # Double-sweep strategy 
        return list(range(1, n-1)) + list(range(n-3, 0, -1))+[2]

def farmer_strategy(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [2,2]       
    elif n == 3:
        return [2, 2]
    else:
        # Double-sweep strategy 
        return list(range(2, n)) + list(range(n-1, 1, -1))

def game(n): # n must be greater or equal to 4
    F = farmer_strategy(n)
    X = fox_strategy(n)
    m = len(F)
    day_t = 0
    farmer_pos = []
    fox_pos = []

    while True:
        day_t += 1
        fox = X[(day_t-1) % m]
        farmer = F[(day_t-1) % m]
        farmer_pos.append(farmer)
        fox_pos.append(fox)
        if fox == farmer:
            break
        

    return fox_pos, farmer_pos


# Computational validation : 

# Plot cost(n) vs 2n-4 : Fig 1 

cost_values = []
n_values = list(range(4, 101))

for n in n_values:
    fox_pos, farmer_pos = game(n)
    cost_values.append(len(fox_pos))

plt.figure(figsize=(10, 6))
plt.plot(n_values, cost_values, marker="o", label="Cost(n)")
plt.plot(n_values, [2*n - 4 for n in n_values],
         linestyle="--", label="2n - 4 (upper bound)")
plt.xlabel("n")
plt.ylabel("Cost")
plt.title("Cost for deterministic farmer/fox strategies vs 2n-4")
plt.grid(True)
plt.legend()


# Plot of history : Fig 2

n_demo = 10
fox_pos, farmer_pos = game(n_demo)
days = list(range(1, len(fox_pos) + 1))

plt.figure(figsize=(10, 6))

plt.plot(days, farmer_pos, "-s", label="Farmer position")
plt.plot(days, fox_pos, "-o", label="Fox position")
plt.xlabel("Days")
plt.ylabel("Holes")
plt.title(f"Movement of Fox and Farmer over time (n={n_demo})")
plt.grid(True)
plt.legend()

plt.xlim(1,days[-1]+0.2)
plt.xticks(days)
plt.ylim(0.8, n_demo+0.2)
plt.yticks(list(range(1,n_demo +1)))
plt.show()
