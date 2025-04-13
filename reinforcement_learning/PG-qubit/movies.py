import numpy as np
from scipy.linalg import expm

from Bloch_lib import *

# fix seed
seed=0 
np.random.seed(seed)

# fix output array
np.set_printoptions(suppress=True,precision=2) 


############################################################


### load data
#data = np.load('PG-1_learned_states.npz')
data = np.load('learned_states_1q.npy')
print(data)
exit()

# all_states = data['learned_states_1q.npy']
# times = data['learned_times_1q.npy']

all_states = data['states_visited']
times = data['times']

target = np.array([1.0,0.0], dtype=np.complex128)


### plot on Bloch sphere

for i, states in enumerate(all_states):

    fid_t = Bloch_movie(states, times[i], target, movie_name='blochtraj_{0:d}'.format(i))

