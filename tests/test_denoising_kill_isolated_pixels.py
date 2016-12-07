#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jérémie DECOCK (http://www.jdhp.org)

# This script is provided under the terms and conditions of the MIT license:
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
This module contains unit tests for the "denoising.kill_isolated_pixels" module.
"""

from datapipe.denoising.kill_isolated_pixels import kill_isolated_pixels

import numpy as np

import unittest

class TestKillIsolatedPixels(unittest.TestCase):
    """
    Contains unit tests for the "denoising.kill_isolated_pixels" module.
    """

    # Test the "kill_isolated_pixels" function #############################################

    def test_example1(self):
        """Check the output of the kill_isolated_pixels function."""

        # Input image #################

        # [[0 0 1 1 0 0]
        #  [0 0 0 1 0 0]
        #  [1 1 0 0 1 0]
        #  [0 0 0 1 0 0]]

        input_img = np.array([[0, 0, 1, 1, 0, 0],
                              [0, 0, 0, 1, 0, 0],
                              [1, 1, 0, 0, 1, 0],
                              [0, 0, 0, 1, 0, 0]])

        # Output image ################

        output_img = kill_isolated_pixels(input_img)

        # Expected output image #######

        # [[0 0 1 1 0 0]
        #  [0 0 0 1 0 0]
        #  [0 0 0 0 0 0]
        #  [0 0 0 0 0 0]]

        expected_output_img = np.array([[0, 0, 1, 1, 0, 0],
                                        [0, 0, 0, 1, 0, 0],
                                        [0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0]])

        np.testing.assert_array_equal(output_img, expected_output_img)
    

if __name__ == '__main__':
    unittest.main()
