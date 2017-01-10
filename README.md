# Poppy Neuro-robotic Control

This project aims at providing poppy robot from INRIA FLOWERS lab with gaits in two steps (CMA-ES optim of control signals; morphological closed-loop learning). This should be then extended to spiking neural models control using NEST in the Neuro-robotics platform.

The current state is about building a mock-up to create gait actuation primitives, CMA-ES evolution and closed-loop control learning.

## Installation
Poppy robot is provided with software python libraries to enable high level simulation in the V-REP simulator.
The simulator and installation instructions can be found here:
- [VRep download page](http://www.coppeliarobotics.com/downloads.html)
The additionnal required python libraries are:
- Pypot>=2.1, a python library for controlling dynamixel motors. See [Repository](https://github.com/poppy-project/pypot) and [Documentation](http://poppy-project.github.io/pypot/)
- Poppy_humanoid>=1.0, the python software to control the robot. See [Repository](https://github.com/poppy-project/poppy-humanoid/tree/master/software)

To install this software just clone it in your project folder:
 ```
 cd $PRJ
 git clone https://github.com/Gabs48/poppy
 ```

## First steps
A [jupyter notebook](https://github.com/poppy-project/poppy-humanoid/blob/master/software/samples/notebooks/Controlling%20a%20Poppy%20humanoid%20in%20V-REP%20using%20pypot.ipynb) supplied with the poppy project can be followed in order to test and understand the simulation API.

## Simulation
In a first terminal, start VRep simulator:
 ```
 cd $PRJ/VREP
 ./vrep.sh
 ```
In a second terminal, we start the python code that will set up and run the simulation:
 ```
 cd $PRJ.poppy
 ./main.py
 ```
(You may have to accept to start the simulation from an external software the first time)

When the simulation script is finished, do not forget to stop the simulator (and close it if needed) to free up memory and CPU.