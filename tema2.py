#1
import numpy as np

numar_simulari = 100000

X = np.random.randint(1,7,numar_simulari)
Y = np.random.randint(1,7,numar_simulari)

P_1 = 2/9
P_2 = 5/27
P_3 = 3/5

cond_1 = (X % 2 == 0)
tinta_1 = (X + Y) >= 10
p_1 = np.mean(tinta_1[cond_1]) if np.sum(cond_1) > 0 else 0

cond_2 = (X % 2 == 0) | (Y % 2 == 0)
tinta_2 = (X + Y) >= 10
p_2 = np.mean(tinta_2[cond_2]) if np.sum(cond_2) > 0 else 0

cond_3 = (X + Y) == 8
tinta_3 = (X % 2 == 0) & (Y % 2 == 0)
p_3 = np.mean(tinta_3[cond_3]) if np.sum(cond_3) > 0 else 0

print(f"1. P(Suma >= 10 | Primul zar par)       = {p_1:.4f}  (Teoretic: {P_1})")
print(f"2. P(Suma >= 10 | Cel puțin un zar par) = {p_2:.4f}  (Teoretic: {P_2})")
print(f"3. P(Ambele pare | Suma = 8)            = {p_3:.4f}  (Teoretic: {P_3})")


#3
import pandas as pd
import numpy as np

data = {
    'Program': ['Program_1', 'Program_1', 'Program_2', 'Program_2'],
    'Disciplina': ['A', 'B', 'A', 'B'],
    'Promovati': [40, 70, 20, 1],
    'Total_Studenti': [50, 97, 50, 3]
}

df = pd.DataFrame(data)

df['Rata_Promovare'] = df['Promovati'] / df['Total_Studenti']

print("Tabelul cu date locale")
print(df)
print("\n")

global_A = df[df['Disciplina'] == 'A']['Promovati'].sum() / df[df['Disciplina'] == 'A']['Total_Studenti'].sum()
global_B = df[df['Disciplina'] == 'B']['Promovati'].sum() / df[df['Disciplina'] == 'B']['Total_Studenti'].sum()

print(f"Rata globala de promovare pentru Disciplina A: {global_A:.4f} ({global_A*100:.1f}%)")
print(f"Rata globala de promovare pentru Disciplina B: {global_B:.4f} ({global_B*100:.1f}%)")
