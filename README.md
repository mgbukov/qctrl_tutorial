This file contains instructions for using the Jupyter notebooks accompanying arXiv:2501.16436 (Taming quantum systems: A tutorial for using shortcuts-to-adiabaticity, quantum optimal control, and reinforcement learning) by Duncan et al. 


Sec II: [Shortcuts to Adiabaticity](shortcuts_to_adiabaticity)

    * Notebook 2.1: 


Sec III: [Quantum Optimal Control](quantum_optimal_control)

    * Notebook 3.1: 

Sec IV: [Reinforcement Learning for Optimal Quantum Control](reinforcement_learning)  

    * Notebook 4.1: [Universal single-qubit state preparation](reinforcement_learning/PG-qubit)  
    * Notebook 4.2: [RL vs. counter-diabatic driving in the presence of Trotterization errors](reinforcement_learning/PG-STA)  
    * Notebook 4.3: [Continuous single-qubit feedback control using quantum data](reinforcement_learning/PG-quantum_data)  


Required packages can be found in [requirements.txt](./requirements.txt). 

You may create a virtual environment using `pip` and install all packages at once by running:
    
    .. python -m venv .ctrl_tutorial
    .. source .ctrl_tutorial/bin/activate
    .. python -m pip install --upgrade pip
    .. python -m pip install -r requirements.txt




