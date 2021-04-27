from collections import defaultdict

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf


class Adam():
    B1 = 0.9
    B2 = 0.999
    epsilon = 1e-8
    eta=0.01

    def __init__(self):
        self.m = [ 'dw': 0,
                   'db': 0 ]
        self.v = [ 'dw': 0,
                   'db': 0 ]

    @tf.function
    def update(self, t, w, b, dw, db):
        self.m = [ 'dw': self.B1 * self.m['dw'] + (1 - self.B1) * dw,
                   'db': self.B1 * self.m['db'] + (1 - self.B1) * db ]

        self.v = [ 'dw': self.B2 * self.v['dw'] + (1 - self.B2) * (dw ** 2),
                   'db': self.B2 * self.v['db'] + (1 - self.B2) * (db ** 2) ]

        corrected_m = 

        corrected_m = [ 'dw': self.m['dw'] / (1 - self.B1 ** t),
                        'db': self.m['db'] / (1 - self.B1 ** t) ]
        corrected_v = [ 'dw': self.m['dw'] / (1 - self.B2 ** t),
                        'db': self.m['db'] / (1 - self.B2 ** t) ]

        w = w - self.eta*(corrected_m['dw']/(tf.math.sqrt(corrected_m['dw']) + self.epsilon))
        b = b - self.eta*(corrected_m['db']/(tf.math.sqrt(corrected_m['db']) + self.epsilon))
        return w, b
