#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit test suite for PoPPy

Copyright 2010-2014 Los Alamos National Security, LLC.
"""

import math
try:
    import StringIO
except ImportError:
    import io as StringIO
import sys
import unittest

import numpy
import numpy.random
import scipy.special
try:
    import poppy
except ImportError:
    from spacepy import poppy
from spacepy import toolbox

__all__ = ['BaseTests', 'BootstrapTests', 'AssocTests', 'ValuePercentileTests']


class BaseTests(unittest.TestCase):
    """Tests of basic functions in poppy"""
    def setUp(self):
        super(BaseTests, self).setUp()
        t1 = [655963,  70837, 681914, 671054, 120856,  52827, 674833, 727548,
              569743, 168496, 417843, 846365, 124030, 149118, 331591, 499616,
              401455, 484069, 470137, 476552, 105777, 711075, 688800, 544110,
              730248,  90896, 249113, 132259, 261126, 723237, 197802, 236209,
              239956, 231539, 537703, 528239, 354486, 135203, 357335, 683024,
              258661, 316019, 214481, 672555, 212034, 103213, 746137, 111065,
              436613, 286559, 511857, 489026,  32363, 275374, 342386, 192878,
              266724, 116734, 176916, 818199, 842720, 863230,  44519, 439228,
              419808, 179134, 639349, 763944, 605673, 507410, 618672, 828078,
              85643, 438461, 737909,  39394, 708392, 652198, 588335, 670095,
              675992, 580726, 455917, 267198, 708865, 423934, 126758, 537249,
              228845, 364992, 843165, 687482, 162219, 107074, 263547, 272363,
              838316, 574703, 421124, 484203]
        t2 = [757071, 820424, 522664, 399644, 558150, 342836, 834185,   9550,
              278019, 110750, 514961, 473701, 673490, 830021, 762821, 231852,
              662373, 729429, 545901, 409830, 432443, 649515, 446492, 286360,
              364346, 794408, 270865, 291723, 160511, 376046, 483439, 522531,
              92429, 642585, 803893,  61784, 116165, 405721, 565018,   3538,
              815125, 311551, 850973, 629556, 701310, 490674, 183441, 116949,
              388805, 457620, 302912,  75785, 717289, 424186, 370460,  93986,
              194428, 125804,  95628, 382477, 234520,  34429, 568429, 110523,
              519464, 530399, 244645, 345020, 690005, 750812, 237726, 549233,
              297069,  60590, 779392, 120764, 298320, 587738, 141891, 114935,
              585671, 138104, 752052, 585814, 670661, 281514, 148099, 682492,
              660800, 429724, 832390, 536037, 618901, 363413, 257753, 858464,
              674609, 191279, 337199, 193586]
        self.t1 = t1
        self.t2 = t2

    def tearDown(self):
        super(BaseTests, self).tearDown()

    def test_str(self):
        """__str__ should give known results"""
        pop = poppy.PPro(self.t1, self.t2)
        self.assertEqual(str(pop), 'Point Process Object:\n        Points in process #1 - 100 ; Points in process #2 - 100\n        Peak association number - N/A ; Asymptotic association - N/A\n        ')

    def test_len(self):
        """__len__ has a known behaviour"""
        pop = poppy.PPro(self.t1, self.t2)
        self.assertEqual(len(pop), 100)

    def test_swap(self):
        """swap() should swap the processes"""
        pop = poppy.PPro(self.t1, self.t2)
        pop.swap()
        self.assertEqual(pop.process1, self.t2)
        self.assertEqual(pop.process2, self.t1)

class BootstrapTests(unittest.TestCase):
    """Tests of the boots_ci function

    @ivar long_test: Run a very long test
    @type long_test: bool
    """

    def __init__(self, *args, **kwargs):
        super(BootstrapTests, self).__init__(*args, **kwargs)
        self.long_test = False

    def testGaussian(self):
        """Check output on a Gaussian"""
        gauss = lambda x: math.exp(-(x ** 2) / (2 * 5 ** 2)) / \
                          (5 * math.sqrt(2 * math.pi))
        mean = lambda x: sum(x) / len(x)
        if self.long_test:
            gauss_values = toolbox.dist_to_list(gauss, 5000)
            (ci_low, ci_high, prc) = poppy.boots_ci(
                gauss_values, 50000, 95.0, mean, seed=0, target=-0.138)
            #standard error on the mean for 5000 samples, standard dev 5 is
            #0.0707, 95% confidence interval is 1.96 standard dev or
            #0.13859292911256332 (+/-)
            self.assertAlmostEqual(-0.138373060749, ci_low, places=10)
            self.assertAlmostEqual(0.137630863579, ci_high, places=10)
            self.assertAlmostEqual(97.453789371746154, prc, places=10)
        else:
            gauss_values = toolbox.dist_to_list(gauss, 100)
            (ci_low, ci_high, prc) = poppy.boots_ci(
                gauss_values, 100, 95.0, mean, seed=0, target=-1.04)
            #for 100 samples, stderr is 0.5, 95% is +/- 0.98
            self.assertAlmostEqual(-1.03977357727, ci_low, places=10)
            self.assertAlmostEqual(0.914472603387, ci_high, places=10)
            self.assertAlmostEqual(97.502939756605045, prc, places=10)

    def testLogNormal(self):
        """Check output on a LogNormal"""
        lnorm = lambda x: math.exp(-1*(math.log(x) - 5.1)**2./(2*0.3**2.) ) \
                          / (x*math.sqrt(2*math.pi) * 0.3)

        if self.long_test:
            dist_values = toolbox.dist_to_list(lnorm, 5000, min=0)
            (ci_low, ci_high) = poppy.boots_ci(dist_values, 50000, 95.0,
                                               numpy.median, seed=0)
            #confidence interval is given as [exp(mu-sigma*q), exp(mu+sigma*q)]
            #where q is the (1 - alpha/2) quantile of the standard normal distr.
            #Here, the theoretical median is 164.022 (6 s.f.)
            self.assertAlmostEqual(162.31603275984526, ci_low, places=10)
            self.assertAlmostEqual(165.73324112594128, ci_high, places=10)
        else:
            dist_values = toolbox.dist_to_list(lnorm, 100, min=0)
            (ci_low, ci_high) = poppy.boots_ci(dist_values, 100, 95.0,
                                               numpy.median, seed=0)
            #TODO: the CI for lognorms should be calculated by the given form
            #currently this is just taken from the test code output
            #after the distributions have been calculated. The values do fit
            #with the theoretical median though...
            self.assertAlmostEqual(152.6079463660717, ci_low, places=10)
            self.assertAlmostEqual(174.61664971746504, ci_high, places=10)

    def testPoisson(self):
        """Check output on a continuous Poisson-like distribution"""
        l = 4 #Expected number of counts
        poiss = lambda k: l **k * math.exp(-l) / scipy.special.gamma(k + 1)
        mean = lambda x: sum(x) / len(x)
        if self.long_test:
            poiss_values = toolbox.dist_to_list(poiss, 5000, 0, 100)
            (ci_low, ci_high) = poppy.boots_ci(poiss_values, 50000, 95.0, mean,
                                               seed=0)
            #IF this were normal (which it isn't), expected confidence interval
            #3.94456 - 4.05544, in reality should be skewed right
            self.assertAlmostEqual(3.97171801164, ci_low, places=10)
            self.assertAlmostEqual(4.08051711605, ci_high, places=10)
        else:
            poiss_values = toolbox.dist_to_list(poiss, 100, 0, 100)
            (ci_low, ci_high) = poppy.boots_ci(poiss_values, 100, 95.0, mean,
                                               seed=0)
            #'Expected' 3.608 - 4.392
            self.assertAlmostEqual(3.57505503117, ci_low, places=10)
            self.assertAlmostEqual(4.4100232162, ci_high, places=10)


class AssocTests(unittest.TestCase):
    """Tests of association analysis"""

    def setUp(self):
        """Create arrays of data used by various tests"""
        super(AssocTests, self).setUp()
        #Created from numpy.random.randint(0, 864000, [100])
        t1 = [655963,  70837, 681914, 671054, 120856,  52827, 674833, 727548,
              569743, 168496, 417843, 846365, 124030, 149118, 331591, 499616,
              401455, 484069, 470137, 476552, 105777, 711075, 688800, 544110,
              730248,  90896, 249113, 132259, 261126, 723237, 197802, 236209,
              239956, 231539, 537703, 528239, 354486, 135203, 357335, 683024,
              258661, 316019, 214481, 672555, 212034, 103213, 746137, 111065,
              436613, 286559, 511857, 489026,  32363, 275374, 342386, 192878,
              266724, 116734, 176916, 818199, 842720, 863230,  44519, 439228,
              419808, 179134, 639349, 763944, 605673, 507410, 618672, 828078,
              85643, 438461, 737909,  39394, 708392, 652198, 588335, 670095,
              675992, 580726, 455917, 267198, 708865, 423934, 126758, 537249,
              228845, 364992, 843165, 687482, 162219, 107074, 263547, 272363,
              838316, 574703, 421124, 484203]
        t2 = [757071, 820424, 522664, 399644, 558150, 342836, 834185,   9550,
              278019, 110750, 514961, 473701, 673490, 830021, 762821, 231852,
              662373, 729429, 545901, 409830, 432443, 649515, 446492, 286360,
              364346, 794408, 270865, 291723, 160511, 376046, 483439, 522531,
              92429, 642585, 803893,  61784, 116165, 405721, 565018,   3538,
              815125, 311551, 850973, 629556, 701310, 490674, 183441, 116949,
              388805, 457620, 302912,  75785, 717289, 424186, 370460,  93986,
              194428, 125804,  95628, 382477, 234520,  34429, 568429, 110523,
              519464, 530399, 244645, 345020, 690005, 750812, 237726, 549233,
              297069,  60590, 779392, 120764, 298320, 587738, 141891, 114935,
              585671, 138104, 752052, 585814, 670661, 281514, 148099, 682492,
              660800, 429724, 832390, 536037, 618901, 363413, 257753, 858464,
              674609, 191279, 337199, 193586]
        self.t1 = t1
        self.t2 = t2
        expected_low = ['0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.e666666666668p-2', '0x0.0p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+1', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.e666666666668p-2', '0x1.0000000000000p+0', '0x1.3cccccccccccdp+1', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.799999999999ap+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+1', '0x1.799999999999ap+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.e666666666668p-2', '0x0.0p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.3cccccccccccdp+1', '0x1.0000000000000p+1', '0x1.799999999999ap+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x1.799999999999ap+0', '0x1.0000000000000p+0', '0x1.8000000000000p+1', '0x1.8000000000000p+1', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.e666666666668p-2', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+1', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.799999999999ap+0', '0x1.8000000000000p+1', '0x1.0000000000000p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x1.e666666666668p-2', '0x1.0000000000000p+0', '0x1.799999999999ap+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x0.0p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+1', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x1.e666666666668p-2', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.799999999999ap+0', '0x1.e666666666668p-2', '0x1.0000000000000p+1', '0x1.0000000000000p+1', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.799999999999ap+0', '0x1.0000000000000p+0', '0x1.0000000000000p+1', '0x1.0000000000000p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.e666666666668p-2', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+1', '0x1.799999999999ap+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+1', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+1', '0x1.0000000000000p+1', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.799999999999ap+0', '0x1.0000000000000p+1', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+1', '0x1.0000000000000p+1', '0x1.e666666666668p-2', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x1.e666666666668p-2', '0x1.0000000000000p+1', '0x1.0000000000000p+1', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x1.0000000000000p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x1.0000000000000p+0']
        expected_high = ['0x1.8000000000000p+2', '0x1.4000000000000p+2', '0x1.8000000000000p+1', '0x1.8000000000000p+1', '0x1.c333333333320p+2', '0x1.6199999999990p+2', '0x1.6199999999990p+2', '0x1.0000000000000p+3', '0x1.8000000000000p+2', '0x1.4000000000000p+2', '0x1.c000000000000p+2', '0x1.c333333333320p+1', '0x0.0p+0', '0x1.8000000000000p+2', '0x1.4000000000000p+2', '0x1.4000000000000p+2', '0x1.4000000000000p+3', '0x1.4000000000000p+3', '0x1.50cccccccccc8p+3', '0x1.8000000000000p+2', '0x0.0p+0', '0x1.8000000000000p+2', '0x1.6000000000000p+3', '0x1.0000000000000p+3', '0x1.2000000000000p+3', '0x1.0000000000000p+3', '0x1.30cccccccccc8p+3', '0x1.8000000000000p+3', '0x1.0000000000000p+3', '0x1.8000000000000p+1', '0x1.8000000000000p+2', '0x1.4000000000000p+2', '0x1.c000000000000p+2', '0x1.10cccccccccc8p+3', '0x1.50cccccccccc8p+3', '0x1.c000000000000p+2', '0x1.a199999999990p+2', '0x1.6199999999990p+2', '0x1.2199999999990p+2', '0x1.8000000000000p+2', '0x1.30cccccccccc8p+3', '0x1.6000000000000p+3', '0x1.2000000000000p+3', '0x1.4000000000000p+2', '0x1.8000000000000p+1', '0x1.8000000000000p+2', '0x1.0000000000000p+3', '0x1.c000000000000p+2', '0x1.c333333333320p+2', '0x1.2000000000000p+3', '0x1.8000000000000p+2', '0x1.8000000000000p+1', '0x1.8000000000000p+1', '0x1.c333333333320p+1', '0x1.4000000000000p+2', '0x1.c000000000000p+2', '0x1.4000000000000p+2', '0x1.e199999999990p+2', '0x1.6000000000000p+3', '0x1.8000000000000p+3', '0x1.10cccccccccc8p+3', '0x1.4000000000000p+2', '0x1.2000000000000p+3', '0x1.70cccccccccc8p+3', '0x1.e199999999990p+2', '0x1.90cccccccccc8p+3', '0x1.4000000000000p+3', '0x1.4000000000000p+2', '0x1.c000000000000p+2', '0x1.2000000000000p+3', '0x1.e199999999990p+2', '0x1.c000000000000p+2', '0x1.e199999999990p+2', '0x1.2000000000000p+3', '0x1.2000000000000p+3', '0x1.8000000000000p+1', '0x1.6199999999990p+2', '0x1.e199999999990p+2', '0x1.c000000000000p+2', '0x1.4000000000000p+2', '0x1.0199999999990p+3', '0x1.8000000000000p+2', '0x1.0000000000000p+2', '0x1.0000000000000p+3', '0x1.2199999999990p+3', '0x1.4000000000000p+2', '0x1.c000000000000p+2', '0x1.2000000000000p+3', '0x1.c333333333320p+1', '0x1.8000000000000p+1', '0x1.a199999999990p+2', '0x1.0000000000000p+3', '0x1.8000000000000p+2', '0x1.0000000000000p+2', '0x1.70cccccccccc8p+3', '0x1.6000000000000p+3', '0x1.6199999999990p+2', '0x1.0000000000000p+3', '0x1.a199999999990p+2', '0x1.6199999999990p+2', '0x1.2199999999990p+2', '0x1.4000000000000p+2', '0x1.8000000000000p+2', '0x1.4000000000000p+2', '0x1.8000000000000p+2', '0x1.a199999999990p+2', '0x1.8000000000000p+2', '0x1.2000000000000p+3', '0x1.4000000000000p+2', '0x1.0000000000000p+3', '0x1.8000000000000p+2', '0x1.4333333333320p+1', '0x1.8000000000000p+1', '0x0.0p+0', '0x0.0p+0', '0x1.4000000000000p+2', '0x1.8000000000000p+2', '0x1.0000000000000p+2', '0x1.8000000000000p+1', '0x1.8000000000000p+1', '0x1.8000000000000p+1', '0x1.8000000000000p+2', '0x1.0000000000000p+3', '0x1.2199999999990p+2', '0x1.c333333333320p+1', '0x1.c333333333320p+1', '0x1.8000000000000p+1', '0x0.0p+0', '0x1.4000000000000p+2', '0x1.30cccccccccc8p+3', '0x1.a000000000000p+3', '0x1.10cccccccccc8p+3', '0x1.a199999999990p+2', '0x1.c000000000000p+2', '0x1.8000000000000p+2', '0x1.4000000000000p+2', '0x1.a199999999990p+2', '0x1.0000000000000p+3', '0x1.0000000000000p+3', '0x1.50cccccccccc8p+3', '0x1.10cccccccccc8p+3', '0x1.0000000000000p+2', '0x1.c000000000000p+2', '0x1.c000000000000p+2', '0x1.0000000000000p+2', '0x1.2199999999990p+2', '0x1.c000000000000p+2', '0x1.c000000000000p+2', '0x1.c000000000000p+2', '0x1.a199999999990p+2', '0x1.8000000000000p+1', '0x1.8000000000000p+1', '0x1.c333333333320p+1', '0x0.0p+0', '0x1.8000000000000p+1', '0x1.8000000000000p+1', '0x1.8000000000000p+2', '0x1.0000000000000p+3', '0x1.0000000000000p+3', '0x1.e199999999990p+2', '0x1.0000000000000p+2', '0x1.0000000000000p+3', '0x1.0000000000000p+3', '0x1.4000000000000p+2', '0x1.8000000000000p+1', '0x1.8000000000000p+2', '0x1.c000000000000p+2', '0x1.8000000000000p+1', '0x1.0000000000000p+2', '0x1.50cccccccccc8p+3', '0x1.4000000000000p+3', '0x1.8000000000000p+1', '0x1.4000000000000p+2', '0x1.0000000000000p+3', '0x1.0000000000000p+3', '0x1.6199999999990p+2', '0x1.c333333333320p+1', '0x1.4000000000000p+2', '0x1.2199999999990p+2', '0x1.0000000000000p+3', '0x1.0000000000000p+3', '0x1.4000000000000p+2', '0x1.a199999999990p+2', '0x1.4000000000000p+3', '0x1.2000000000000p+3', '0x1.4199999999990p+3', '0x1.90cccccccccc8p+3', '0x1.2000000000000p+3', '0x1.8000000000000p+1', '0x1.8000000000000p+1', '0x1.6199999999990p+2', '0x1.8000000000000p+2', '0x1.0000000000000p+3', '0x1.2000000000000p+3', '0x1.0000000000000p+3', '0x1.4000000000000p+3', '0x1.30cccccccccc8p+3', '0x1.a199999999990p+2', '0x1.0000000000000p+3', '0x1.0000000000000p+3', '0x1.e199999999990p+2', '0x1.4000000000000p+2', '0x1.0000000000000p+3', '0x1.8000000000000p+2', '0x1.8000000000000p+2', '0x1.e199999999990p+2', '0x1.4000000000000p+2', '0x1.0000000000000p+3', '0x1.e199999999990p+2', '0x1.0000000000000p+3', '0x1.8000000000000p+2', '0x1.4000000000000p+2', '0x1.c000000000000p+2', '0x1.0000000000000p+3', '0x1.30cccccccccc8p+3', '0x1.4000000000000p+3', '0x1.2000000000000p+3', '0x1.4000000000000p+2', '0x1.e199999999990p+2', '0x1.6000000000000p+3', '0x1.10cccccccccc8p+3', '0x1.0000000000000p+2', '0x0.0p+0', '0x0.0p+0', '0x1.2199999999990p+2', '0x1.c000000000000p+2', '0x1.6000000000000p+3', '0x1.4000000000000p+3', '0x1.8000000000000p+2', '0x1.4000000000000p+2', '0x1.8000000000000p+1', '0x1.4000000000000p+2', '0x1.2199999999990p+2', '0x1.8000000000000p+1', '0x1.8000000000000p+2', '0x1.6000000000000p+3', '0x1.8000000000000p+3', '0x1.e199999999990p+2', '0x1.4000000000000p+3', '0x1.0000000000000p+3', '0x1.4000000000000p+2', '0x1.6199999999990p+2', '0x1.a199999999990p+2', '0x1.c000000000000p+2', '0x1.0000000000000p+3', '0x1.10cccccccccc8p+3', '0x1.6199999999990p+2', '0x1.8000000000000p+1', '0x1.4000000000000p+2', '0x1.c000000000000p+2', '0x1.4000000000000p+2', '0x1.8000000000000p+2', '0x1.10cccccccccc8p+3', '0x1.e199999999990p+2', '0x1.0000000000000p+3', '0x1.c000000000000p+2', '0x1.8000000000000p+1', '0x0.0p+0', '0x1.6199999999990p+2', '0x1.8000000000000p+2', '0x1.8000000000000p+2', '0x1.6000000000000p+3', '0x1.50cccccccccc8p+3', '0x1.8000000000000p+2', '0x1.0000000000000p+3', '0x1.e199999999990p+2', '0x1.8000000000000p+2', '0x1.a199999999990p+2', '0x1.a199999999990p+2', '0x1.6199999999990p+2', '0x1.a199999999990p+2', '0x1.8000000000000p+3', '0x1.4000000000000p+3', '0x1.8000000000000p+1', '0x0.0p+0', '0x1.8000000000000p+2', '0x1.c000000000000p+2', '0x1.50cccccccccc8p+3', '0x1.10cccccccccc8p+3', '0x0.0p+0', '0x1.4000000000000p+2', '0x1.8000000000000p+2', '0x1.8000000000000p+1', '0x1.4000000000000p+2', '0x1.6199999999990p+2', '0x1.c333333333320p+1', '0x0.0p+0', '0x1.8000000000000p+2', '0x1.8000000000000p+2']
        expected_conf_above = ['0x1.ccf451ad6e4cep+5', '0x1.b50f6d0d4934cp+4', '0x1.055f51f1e9590p+2', '0x1.244d65bd7b238p+3', '0x1.a48ce27c4caf2p+5', '0x1.2b5694e8e7d5ep+5', '0x1.1b2d353ba7306p+5', '0x1.3b535f244a8b4p+6', '0x1.02c29045e8481p+6', '0x1.b4b642298d54ap+5', '0x1.ed471107ef97ep+5', '0x1.86aa4f5bee850p+2', '0x0.0p+0', '0x1.3b7ff496287b6p+5', '0x1.1b2d353ba7306p+5', '0x1.0b03d58e668aep+5', '0x1.43680efaeade0p+6', '0x1.6bcf7e2c0c7bcp+6', '0x1.333eaf4daa388p+6', '0x1.d50901840e9fap+5', '0x0.0p+0', '0x1.0b03d58e668aep+5', '0x1.4b7cbed18b30cp+6', '0x1.4b7cbed18b30cp+6', '0x1.333eaf4daa388p+6', '0x1.1b009fc9c9404p+6', '0x1.53916ea82b838p+6', '0x1.840d8dafed740p+6', '0x1.37490738fa61ep+6', '0x1.4604d0a6ebef0p+2', '0x1.02ef25b7c6382p+5', '0x1.1b2d353ba7306p+5', '0x1.8c4ed2f86bb6ep+5', '0x1.43680efaeade0p+6', '0x1.7bf8ddd94d214p+6', '0x1.3f5db70f9ab4ap+6', '0x1.c4dfa1d6cdfa2p+5', '0x1.aca19252ed01ep+5', '0x1.e58b8c150b254p+4', '0x1.bccaf2002da76p+5', '0x1.2f3457625a0f2p+6', '0x1.73e42e02acce8p+6', '0x1.6bcf7e2c0c7bcp+6', '0x1.c538ccba89da4p+4', '0x1.8545a3ccff048p+3', '0x1.bccaf2002da76p+5', '0x1.271fa78bb9bc6p+6', '0x1.12ebeff328ed8p+6', '0x1.0ee19807d8c42p+6', '0x1.43680efaeade0p+6', '0x1.d50901840e9fap+5', '0x1.055f51f1e9590p+2', '0x1.44a02517fc6e8p+3', '0x1.03faa662f9d88p+3', '0x1.2341e51247832p+5', '0x1.02c29045e8481p+6', '0x1.2341e51247832p+5', '0x1.271fa78bb9bc6p+6', '0x1.840d8dafed740p+6', '0x1.7bf8ddd94d214p+6', '0x1.5fb0766a1bffap+6', '0x1.1318856506ddap+5', '0x1.333eaf4daa388p+6', '0x1.73e42e02acce8p+6', '0x1.43680efaeade0p+6', '0x1.8c223d868dc6cp+6', '0x1.8c0bf2cd9ecebp+6', '0x1.e58b8c150b254p+4', '0x1.d50901840e9fap+5', '0x1.477266e63b076p+6', '0x1.1b009fc9c9404p+6', '0x1.946382cf0c09ap+5', '0x1.579bc6937bacep+6', '0x1.3f5db70f9ab4ap+6', '0x1.2b29ff7709e5cp+6', '0x1.86aa4f5bee850p+2', '0x1.d5622c67ca7fcp+4', '0x1.333eaf4daa388p+6', '0x1.ccf451ad6e4cep+5', '0x1.d5622c67ca7fcp+4', '0x1.02c29045e8481p+6', '0x1.c4dfa1d6cdfa2p+5', '0x1.64f2e4727db98p+3', '0x1.bccaf2002da76p+5', '0x1.5ba61e7ecbd64p+6', '0x1.f5b4ebc24bcacp+4', '0x1.e53261314f452p+5', '0x1.3f5db70f9ab4ap+6', '0x1.03faa662f9d88p+3', '0x1.64f2e4727db98p+3', '0x1.dd1db15aaef26p+5', '0x1.23154fa069930p+6', '0x1.c4dfa1d6cdfa2p+5', '0x1.e58b8c150b254p+4', '0x1.77ee85edfcf7ep+6', '0x1.73e42e02acce8p+6', '0x1.1b2d353ba7306p+5', '0x1.c4dfa1d6cdfa2p+5', '0x1.7c25734b2b116p+5', '0x1.b50f6d0d4934cp+4', '0x1.0b03d58e668aep+5', '0x1.0b03d58e668aep+5', '0x1.dd1db15aaef26p+5', '0x1.02ef25b7c6382p+5', '0x1.06cce83138717p+6', '0x1.8c4ed2f86bb6ep+5', '0x1.d50901840e9fap+5', '0x1.333eaf4daa388p+6', '0x1.0b03d58e668aep+5', '0x1.333eaf4daa388p+6', '0x1.8c4ed2f86bb6ep+5', '0x1.0828a90fc85a0p+1', '0x1.4604d0a6ebef0p+2', '0x0.0p+0', '0x0.0p+0', '0x1.b50f6d0d4934cp+4', '0x1.e53261314f452p+5', '0x1.03faa662f9d88p+3', '0x1.86aa4f5bee850p+2', '0x1.244d65bd7b238p+3', '0x1.64f2e4727db98p+3', '0x1.aca19252ed01ep+5', '0x1.f55bc0de8feaap+5', '0x1.a4e60d60088f4p+4', '0x1.c74fce10f11b0p+2', '0x1.055f51f1e9590p+2', '0x1.055f51f1e9590p+2', '0x0.0p+0', '0x1.94bcadb2c7e9cp+4', '0x1.6bcf7e2c0c7bcp+6', '0x1.8817e59b3d9d6p+6', '0x1.271fa78bb9bc6p+6', '0x1.ccf451ad6e4cep+5', '0x1.37490738fa61ep+6', '0x1.02c29045e8481p+6', '0x1.1318856506ddap+5', '0x1.aca19252ed01ep+5', '0x1.2b29ff7709e5cp+6', '0x1.3b535f244a8b4p+6', '0x1.6fd9d6175ca52p+6', '0x1.4b7cbed18b30cp+6', '0x1.54172efdc5540p+4', '0x1.0ad7401c889adp+6', '0x1.e53261314f452p+5', '0x1.244d65bd7b238p+3', '0x1.a4e60d60088f4p+4', '0x1.1b009fc9c9404p+6', '0x1.ccf451ad6e4cep+5', '0x1.ed471107ef97ep+5', '0x1.aca19252ed01ep+5', '0x1.244d65bd7b238p+3', '0x1.03faa662f9d88p+3', '0x1.244d65bd7b238p+3', '0x0.0p+0', '0x1.86aa4f5bee850p+2', '0x1.244d65bd7b238p+3', '0x1.c4dfa1d6cdfa2p+5', '0x1.23154fa069930p+6', '0x1.477266e63b076p+6', '0x1.23154fa069930p+6', '0x1.64408eab05f94p+4', '0x1.2f3457625a0f2p+6', '0x1.23154fa069930p+6', '0x1.d5622c67ca7fcp+4', '0x1.4604d0a6ebef0p+2', '0x1.946382cf0c09ap+5', '0x1.e53261314f452p+5', '0x1.03faa662f9d88p+3', '0x1.02ef25b7c6382p+5', '0x1.800335c49d4aap+6', '0x1.5ba61e7ecbd64p+6', '0x1.244d65bd7b238p+3', '0x1.1b2d353ba7306p+5', '0x1.43680efaeade0p+6', '0x1.53916ea82b838p+6', '0x1.e58b8c150b254p+4', '0x1.4604d0a6ebef0p+2', '0x1.2b5694e8e7d5ep+5', '0x1.a4e60d60088f4p+4', '0x1.23154fa069930p+6', '0x1.2b29ff7709e5cp+6', '0x1.0b03d58e668aep+5', '0x1.ed471107ef97ep+5', '0x1.4b7cbed18b30cp+6', '0x1.23154fa069930p+6', '0x1.579bc6937bacep+6', '0x1.800335c49d4aap+6', '0x1.2f3457625a0f2p+6', '0x1.c74fce10f11b0p+2', '0x1.4604d0a6ebef0p+2', '0x1.c538ccba89da4p+4', '0x1.02c29045e8481p+6', '0x1.333eaf4daa388p+6', '0x1.333eaf4daa388p+6', '0x1.477266e63b076p+6', '0x1.77ee85edfcf7ep+6', '0x1.43680efaeade0p+6', '0x1.bccaf2002da76p+5', '0x1.23154fa069930p+6', '0x1.4f8716bcdb5a2p+6', '0x1.c4dfa1d6cdfa2p+5', '0x1.2b5694e8e7d5ep+5', '0x1.3b535f244a8b4p+6', '0x1.d50901840e9fap+5', '0x1.b4b642298d54ap+5', '0x1.ccf451ad6e4cep+5', '0x1.1b2d353ba7306p+5', '0x1.23154fa069930p+6', '0x1.3f5db70f9ab4ap+6', '0x1.4b7cbed18b30cp+6', '0x1.aca19252ed01ep+5', '0x1.84934e0587444p+4', '0x1.ed471107ef97ep+5', '0x1.37490738fa61ep+6', '0x1.5ba61e7ecbd64p+6', '0x1.7bf8ddd94d214p+6', '0x1.477266e63b076p+6', '0x1.2b5694e8e7d5ep+5', '0x1.333eaf4daa388p+6', '0x1.7bf8ddd94d214p+6', '0x1.333eaf4daa388p+6', '0x1.1b2d353ba7306p+5', '0x0.0p+0', '0x0.0p+0', '0x1.e58b8c150b254p+4', '0x1.b4b642298d54ap+5', '0x1.7bf8ddd94d214p+6', '0x1.7bf8ddd94d214p+6', '0x1.946382cf0c09ap+5', '0x1.1b2d353ba7306p+5', '0x1.8973a679cd860p+1', '0x1.d5622c67ca7fcp+4', '0x1.f5b4ebc24bcacp+4', '0x1.8973a679cd860p+1', '0x1.c4dfa1d6cdfa2p+5', '0x1.6fd9d6175ca52p+6', '0x1.5ba61e7ecbd64p+6', '0x1.2f3457625a0f2p+6', '0x1.6fd9d6175ca52p+6', '0x1.5fb0766a1bffap+6', '0x1.c538ccba89da4p+4', '0x1.f5b4ebc24bcacp+4', '0x1.ed471107ef97ep+5', '0x1.2f3457625a0f2p+6', '0x1.37490738fa61ep+6', '0x1.2f3457625a0f2p+6', '0x1.02ef25b7c6382p+5', '0x1.c74fce10f11b0p+2', '0x1.02ef25b7c6382p+5', '0x1.9c7832a5ac5c6p+5', '0x1.d5622c67ca7fcp+4', '0x1.aca19252ed01ep+5', '0x1.3b535f244a8b4p+6', '0x1.d50901840e9fap+5', '0x1.271fa78bb9bc6p+6', '0x1.fd7070b5303d6p+5', '0x1.055f51f1e9590p+2', '0x0.0p+0', '0x1.02ef25b7c6382p+5', '0x1.ccf451ad6e4cep+5', '0x1.2f3457625a0f2p+6', '0x1.800335c49d4aap+6', '0x1.5fb0766a1bffap+6', '0x1.a48ce27c4caf2p+5', '0x1.1b009fc9c9404p+6', '0x1.ed471107ef97ep+5', '0x1.aca19252ed01ep+5', '0x1.fd7070b5303d6p+5', '0x1.f55bc0de8feaap+5', '0x1.0b03d58e668aep+5', '0x1.ccf451ad6e4cep+5', '0x1.7bf8ddd94d214p+6', '0x1.77ee85edfcf7ep+6', '0x1.244d65bd7b238p+3', '0x0.0p+0', '0x1.d50901840e9fap+5', '0x1.271fa78bb9bc6p+6', '0x1.77ee85edfcf7ep+6', '0x1.16f647de7916ep+6', '0x0.0p+0', '0x1.02ef25b7c6382p+5', '0x1.b50f6d0d4934cp+4', '0x1.c74fce10f11b0p+2', '0x1.d5622c67ca7fcp+4', '0x1.f5b4ebc24bcacp+4', '0x1.64f2e4727db98p+3', '0x0.0p+0', '0x1.1318856506ddap+5', '0x1.ccf451ad6e4cep+5']
        self.expected_low = [float.fromhex(i) for i in expected_low]
        self.expected_high = [float.fromhex(i) for i in expected_high]
        self.expected_conf_above = [float.fromhex(i)
                                    for i in expected_conf_above]

    def testAssocRegress(self):
        """Test entire association analysis

        This is a regression test: values are taken from existing
        implementation and assumed correct.
        """
        pop = poppy.PPro(self.t1, self.t2)
        lags = [(i - 144) * 120 for i in range(289)]
        pop.assoc(lags, 120)
        expected = [3.0, 2.0, 1.0, 1.0, 3.0, 2.0, 2.0, 4.0, 3.0, 3.0, 3.0, 1.0,
                    0.0, 2.0, 2.0, 2.0, 5.0, 5.0, 5.0, 3.0, 0.0, 2.0, 5.0, 5.0,
                    4.0, 4.0, 5.0, 7.0, 4.0, 1.0, 2.0, 2.0, 3.0, 4.0, 6.0, 4.0,
                    3.0, 3.0, 2.0, 3.0, 4.0, 6.0, 5.0, 2.0, 1.0, 3.0, 4.0, 3.0,
                    3.0, 4.0, 3.0, 1.0, 1.0, 1.0, 2.0, 3.0, 2.0, 4.0, 6.0, 7.0,
                    5.0, 2.0, 4.0, 5.0, 4.0, 7.0, 6.0, 2.0, 3.0, 5.0, 4.0, 3.0,
                    4.0, 5.0, 4.0, 1.0, 2.0, 4.0, 3.0, 2.0, 3.0, 3.0, 1.0, 3.0,
                    5.0, 2.0, 3.0, 4.0, 1.0, 1.0, 3.0, 4.0, 3.0, 2.0, 6.0, 6.0,
                    2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 3.0, 2.0, 3.0, 3.0, 3.0, 4.0,
                    2.0, 4.0, 3.0, 1.0, 1.0, 0.0, 0.0, 2.0, 3.0, 1.0, 1.0, 1.0,
                    1.0, 3.0, 3.0, 2.0, 1.0, 1.0, 1.0, 0.0, 2.0, 5.0, 6.0, 4.0,
                    3.0, 4.0, 3.0, 2.0, 3.0, 4.0, 4.0, 6.0, 5.0, 2.0, 3.0, 3.0,
                    1.0, 2.0, 4.0, 3.0, 3.0, 3.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0,
                    3.0, 4.0, 4.0, 4.0, 2.0, 4.0, 4.0, 2.0, 1.0, 3.0, 3.0, 1.0,
                    2.0, 6.0, 5.0, 1.0, 2.0, 4.0, 4.0, 2.0, 1.0, 2.0, 2.0, 4.0,
                    4.0, 2.0, 3.0, 5.0, 4.0, 5.0, 7.0, 4.0, 1.0, 1.0, 2.0, 3.0,
                    4.0, 4.0, 4.0, 6.0, 5.0, 3.0, 4.0, 4.0, 3.0, 2.0, 4.0, 3.0,
                    3.0, 3.0, 2.0, 4.0, 4.0, 4.0, 3.0, 2.0, 3.0, 4.0, 5.0, 6.0,
                    4.0, 2.0, 4.0, 6.0, 4.0, 2.0, 0.0, 0.0, 2.0, 3.0, 6.0, 6.0,
                    3.0, 2.0, 1.0, 2.0, 2.0, 1.0, 3.0, 6.0, 5.0, 4.0, 6.0, 5.0,
                    2.0, 2.0, 3.0, 4.0, 4.0, 4.0, 2.0, 1.0, 2.0, 3.0, 2.0, 3.0,
                    4.0, 3.0, 4.0, 3.0, 1.0, 0.0, 2.0, 3.0, 4.0, 6.0, 5.0, 3.0,
                    4.0, 3.0, 3.0, 3.0, 3.0, 2.0, 3.0, 7.0, 5.0, 1.0, 0.0, 3.0,
                    4.0, 6.0, 4.0, 0.0, 2.0, 2.0, 1.0, 2.0, 2.0, 1.0, 0.0, 2.0,
                    3.0]
        self.assertEqual(expected, list(pop.assoc_total))

    def testAssocBootstrapRegress(self):
        """Test entire association analysis with bootstrap

        This is a regression test: values are taken from existing
        implementation and assumed correct.
        """
        pop = poppy.PPro(self.t1, self.t2)
        lags = [(i - 144) * 120 for i in range(289)]
        pop.assoc(lags, 120)
        pop.aa_ci(95, n_boots=100, seed=0)
        #Know that the code runs at this point, but do not have expected values
        #for these platforms (test assumes 64-bit seed).
        if sys.maxsize <= 2 ** 31 \
           or sys.platform.startswith('win'):
            return
        self.assertEqual(self.expected_low, list(pop.ci[0]))
        self.assertEqual(self.expected_high, list(pop.ci[1]))
        self.assertEqual(self.expected_conf_above,
                         list(pop.conf_above))

    def testAssocDirection(self):
        """Test that AA gives same answer for either order of series"""
        lags = [(i - 144) * 120 for i in range(289)]
        pop = poppy.PPro(self.t1, self.t2, lags=lags, winhalf=120)
        pop.assoc()
        poprev = poppy.PPro(self.t2, self.t1, lags=lags[-1::-1], winhalf=120)
        poprev.assoc()
        self.assertTrue((pop.assoc_total == poprev.assoc_total).all())


class ValuePercentileTests(unittest.TestCase):
    """Tests of the value_percentile function"""

    def testValuePercentile(self):
        """Series of tests of ValuePercentile"""

        #Sequences on which to find the percentile
        sequences = [[3, 8, 12, 14, 31, 33, 35, 39, 41, 57, 61,
                      65, 65, 69, 79, 81, 82, 86, 88, 92],
                     [-9.0, -6.0, -5.8, -2.5, 1.1, 3.8, 6.2, 9.8, 9.9, 9.9],
                     ]
        #Target values to find within each sequence, multiple per sequence
        targets = [[0, 8, 40, 80, 90],
                   [-9.1, 3.1, 5.7, 8.9],
                   ]
        for sequence, target in zip(sequences, targets):
            for t in target:
                result = poppy.value_percentile(sequence, t)
                rt_target = numpy.percentile(sequence, result)
                if result == 0.0:
                    self.assertTrue(t <= rt_target)
                elif result == 100.0:
                    self.assertTrue(t >= rt_target)
                else:
                    self.assertAlmostEqual(rt_target, t, places=6)


if __name__ == '__main__':
    unittest.main()
