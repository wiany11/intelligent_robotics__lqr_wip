from control import lqr
import numpy as np
from math import pi


M = 25.0

m = 5.0

l = 2.0

g = 9.80665    

A = [[0,                1,  0,  0   ],
     [((M+m)*g)/(M*l),  0,  0,  0   ],
     [0,                0,  0,  1   ],
     [-m*g/M,           0,  0,  0   ]]

B = [[0,    0,          0,  0       ],
     [0,    -1.0/(M*l), 0,  0       ],
     [0,    0,          0,  0       ],
     [0,    0,          0,  1.0/M   ]]

Q = [[1.0,  0,      0,      0       ],
     [0,    1.0,    0,      0       ],
     [0,    0,      250.0,   0       ],
     [0,    0,      0,      100.0    ]]

R = [[1.0,  0,      0,      0   ],
     [0,    1.0,    0,      0   ],
     [0,    0,      1.0,    0   ],
     [0,    0,      0,      1.0 ]]

K, S, E = lqr(A, B, Q, R)


#@state_feedback
#    param:
#        X
#            [theta, theta_dot, x, x_dot]
#        t
#            double
#    return:
#        new_X
#            [new_theta, new_theta_dot, new_x, new_x_dot]
def state_feedback(X, t):
    
    if -pi/360 < X[0] and X[0] < pi/360:
        return [0, 0, 0, 0]
    else:    
        BK = np.dot(B, K)
        AminusBK = np.subtract(A, BK)
        X_dot = np.dot(AminusBK, X)    #X_dot
        
        new_theta = X_dot[0]*t + 1/2*X_dot[1]*t*t #X[0] +   
        new_theta_dot = X_dot[0] + X_dot[1]*t 
        #new_x = X_dot[2]*t + 1/2*X_dot[3]*t*t #X[2] +   
        new_x = 0
        new_x_dot = X_dot[2]*t + X_dot[3]*t 
                    
        return [new_theta, new_theta_dot, new_x, new_x_dot]