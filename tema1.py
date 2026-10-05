#EX 1
import csv
import random

def extrage_studenti(fisier, numar):
    studenti= []
    with open(fisier,"r") as file:
        data = csv.reader(file)
        for row in data:
            studenti.append(row[0])

    if numar>len(studenti):
        print("Numarul cerut este mai mare decat numarul de studenti.")

    esantion=random.sample(studenti,numar)
    return esantion

test = extrage_studenti('studenti.csv', 5)
print(test)

#EX 2
# N urmeaza o distributie geometrica!!

import matplotlib.pyplot as plt
import numpy as np

# b
def simulare_joc(prob_stema):
    S=0.0
    N=1
    while np.random.choice([1,0],p=[prob_stema, 1-prob_stema]) == 0:
        S -= 0.5
        N += 1
    z=np.random.randint(1,7)
    S += z-3
    return N,S 

def analiza_joc(prob_stema, numar=100000):
    rezultate = []
    for i in range(numar):
        N, S = simulare_joc(prob_stema)
        rezultate.append(S)
    medie = np.mean(rezultate)

    plt.hist(rezultate, bins=20, edgecolor='black', alpha=0.7)
    plt.title(f'Distributia sumei S (prob_stema = {prob_stema})\nMedia: {medie:.3f}')
    plt.xlabel('Suma S')
    plt.ylabel('Frecventa')
    plt.show()

    return medie

# c
analiza = analiza_joc(0.5)
print(f"Media lui S pentru p=0.5 este: {analiza:.3f}")

# d

analiza = analiza_joc(0.3)
print(f"Media lui S pentru p=0.3 este: {analiza:.3f}")

analiza = analiza_joc(0.7)
print(f"Media lui S pentru p=0.7 este: {analiza:.3f}")

#EX 3
import arviz as az
import xarray as xr

lambda_valori = [3, 6, 4]
prob = [3/13, 6/13, 4/13]
numar = 10000

alegeri_frizeri = np.random.choice([0,1,2], size = numar, p = prob)
X = np.zeros(numar)

for i in range(numar):
    lambda_frizer = lambda_valori[alegeri_frizeri[i]]
    X[i]=np.random.exponential(scale=1/lambda_frizer)

medie_X = np.mean(X)
deviatie_X = np.std(X)

print(f"Media estimata a lui X: {medie_X:.4f} ore")
print(f"Deviatia standard estimata a lui X: {deviatie_X:.4f} ore")

dataset = xr.Dataset({"X": (("chain", "draw"), [X])})
idata = xr.DataTree.from_dict({"posterior": dataset})
az.plot_dist(idata, kind="kde")
plt.title('Distribuția timpului de servire (X)')
plt.xlabel('Timpul de servire (ore)')
plt.ylabel('Densitate')
plt.show()