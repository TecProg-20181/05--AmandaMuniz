import unittest
from diskspace import *

class DiskspaceTest(unittest.TestCase):

    def test_bytes_to_readable(self):
        blocks = 224
        result = "112.00Kb"
        command = bytes_to_readable(blocks)
        self.assertEqual(command, result)

    def test_subprocess_check_output(self):
        command = 'du'
        firstResult = subprocess.check_output(command.strip().split(' '))
        finalResult = subprocess_check_output(command)
        self.assertEqual(firstResult, finalResult)

if __name__ == '__main__':
    unittest.main()
