import numpy as np
from scipy.intergate import solve_ivp
import matplotlib.pyplot as plt

def concentration(D,t):
    """
    differential equation to describe antibiotic concentration time evolution

    Parameters
    ----------
    D : Concentration of antiobiotics
    t : time

    Returns
    -------
    dD_dt : first order DE
    """
    #Define k_deg parameter
    k_deg = 1.0
    dD_dt = - k_deg * D

    return dD_dt

def number_cells(N,t,D,EC50):
    """
    differential equation to describe time evolution of number of bacteria cells

    Parameters
    ----------
    N : Number of cells
    t : time

    Returns
    -------
    dN_dt : first order DE
    """
    #define parameters
    g=1.0
    V_max=1.0
    n=3.0

    dN_dt = g*N - (V_max * D**n * N) / (D**n + EC50**n)

    return dN_dt

def area(N):
    #function calculate area of colony proportional to N(t)
    return area 

#initial conditions
D0=1.0      #?
N0=2000
threshold=   #?

#time points
trange = (0.0, 10.0)         #placeholder values
time = np.linspace(0,10)

#solve antiobiotic concentration debug
D = solve_ivp(concentration, trange, D0, t_eval=time, dense_output=True)

# EC50 = np.random.gamma(2.0,2.0,N0)      #2000 EC50 values from gamma distribution (review shape,scale)
# EC50[EC50<threshold] = 0.0              #insantly kill number of cells if EC50 below threshold value

EC50_list = []
for i in range(N0):
    EC50 = np.random.gamma(2.0,2.0)
    if EC50>threshold:
        EC50_list.append(EC50)

N = len(EC50_list)          #number of cells not killed immediately

#solce DE for number of cells
N = solve_ivp(number_cells, trange, y0=1.0, t_eval=time, dense_output=True)
