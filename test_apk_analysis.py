import unittest
from apk_analysis.apk_parser import APKParser

class TestAPKParser(unittest.TestCase):
    def test_decompile_apk(self):
        apk_parser = APKParser("path/to/test.apk")
        apk_parser.decompile_apk("output")
        self.assertTrue(os.path.exists("output"))

if __name__ == "__main__":
    unittest.main()
