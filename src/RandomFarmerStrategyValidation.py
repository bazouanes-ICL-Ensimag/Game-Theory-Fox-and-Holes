import random 
import matplotlib.pyplot as plt

N= 10000


def cost(n):
    fox=random.randint(1,n)
    day_t=0
    while True : 
        day_t+=1
        farmer=random.randint(1,n)
        if fox==farmer:
            return day_t
        elif fox == 1 :
            fox=fox+1
        elif fox == n :
            fox= fox-1
        else :
            fox = fox+random.choice([-1,1])

# To check with only one value n : you should uncomment the following lines (choose a value for n) and comment all the rest of the code. 
# n=8 
# res=[cost(n) for elt in range(N)]
# print(sum(res)/N)

L=[]
n_values=list(range(1,101))
for n in range(1,101):
    res=[cost(n) for elt in range(N)]
    L.append(sum(res)/N)
    print(f"for n={n} : " ,sum(res)/N)

plt.figure(figsize=(9, 6))

plt.plot(n_values, L, label="Empirical expected capture time", linewidth=2, marker="o", markersize=4)
plt.plot(n_values, n_values, label="Theoretical line  T = n", linestyle="--", linewidth=2)

plt.xlabel("n (number of holes)", fontsize=12)
plt.ylabel("Expected capture time T ", fontsize=12)
plt.title("Expected Capture Time vs Number of Holes\n(Random Farmer Strategy)", fontsize=14, fontweight="bold")

plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()


