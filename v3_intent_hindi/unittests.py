#!/usr/bin/env python3
import unittest
from bot import *

class SetUp(unittest.TestCase):
    def setUp(self):
        self.bot = Bot()

class TestBot(SetUp):
    def test_response(self):
        self.assertTrue(self.bot.reply('Hello') in ['हाय मानव', 'नमस्ते मानव'])

    def test_translation(self):
        self.assertEqual(self.bot._translate('Test'), 'परीक्षा')

if __name__ == '__main__':
    unittest.main()
