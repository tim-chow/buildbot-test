from unittest import TestCase

from hello.say_word import say_word

class SayWordTest(TestCase):
    def test_say_word(self):
        self.assertEqual(say_word("tim"), "word: tim")
