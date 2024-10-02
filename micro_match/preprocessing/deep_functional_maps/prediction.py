import os

import numpy as np

from . import operations as ops

"""====================================================================================="""
"""                                       Training                                      """
"""====================================================================================="""


class dfmPredictor:
    def __init__(self, checkpoint_dir, chkpt_name, num_signatures):
        self.func = ops.residualNet(7, num_signatures, training=False)
        weight_path = os.path.join(checkpoint_dir, chkpt_name)
        self.func.load_weights(weight_path)

    def __call__(self, raw_signatures):
        raw_signatures = raw_signatures[np.newaxis].astype(np.float32)
        improved_signatures = self.func(raw_signatures)[0].numpy()
        return improved_signatures


if __name__ == "__main__":
    pass
