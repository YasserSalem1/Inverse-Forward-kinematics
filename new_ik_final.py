#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi


def main():
    np.set_printoptions(precision=3, suppress=True)
    # |  d  |  a  |  alpha  |  theta  |
        # dh_params = np.array([[0.04, 0., 0.5 * pi, 0.],
        #                       [0., 0.105, pi, 0.5 * pi],
        #                       [0., 0.105, pi, 0.],
        #                       [0, 0.105, pi/2, 0]
        #                       ])

    dh_params = np.array([[0.04, 0., 0.5 * pi, 0.],
                          [0., 0.105, pi, 0.5 * pi],
                          [0., 0.105, pi, pi],
                          [0, 0.105, pi/2, 0]
                          ])
                        
    robot = RobotSerial(dh_params)


    xyz = np.array([[2], [0], [0]])
    abc = np.array([0,0 ,0])
    end = Frame.from_euler_3(abc, xyz)
    robot.inverse(end)


    print("inverse is successful: {0}".format(robot.is_reachable_inverse))
    print("axis values: \n{0}".format(robot.axis_values))
    robot.show()

if __name__ == "__main__":
    main()