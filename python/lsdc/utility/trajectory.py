""" This file defines the sample class. """
import numpy as np


class Trajectory(object):
    def __init__(self, hyperparams):

        self.T = hyperparams['T']

        self._sample_images = np.zeros((self.T,
                                        hyperparams['image_height'],
                                        hyperparams['image_width'],
                                        hyperparams['image_channels']), dtype='uint8')

        self.U = np.empty([self.T, 2])
        self.X_full = np.empty([self.T, 2])
        self.Xdot_full = np.empty([self.T, 2])
        self.Object_pos = np.empty((self.T, hyperparams['num_objects'], 2))
        self.X_Xdot_full = np.empty([self.T, 4])

        self.desig_pos = np.empty([self.T, 2])
        self.score = np.empty([self.T])