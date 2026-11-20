import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from hmmlearn import hmm


states = ["1", "2", "3", "4"]
observations = ["red", "green", "blue"]


start_probability = np.array([1/4, 1/4, 1/4, 1/4])


transition_probability = np.array([
    [0.2,  0.4,  0, 0.4],  
    [0.4,  0.2, 0.4, 0], 
    [0,  0.4, 0.2, 0.4],
    [0.4, 0, 0.4, 0.2]
])


emission_probability = np.array([
    [0.7,  0.2,  0.1],  
    [0.2, 0.6, 0.2],  
    [0.1,  0.3,  0.6],
    [0.5, 0.2, 0.3] 
])


model = hmm.CategoricalHMM(n_components=len(states))
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability

obs_map = {"red": 0, "green": 1, "blue": 2}
obs_seq_str = ["red", "green", "blue", "blue", "red"]

obs_seq = np.array([[obs_map[o]] for o in obs_seq_str])

log_prob, hidden_states = model.decode(obs_seq, algorithm="viterbi")

probabilitate = np.exp(log_prob)
secventa_dificultati = [states[s] for s in hidden_states]

print("Cerinta a)")
print("Observații: ", obs_seq_str)
print("Secvența:", secventa_dificultati)
print(f"Log-probabilitatea:     {log_prob:.6f}")
print(f"Probabilitatea:         {probabilitate:.10e}")

transition_probability = np.array([
    [0,  0.5,  0, 0.5],  
    [0.5,  0, 0.5, 0], 
    [0,  0.5, 0, 0.5],
    [0.5, 0, 0.5, 0]
])

model = hmm.CategoricalHMM(n_components=len(states))
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability

obs_map = {"red": 0, "green": 1, "blue": 2}
obs_seq_str = ["red", "green", "blue", "blue", "red"]

obs_seq = np.array([[obs_map[o]] for o in obs_seq_str])

log_prob, hidden_states = model.decode(obs_seq, algorithm="viterbi")

probabilitate = np.exp(log_prob)
secventa_dificultati = [states[s] for s in hidden_states]

print("Cerinta b)")
print("Observații: ", obs_seq_str)
print("Secvența:", secventa_dificultati)
print(f"Log-probabilitatea:     {log_prob:.6f}")
print(f"Probabilitatea:         {probabilitate:.10e}")