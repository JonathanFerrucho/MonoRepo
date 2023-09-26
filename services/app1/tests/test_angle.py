from unittest import TestCase
import angle


class AngleTest(TestCase):

    def test_twelve(self):
        self.assertEqual(angle.between(12, 00), 0)
        self.assertEqual(angle.between(1, 00), 30)
        self.assertEqual(angle.between(1, 1), 24.5)
