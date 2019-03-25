from unittest import TestCase

from hello.say_hello import say_hello


class SayHelloTest(TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("tim"), "hello tim")

