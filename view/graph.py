from control.dynamics import state_feedback
from control.plot import plot_rotation_and_transition
from math import pi


if __name__ == '__main__':
    Theta = pi/6
    t = 0.001
    X = [Theta, Theta/t, 0, 0]
    
    Transition = []
    Rotation = []    
    Time = []
    X_tr = 0
    for i in range(1500):
        if -pi/360 < X[0] and X[0] < pi/360:
            break
        
        #print(i, X)
        X = state_feedback(X, t)
        X = [Theta, Theta/t, 0, 0]
        
        X_tr += 1000000.0*(X[2]*t + 1.0/2*X[3]*t*t)
        print(i, X[0] / pi * 180, X_tr)
        Transition.append(X_tr)
        Rotation.append(X[0]/ pi * 180)  
        Time.append(i * t)
    
    plot_rotation_and_transition(Transition, Rotation, Time, "M=25, m=5, l=2")
