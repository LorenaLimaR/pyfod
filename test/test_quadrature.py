import numpy as np
import sympy as sp
import unittest
from pyfod import quadrature as qm


# --------------------------
class GLegTesting(unittest.TestCase):

    @classmethod
    def f(cls, t):
        return np.exp(2*t)

    def test_init(self):
        GL = qm.GaussLegendre(ndom=10, deg=6, lower=1.0, upper=12.0)
        attributes = ['points', 'weights', 'f', 'alpha', 'singularity',
                      'initial_weights', 'description']
        for att in attributes:
            self.assertTrue(hasattr(GL, att),
                            msg=str('Missing {} attribute'.format(att)))

    def test_update_weights(self):
        GLeg = qm.GaussLegendre(ndom=10, deg=3, lower=1.0, upper=12.0)
        GLeg.weights = []
        GLeg.update_weights(alpha=0.0)
        self.assertTrue(isinstance(GLeg.weights, np.ndarray),
                        msg='Weights should be updated.')

    def test_integrate(self):
        GLeg = qm.GaussLegendre(ndom=10, deg=3, lower=0.0, upper=1.0)
        a = GLeg.integrate(f=self.f)
        self.assertTrue(isinstance(a, float), msg='Expect float')


# --------------------------
class BaseGaussPoints(unittest.TestCase):

    def test_base_gauss_points(self):
        GQ = qm.GaussLegendre(ndom=10, deg=4, lower=1.0, upper=12.0)
        gpts = GQ._base_gauss_points(deg=4)
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
        GQ = qm.GaussLegendre(ndom=10, deg=4, lower=1.0, upper=12.0)
        gwts = GQ._base_gauss_weights(deg=4, h=0.1)
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
        GQ = qm.GaussLegendre(ndom=10, deg=4, lower=1.0, upper=12.0)
        igp = GQ._interval_gauss_points(
            base_gpts=GQ._base_gauss_points(deg=4),
            ndom=4, deg=4, h=0.1, lower=0.)
        self.assertEqual(igp.shape, (4*4,), msg='Expect shape = (16,)')


# --------------------------
class GaussPoints(unittest.TestCase):

    def test_gauss_points(self):
        GQ = qm.GaussLegendre(ndom=10, lower=1.0, upper=12.0)
        gpoints = GQ._gauss_points(ndom=4, deg=4, h=0.1, lower=0.)
        self.assertEqual(gpoints.shape, (4*4,), msg='Expect shape = (16,)')


# --------------------------
class GaussWeights(unittest.TestCase):

    def test_gauss_weights(self):
        GQ = qm.GaussLegendre(ndom=10, lower=1.0, upper=12.0)
        gweights = GQ._gauss_weights(ndom=4, deg=4, h=0.1)
        self.assertEqual(gweights.shape, (4*4,), msg='Expect shape = (16,)')


# --------------------------
class GaussLaguerreTesting(unittest.TestCase):

    @classmethod
    def f(cls, t):
        return np.exp(2*t)

    def test_init(self):
        Q = qm.GaussLaguerre(deg=10, lower=1.0, upper=12.0)
        attributes = ['points', 'weights', 'f', 'alpha',
                      'initial_weights', 'description', 'singularity']
        for att in attributes:
            self.assertTrue(hasattr(Q, att),
                            msg=str('Missing {} attribute'.format(att)))

    def test_update_weights(self):
        Q = qm.GaussLaguerre(deg=10, lower=1.0, upper=12.0,
                             extend_precision=False)
        Q.weights = []
        Q.update_weights(alpha=0.0)
        self.assertTrue(isinstance(Q.weights, np.ndarray),
                        msg='Weights should be updated.')

    def test_integrate(self):
        Q = qm.GaussLaguerre(deg=10, lower=0.0, upper=1.0,
                             extend_precision=False)
        a = Q.integrate(f=self.f)
        self.assertTrue(isinstance(a, float), msg='Expect float')


# --------------------------
class Initialization_non_extended(unittest.TestCase):

    @classmethod
    def f(cls, t):
        return np.exp(2*t)

    def test_init(self):
        GQ = qm.GaussLaguerre(deg=10, lower=1.0, upper=12.0,
                              extend_precision=False)
        self.assertTrue(hasattr(GQ, 'f'), msg='Expect attribute f to exist')
        self.assertEqual(GQ.f, None, msg='Expect value of None')
        self.assertEqual(GQ.points.size, 10, msg='Expect 10 nodes')
        self.assertEqual(GQ.weights.size, 10, msg='Expect 10 weights')
        self.assertEqual(GQ.alpha, 0, msg='Expect alpha eq 0')

    def test_init_with_f(self):
        GQ = qm.GaussLaguerre(deg=10, lower=1.0, upper=12.0, alpha=0.5,
                              f=self.f, extend_precision=False)
        self.assertTrue(hasattr(GQ, 'f'), msg='Expect attribute f to exist')
        self.assertEqual(GQ.f, self.f, msg='Expect function f')
        self.assertEqual(GQ.points.size, 10, msg='Expect 10 nodes')
        self.assertEqual(GQ.weights.size, 10, msg='Expect 10 weights')
        self.assertEqual(GQ.alpha, 0.5, msg='Expect alpha eq 0.5')


