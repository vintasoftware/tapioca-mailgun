# coding: utf-8

import unittest

from tapioca_mailgun import Mailgun


class TestTapiocaMailgun(unittest.TestCase):

    def setUp(self):
        self.wrapper = Mailgun()


if __name__ == '__main__':
    unittest.main()
