# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:14:07 2018

@author: prmiles
"""

import numpy as np
import unittest
from pyfod.GaussLegendre import GaussLegendre


# --------------------------
class BaseGaussPoints(unittest.TestCase):

    def test_base_gauss_points(self):
        GQ = GaussLegendre(N=10, start=1.0, finish=12.0)
        gpts = GQ.base_gauss_points()
        mlgpts = np.array([0.069431844202974, 0.330009478207572,
                           0.669990521792428, 0.930568155797026])
        self.assertEqual(gpts.size, 4, msg='Expect 4 elements')
        self.assertEqual(gpts.shape, (4,), msg='Expect shape = (4,)')
        self.assertTrue(np.allclose(gpts, mlgpts),
                        msg=str('Expect arrays to match: {} neq {}'.format(
                                gpts,
                                mlgpts)))


# --------------------------
class BaseGaussWeights(unittest.TestCase):

    def test_base_gauss_weights(self):
        GQ = GaussLegendre(N=10, start=1.0, finish=12.0)
        gwts = GQ.base_gauss_weights(h=0.1)
        mlgwts = np.array([0.017392742256873, 0.032607257743127,
                            0.032607257743127, 0.017392742256873]).T
        self.assertEqual(gwts.size, 4, msg='Expect 4 elements')
        self.assertEqual(gwts.shape, (4,), msg='Expect shape = (4,)')
        self.assertTrue(np.allclose(gwts, mlgwts),
                        msg=str('Expect arrays to match: {} neq {}'.format(
                                gwts, mlgwts)))


# --------------------------
class IntervalGaussPoints(unittest.TestCase):

    def test_interval_gauss_points(self):
        GQ = GaussLegendre(N=10, start=1.0, finish=12.0)
        igp = GQ.interval_gauss_points(
                base_gpts=GQ.base_gauss_points(),
                N=4, h=0.1, start=0.)
        self.assertEqual(igp.shape, (4*4,), msg='Expect shape = (16,)')


# --------------------------
class GaussPoints(unittest.TestCase):

    def test_gauss_points(self):
        GQ = GaussLegendre(N=10, start=1.0, finish=12.0)
        gpoints = GQ.gauss_points(N=4, h=0.1, start=0.)
        self.assertEqual(gpoints.shape, (4*4,), msg='Expect shape = (16,)')


# --------------------------
class GaussWeights(unittest.TestCase):

    def test_gauss_weights(self):
        GQ = GaussLegendre(N=10, start=1.0, finish=12.0)
        gweights = GQ.gauss_weights(N=4, h=0.1)
        self.assertEqual(gweights.shape, (4*4,), msg='Expect shape = (16,)')
