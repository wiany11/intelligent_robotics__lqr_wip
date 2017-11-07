# lqr-ip
Linear-Quadratic Regulator (LQR) for Wheeled Inverted Pendulum (WIP)

### Introduction

The theory of optimal control is concerned with operating a dynamic system at minimum cost. The case where the system dynamics are described by a set of linear differential equations and the cost is described by a quadratic function is called the LQ problem. One of the main results in the theory is that the solution is provided by the linear–quadratic regulator (LQR), a feedback controller... ([Wikipedia](https://en.wikipedia.org/wiki/Linear%E2%80%93quadratic_regulator))

LQR is one of the optimal control techniques making optimal control decisions using the current state of dynamical system. As a way of understanding LQR, wheeled inverted pendulum is used in modeling and simulation.

I implemented this for term project of the course Intelligent Robotics. It looks crude, however, it may be quite good for beginners like me to understand how LQR really works with the naked eyes.

### Requirements

```
$ sudo apt-get install python-tk
$ sudo apt-get install python-scipy
$ sudo apt-get install python-matplotlib

$ pip install slycot
$ pip install control
```
If you have some trouble installing `slycot` you may find useful informatio at [Slycot GitHub page](https://github.com/jgoppert/Slycot). There are alternatives to install the package. (I used `conda`.) Also, you can find more information about `python-control` at [Python Control Systems Library](http://python-control.readthedocs.io/en/latest/intro.html).

### Run

```
$ python view/sim.py
```

### Demo

[![LQR for WIP Demo.](https://i.ytimg.com/vi/K6Hm0M9G-kc/2.jpg)](https://youtu.be/K6Hm0M9G-kc "LQR for WIP Demo.")

