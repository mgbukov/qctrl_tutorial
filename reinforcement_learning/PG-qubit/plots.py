import numpy as np
from scipy.linalg import expm

from Bloch_lib import *

# fix seed
seed=0 
np.random.seed(seed)

# fix output array
np.set_printoptions(suppress=True,precision=2) 




############################################################

save=False #True


data = np.load('PG-1_qubit_training.npz')


episodes=data['episodes'] 
mean_final_reward=data['mean_final_reward'] 
std_final_reward=data['std_final_reward'] 
min_final_reward=data['min_final_reward']
max_final_reward=data['max_final_reward']


plt.plot(episodes, mean_final_reward, '-k', label='batch average' )
plt.fill_between(episodes, 
                 mean_final_reward-0.5*std_final_reward, 
                 mean_final_reward+0.5*std_final_reward, 
                 color='k', 
                 alpha=0.25)

plt.plot(episodes, min_final_reward, '.b' , markersize=2, label='batch minimum' )
plt.plot(episodes, max_final_reward, '.r' , markersize=1, label='batch maximum' )

plt.xlabel('training episode')
plt.ylabel('final reward $r_T{=}|\\langle\\psi_\\ast|\\psi(T)\\rangle|^2$')

plt.legend(loc='lower right', fontsize=14)
plt.grid()

plt.tight_layout()

if save:
	plt.savefig('RL-1q_training-curve.pdf')
	plt.savefig('RL-1q_training-curve.png', dpi=300)
else:
	plt.show()

plt.close()








