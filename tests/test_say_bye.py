from unittest import TestCase

from hello.say_bye import say_bye


class SayByeTest(TestCase):
    def test_say_bye(self):
        self.assertEqual(say_bye("tim"), "bye tim")
