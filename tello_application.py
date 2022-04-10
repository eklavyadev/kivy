# from djitellopy import Tello
import Tello.Tello as Tello
import cv2
import numpy as np
import time

# Speed of the drone
S = 60
# Frames per second of the pygame window display
# A low number also results in input lag, as input information is processed once per frame.
FPS = 120


class TelloApplication():
    """ Maintains the Tello display and moves it through the keyboard keys.
        Press escape key to quit.
        The controls are:
            - T: Takeoff
            - L: Land
            - Arrow keys: Forward, backward, left and right.
            - A and D: Counter clockwise and clockwise rotations (yaw)
            - W and S: Up and down.
    """

    def __init__(self):
        # Init Tello object that interacts with the Tello drone
        self.tello = Tello()

        # Drone velocities between -100~100
        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0
        self.speed = 10

        self.send_rc_control = False

    def run(self):

        self.tello.connect()
        self.tello.set_speed(self.speed)

        # In case streaming is on. This happens when we quit this program without the escape key.
        # self.tello.streamoff()
        # self.tello.streamon()

        # frame_read = self.tello.get_frame_read()

        # Call it always before finishing. To deallocate resources.
        self.tello.end()

    # def update(self):
    #     """ Update routine. Send velocities to Tello.
    #     """
    #     if self.send_rc_control:
    #         self.tello.send_rc_control(self.left_right_velocity, self.for_back_velocity,
    #                                    self.up_down_velocity, self.yaw_velocity)