# --------------------------
class Initialization_with_extended(unittest.TestCase):

    @classmethod
    def fsp(t):
        return sp.cos(t)

    def test_init(self):
        GQ = qm.GaussLaguerre(deg=10, lower=1.0, upper=12.0)
        self.assertTrue(hasattr(GQ, 'f'), msg='Expect attribute f to exist')
        self.assertEqual(GQ.f, None, msg='Expect value of None')
        self.assertEqual(len(GQ.points), 10, msg='Expect 10 nodes')
        self.assertEqual(len(GQ.weights), 10, msg='Expect 10 weights')
        self.assertEqual(GQ.alpha, 0, msg='Expect alpha eq 0')

    def test_init_with_f(self):
        GQ = qm.GaussLaguerre(deg=10, lower=1.0, upper=12.0,
                              alpha=0.5, f=self.fsp)
        self.assertTrue(hasattr(GQ, 'f'), msg='Expect attribute f to exist')
        self.assertEqual(GQ.f, self.fsp, msg='Expect function fsp')
        self.assertEqual(len(GQ.points), 10, msg='Expect 10 nodes')
        self.assertEqual(len(GQ.weights), 10, msg='Expect 10 weights')
        self.assertEqual(GQ.alpha, 0.5, msg='Expect alpha eq 0.5')


# --------------------------
class Integrate_non_extended(unittest.TestCase):

    @classmethod
    def f(cls, t):
        return np.exp(2*t)

    def test_no_f(self):
        GQ = qm.GaussLaguerre(extend_precision=False)
        with self.assertRaises(SystemExit):
            GQ.integrate()

    def test_with_f(self):
        GQ = qm.GaussLaguerre(extend_precision=False)
        a = GQ.integrate(f=self.f)
        self.assertEqual(a.size, 1, msg='Expect float return')

    def test_with_alpha(self):
        GQ = qm.GaussLaguerre(extend_precision=False)
        a = GQ.integrate(f=self.f)
        self.assertEqual(a.size, 1, msg='Expect float return')


# --------------------------
class Integrate_with_extended(unittest.TestCase):

    @classmethod
    def fsp(cls, t):
        return sp.cos(t)

    def test_no_f(self):
        GQ = qm.GaussLaguerre()
        with self.assertRaises(SystemExit):
            GQ.integrate()

    def test_with_f(self):
        GQ = qm.GaussLaguerre()
        a = GQ.integrate(f=self.fsp)
        self.assertTrue(isinstance(a, float), msg='Expect float return')

    def test_with_alpha(self):
        GQ = qm.GaussLaguerre()
        a = GQ.integrate(f=self.fsp)
        self.assertTrue(isinstance(a, float), msg='Expect float return')


# --------------------------
class RiemannSumTesting(unittest.TestCase):

    @classmethod
    def f(cls, t):
        return np.exp(2*t)

    def test_init(self):
        RS = qm.RiemannSum(n=10, lower=1.0, upper=12.0)
        attributes = ['points', 'weights', 'f', 'alpha', 'grid', 'description',
                      'singularity']
        for att in attributes:
            self.assertTrue(hasattr(RS, att),
                            msg=str('Missing {} attribute'.format(att)))

    def test_update_weights(self):
        RS = qm.RiemannSum(n=10, lower=1.0, upper=12.0)
        RS.weights = []
        RS.update_weights(alpha=0.0)
        self.assertTrue(isinstance(RS.weights, np.ndarray),
                        msg='Weights should be updated.')

    def test_integrate(self):
        RS = qm.RiemannSum(n=10, lower=0.0, upper=1.0)
        a = RS.integrate(f=self.f)
        self.assertTrue(isinstance(a, float), msg='Expect float')

    def test_grid(self):
        RS = qm.RiemannSum()
        grid = RS._rs_grid(lower=1.0, upper=12.0, n=50)
        self.assertTrue(np.allclose(grid, np.linspace(1.0, 12.0, num=50)),
                        msg=str('Expect arrays equal: {} neq {}'.format(
                                grid, np.linspace(1.0, 12.0, num=50))))
        self.assertFalse(np.allclose(grid, np.linspace(2.0, 12.0, num=50)),
                         msg=str('Expect arrays not equal: {} eq {}'.format(
                                 grid, np.linspace(2.0, 12.0, num=50))))

    def test_rs_points(self):
        RS = qm.RiemannSum(n=10, lower=1.0, upper=12.0)
        self.assertTrue(isinstance(RS.points, np.ndarray),
                        msg='Output numpy array')
        grid = RS._rs_grid(n=10, lower=1.0, upper=12.0)
        jj = grid.size - 1
        values = (grid[1:jj+1] + grid[0:jj])/2
        self.assertTrue(np.allclose(RS.points, values),
                        msg=str('Expect arrays equal: {} neq {}'.format(
                                RS.points, values)))

    def different_alphas(self, alpha):
        RS = qm.RiemannSum(alpha=alpha, n=10, lower=1.0, upper=12.0)
        self.assertTrue(isinstance(RS.weights, np.ndarray),
                        msg='Output numpy array')
        grid = RS._rs_grid(n=10, lower=1.0, upper=12.0)
        jj = grid.size - 1
        term1 = (grid[jj] - grid[1:jj+1])**(1-alpha)
        term2 = (grid[jj] - grid[0:jj])**(1-alpha)
        values = -1/(1-alpha)*(term1 - term2)
        self.assertTrue(np.allclose(RS.weights, values),
                        msg=str('Expect arrays equal: {} neq {}'.format(
                                RS.weights, values)))

    def test_rs_weights(self):
        self.different_alphas(alpha=0.0)
        self.different_alphas(alpha=0.5)
        self.different_alphas(alpha=0.99)


