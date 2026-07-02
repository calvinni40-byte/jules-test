import unittest
from hello import hello_world

class TestHello(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world("Jules"), "Hello, Jules!")
        self.assertEqual(hello_world("Alice"), "Hello, Alice!")
        self.assertEqual(hello_world(""), "Hello, !")

if __name__ == "__main__":
    unittest.main()
