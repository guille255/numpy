"""Benchmarks for `numpy.lib`."""


from __future__ import absolute_import, division, print_function

from .common import Benchmark

import numpy as np


class Pad(Benchmark):
    """Benchmarks for `numpy.pad`."""

    param_names = ["shape", "pad_width", "mode"]
    params = [
        [(1000,), (10, 100), (10, 10, 10)],
        [1, 3, (0, 5)],
        ["constant", "edge", "linear_ramp", "mean", "reflect", "wrap"],
    ]

    def setup(self, shape, pad_width, mode):
        self.array = np.empty(shape)

    def time_pad(self, shape, pad_width, mode):
        np.pad(self.array, pad_width, mode)
