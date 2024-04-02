'''Example of solving an ODE with scipy'''

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

tstart = 0 # start solving the ODE at time t=0
tstop = 60 # stop at time t=100

x0 = 1 # Initial condition for x

# parameter values
params = {} # Remember: this is how you create a dictionary
params['r'] = 1
params['K'] = 1000


##################################

# define ode equations.
def logistic_eqn(t, x, params):
    '''This function specifies the ODE(s) to be solved. It must take in the
    current time as the first argument and the current value(s) of the
    independent variables as the second argument. You can also pass in parameters
    with a third argument. I like to use a dictionary for this, as I can give
    the parameters names and don't have to keep track of the order in which I
    put them into a list or somesuch.
    
    BE CAREFUL: dictionaries are mutable.
    '''
    
    dxdt = params['r']*x*(1-x/params['K']) # logistic equation

    return dxdt


# Solve the ODE with given initial condition, start time, end time, and parameters.

y0 = np.array([x0]) # initial condition must be given as an array

# You can give the t_eval argument of solve_ivp a mesh of time points in order to
#   force solutions to be recorded at these points. Otherwise, the variable
#   step solver will choose.
tmesh = np.linspace(tstart,tstop,1000)

### call the solver ###
# The default solver is RK45 which is an explicit, variable step size Runge
#   Kutta solver of order 4(5). It's also known as "Dormand-Prince" and 
#   it's basically ODE45. Try it first unless you have a good reason not to.
# args passes arguments to all supplied functions. It must be a tuple.
solution = solve_ivp(logistic_eqn, t_span=[tstart, tstop], y0=y0, args=(params,))


### Plot a solution set and either show it or return the plot object ###
time = solution.t
x = solution.y[0,:] # only one eqn., so has shape (1, timepoints)
plt.plot(time, x, label='logistic eqn')
plt.xlabel('time')
plt.legend()
plt.tight_layout()
plt.show()

