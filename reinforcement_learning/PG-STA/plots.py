import os, sys

import matplotlib
import matplotlib.pyplot as plt

#os.environ["PATH"] += ':/usr/local/texlive/2015/bin/x86_64-darwin' # <-- change to local path
plt.rc('text', usetex=True)
plt.rc('font', **dict(family='serif', size=16) )
plt.tick_params(labelsize=18)
plt.rcParams["figure.figsize"] = [6.5, 5.5] 

import matplotlib as mpl
mpl.use('MacOSX')


import numpy as np


save=False #True


data = np.load('PG-STA_protocol.npz')

times=data['times'] 
fidelity_inst_t=data['fidelity_inst_t']
fidelity_t=data['fidelity_t'] 
RL_field_t=data['RL_field_t']
CD_protocol_t=data['CD_protocol_t']
exact_CD_protocol=data['exact_CD_protocol']
reward_RL=data['reward_RL']
reward_CD_approx=data['reward_CD_approx']


fig, ax = plt.subplots(figsize=(7,6))

ax.step(times, CD_protocol_t, '.-b', where='pre', label='discretized CD, $r_T={0:0.3f}$'.format(reward_CD_approx) )
ax.step(times, RL_field_t, '.-g', where='pre', label='RL agent, $r_T={0:0.3f}$'.format(reward_RL) )
ax.plot(times, exact_CD_protocol,'--r', label='exact CD, $r_T=\\infty$' )
ax.legend(fontsize=14)

ax.set_xlabel('time $t$')
ax.set_ylabel('drive protocol')

plt.tight_layout()
plt.grid()

if save:
	plt.savefig('PG-STA_protocols.pdf')
else:
	plt.show()

plt.close()


##########################


fig, ax1 = plt.subplots(figsize=(7,6))


# These are in unitless percentages of the figure size. (0,0 is bottom left)
left, bottom, width, height = [0.55, 0.2, 0.33, 0.3]
ax2 = fig.add_axes([left, bottom, width, height])


#ax1.axhline(y=1.0, color='k', linestyle='-', linewidth=1.0)
ax1.step(times, fidelity_t, '.-g', where='pre',label='$|\\langle\\psi_\\ast|\\psi(T)\\rangle|^2$')
ax1.step(times, fidelity_inst_t, '.-',color='brown', where='pre',label='$|\\langle\\mathrm{GS}(t)|\\psi(t)\\rangle|^2$',)
ax2.step(times, np.log10(1-fidelity_t), '.-g', where='pre',)
ax2.step(times, np.log10(1-fidelity_inst_t), '.-',color='brown', where='pre',)
#ax2.set_yscale('log')

ax1.legend(fontsize=14, loc='center left')

ax1.set_xlabel('time $t$')
ax1.set_ylabel('fidelity', fontsize=14)

ax2.set_xlabel('time $t$')
ax2.set_ylabel('$\\log_{10}$-infidelity', fontsize=14)

ax1.grid()
ax2.grid()

#plt.tight_layout()

if save:
	plt.savefig('PG-STA_fidelity.pdf')
else:
	plt.show()

plt.close()


#exit()

############################################################




data = np.load('PG-STA_training.npz')


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

plt.plot(episodes, min_final_reward, '.b' , markersize=1, label='batch minimum' )
plt.plot(episodes, max_final_reward, '.r' , markersize=1, label='batch maximum' )

plt.xlabel('training episode')
plt.ylabel('final reward $r_T{=}{-}\\log_{10}\\left(1{-}|\\langle\\psi_\\ast|\\psi(T)\\rangle|^2\\right) $')

plt.legend(loc='lower right', fontsize=14)
plt.grid()

plt.tight_layout()

if save:
	plt.savefig('PG-STA_training-curve.pdf')
	plt.savefig('PG-STA_training-curve.png', dpi=300)
else:
	plt.show()

plt.close()








