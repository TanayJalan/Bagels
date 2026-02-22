import unittest
import bagels

class TestBagels(unittest.TestCase):
    def test_getClues_duplicates(self):
        # Secret is '123'
        secret = '123'

        # Case 1: Guess '112'
        # Fermi: 1 (pos 0)
        # Pico: 2 (pos 2 matches secret pos 1)
        # Second 1 (pos 1) should NOT be Pico because secret[0] is already matched.
        # Expected: "Fermi Pico"
        # Current (Buggy): "Fermi Pico Pico"
        clues = bagels.getClues('112', secret)
        self.assertEqual(clues, 'Fermi Pico', f"Failed for guess '112' and secret '{secret}'")

    def test_getClues_all_duplicates(self):
        # Secret '123'
        secret = '123'

        # Case 2: Guess '111'
        # Fermi: 1 (pos 0)
        # Other 1s should not be Pico.
        # Expected: "Fermi"
        # Current (Buggy): "Fermi Pico Pico"
        clues = bagels.getClues('111', secret)
        self.assertEqual(clues, 'Fermi', f"Failed for guess '111' and secret '{secret}'")

    def test_getClues_standard(self):
        secret = '123'
        # Standard cases
        self.assertEqual(bagels.getClues('123', secret), 'You got it!')
        self.assertEqual(bagels.getClues('321', secret), 'Fermi Pico Pico') # 2 is Fermi, 1 and 3 are Picos
        self.assertEqual(bagels.getClues('456', secret), 'Bagels')

if __name__ == '__main__':
    unittest.main()
