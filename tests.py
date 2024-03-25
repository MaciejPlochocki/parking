import unittest
from oplaty import oblicz_oplate

class TestOplaty(unittest.TestCase):

    def test_oblicz_oplate(self):
        # Testuj, czy funkcja oblicza opłatę poprawnie
        self.assertEqual(oblicz_oplate("12:00", "13:00", 2), 2)
        self.assertEqual(oblicz_oplate("12:00", "14:00", 2), 4)
        self.assertEqual(oblicz_oplate("12:00", "12:30", 2), 0)

if __name__ == '__main__':
    unittest.main()
