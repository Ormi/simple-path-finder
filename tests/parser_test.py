import unittest
import sys
sys.path.insert(1, '../src')
from parser import array

class TestStringMethods(unittest.TestCase):

    def test_payload(self):
        self.assertEqual(array, [['Estate', 'House', 'Basement', 'Kitchen', 'knife'], ['Estate', 'House', 'Basement', 'Stairs', 'Bedroom', 'pillow'], ['Estate', 'House', 'Hallway', 'keys'], ['Estate', 'Garden', 'Toolshed', 'knife']])

if __name__ == '__main__':
    unittest.main()