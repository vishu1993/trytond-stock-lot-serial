# -*- coding: utf-8 -*-
"""
    __init__

    Test Suite

    :copyright: (c) 2013-2014 by Openlabs Technologies & Consulting (P) Limited
    :license: 3-clause BSD, see LICENSE for more details.
"""
import unittest
import trytond.tests.test_tryton
from test_shipment import TestShipmentIn
from test_views_depends import TestViewsDepends


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestShipmentIn),
        unittest.TestLoader().loadTestsFromTestCase(TestViewsDepends),
    ])
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
