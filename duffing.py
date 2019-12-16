import numpy as np

def duffing(var, t, alpha, beta, gamma, delta, omega, theta):
    """
    Duffing Oscillator
    var = [position, velocity]
    t   = time
    coefficients: alpha, beta, gamma, delta, omega, theta

    ddx = -delta*dx - alpha*x - beta*x**3 + gamma*cos(omega*t + theta)

    return [velocity, force]
    """

    x_dot = var[1]
    v_dot = -delta*var[1] - alpha*var[0] - beta*var[0]**3 + gamma*np.cos(omega*t + theta)

    return np.array([x_dot, v_dot])
