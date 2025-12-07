import random 
import matplotlib.pyplot as plt 

N=10000

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

def cost(n):
    fox=random.randint(1,n)
    day_t=0
    farmer_strat=farmer_strategy(n)
    m=len(farmer_strat)
    while True : 
        day_t+=1
        farmer=farmer_strat[(day_t-1)%m]
        if fox==farmer:
            return day_t
        elif fox == 1 :
            fox=fox+1
        elif fox == n :
            fox= fox-1
        else :
            fox = fox+random.choice([-1,1])

# Comparing the cost to 2n-4 : 
n_values=list(range(4,101))
max_cost = []
for n in n_values:
    vals = [cost(n) for elt in range(N)]
    max_cost.append(max(vals))


plt.figure(figsize=(9,5))
plt.plot(n_values, max_cost, label="Max cost over 10 000 samples for each n", linewidth=2, marker="o", markersize=4)
plt.plot(n_values, [2*n-4 for n in n_values], "--", label="Theoretical bound 2n-4")
plt.xlabel("n")
plt.ylabel("Cost")
plt.title(f"Max observed cost (N={N} simulations per n)")
plt.grid(True)
plt.legend()
plt.show()


# Comparing the expected cost to n : 
n_values=list(range(1,101))
L=[]

for n in range(1,101):
    res=[cost(n) for elt in range(N)]
    L.append(sum(res)/N)
    print(f"for n={n} : " ,sum(res)/N)

plt.figure(figsize=(9, 6))

plt.plot(n_values, L, label="Empirical expected cost", linewidth=2, marker="o", markersize=4)
plt.plot(n_values, n_values, label="Theoretical line  T = n", linestyle="--", linewidth=2)

plt.xlabel("n (number of holes)", fontsize=12)
plt.ylabel("Expected capture time T", fontsize=12)
plt.title("Expected Capture Time vs Number of Holes\n (Deterministic farmer strategy)", fontsize=14, fontweight="bold")

plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()