# --------------------------
class GaussLegendreLaguerreTesting(unittest.TestCase):

    @classmethod
    def f(cls, t):
        try:
            tmp = np.exp(2*t)
        except AttributeError:
            tmp = sp.exp(2*t)
        return tmp

    def test_init(self):
        Q = qm.GaussLegendreGaussLaguerre(lower=1.0, upper=12.0)
        attributes = ['gleg', 'glag', 'f', 'alpha', 'description']
        for att in attributes:
            self.assertTrue(hasattr(Q, att),
                            msg=str('Missing {} attribute'.format(att)))

    def test_update_weights(self):
        Q = qm.GaussLegendreGaussLaguerre(lower=1.0, upper=12.0,
                                          percent=0.9)
        Q.gleg.weights = []
        Q.glag.weights = []
        Q.update_weights(alpha=0.0)
        self.assertTrue(isinstance(Q.gleg.weights, np.ndarray),
                        msg='Weights should be updated.')
        self.assertTrue(isinstance(Q.glag.weights,
                                   object),
                        msg='Weights should be updated.')
        self.assertEqual(Q.gleg.lower, 1.0,
                         msg='Expect GLeg lower limit = 1.0')
        self.assertEqual(Q.gleg.upper, (12.0-1.0)*0.9 + 1.0,
                         msg='Expect GLeg upper limit = 10.9')
        self.assertEqual(Q.glag.lower, (12.0-1.0)*0.9 + 1.0,
                         msg='Expect GLag lower limit = 10.9')
        self.assertEqual(Q.glag.upper, 12.0,
                         msg='Expect GLag upper limit = 12.0')

    def test_integrate(self):
        Q = qm.GaussLegendreGaussLaguerre(lower=0.0, upper=1.0)
        a = Q.integrate(f=self.f)
        self.assertTrue(isinstance(a, float),
                        msg='Expect float regardless of extended precision')
        Q = qm.GaussLegendreGaussLaguerre(lower=0.0, upper=1.0,
                                          extend_precision=False)
        a = Q.integrate(f=self.f)
        self.assertTrue(isinstance(a, float),
                        msg='Expect float if not extended')


# --------------------------
class GaussRiemannSumTesting(unittest.TestCase):

    @classmethod
    def f(cls, t):
        return np.exp(2*t)

    def test_init(self):
        Q = qm.GaussLegendreRiemannSum(lower=1.0, upper=12.0)
        attributes = ['gleg', 'rs', 'f', 'alpha', 'description']
        for att in attributes:
            self.assertTrue(hasattr(Q, att),
                            msg=str('Missing {} attribute'.format(att)))

    def test_update_weights(self):
        Q = qm.GaussLegendreRiemannSum(lower=1.0, upper=12.0,
                                       percent=0.9)
        Q.gleg.weights = []
        Q.rs.weights = []
        Q.update_weights(alpha=0.0)
        self.assertTrue(isinstance(Q.gleg.weights, np.ndarray),
                        msg='Weights should be updated.')
        self.assertTrue(isinstance(Q.rs.weights, np.ndarray),
                        msg='Weights should be updated.')
        self.assertEqual(Q.gleg.lower, 1.0,
                         msg='Expect GL lower limit = 1.0')
        self.assertEqual(Q.gleg.upper, (12.0-1.0)*0.9 + 1.0,
                         msg='Expect GL upper limit = 10.9')
        self.assertEqual(Q.rs.lower, (12.0-1.0)*0.9 + 1.0,
                         msg='Expect RS lower limit = 10.9')
        self.assertEqual(Q.rs.upper, 12.0,
                         msg='Expect RS upper limit = 12.0')

    def test_integrate(self):
        Q = qm.GaussLegendreRiemannSum(lower=0.0, upper=1.0)
        a = Q.integrate(f=self.f)
        self.assertTrue(isinstance(a, float), msg='Expect float')
