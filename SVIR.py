"""
Vaccination model to be fit to data
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import sys

#time points to solve at
tpts = np.linspace(0,100,1001)

#initial values as population fractions
I0 = 1e-2
R0 = 0
V0 = 0

# parameter values
params = {}
params['beta'] = 1.2
params['gamma'] = 0.1
params['mu'] = 0.001
params['nu'] = 0.07
params['rho'] = 0.15


##################################

# vectorize initial conditions
x0 = np.array([1-I0-R0, V0, I0, R0])

# define ode equations
def SVIR_ODEs(t,x,params):
    '''This function returns the time derivates of S,V,I,R.

    The ode solver expects the first two arguments to be t and x

    The params argument should be a dict with beta, gamma, mu, and nu as keys.
    It must be passed into the solver using the set_f_params method
    '''

    S = x[0]; V = x[1]; I = x[2]; R = x[3]
    dx = np.zeros(4)

    dx[0] = -params['beta']*S*I - params['rho']*S + params['mu']*I + params['nu']*(V+R)
    dx[1] = params['rho']*S - params['nu']*V
    dx[2] = params['beta']*S*I - params['gamma']*I - params['mu']*I
    dx[3] = params['gamma']*I - params['nu']*R

    return dx

##### Solve procedure #####
sol = solve_ivp(SVIR_ODEs, t_span=[tpts[0], tpts[-1]], y0=x0, t_eval=tpts, 
                args=(params,))


##### Plot result #####
fig = plt.figure(figsize=(9,7))
plt.plot(sol.t,sol.y[0,:],sol.t,sol.y[1,:],sol.t,sol.y[2,:],sol.t,sol.y[3,:])
plt.legend(['S','V','I','R'])
plt.title("Plot of $S,V,I,R$ vs. time")
plt.xlabel("$t$")
plt.ylabel("population fraction")
plt.show()
