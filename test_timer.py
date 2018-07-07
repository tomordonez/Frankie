import unittest
import pomodoroTimer

class TestTimer(unittest.TestCase):
    
    def test_validate_int(self):
        length = pomodoroTimer.validate_int('Enter number: ')
        self.assertIsInstance(length, int)

if __name__ == '__main__':
    unittest.main()
