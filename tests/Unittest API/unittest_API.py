from parameterized import parameterized
import unittest
from HWtest import YaDisk, token
from config import password_1

ya = YaDisk(token)

class TestFunction(unittest.TestCase):
    def setUp(self) -> None:
        print('Setup ===>')


    def tearDown(self) -> None:
        print('tearDown ===>')

    @parameterized.expand(
        [
            ('200'),
            ('201'),
            ('409'),
        ]
    )
    def test_get_my_files_name(self, etalon):

        result = ya.get_my_files_name()
        self.assertEqual(etalon, result)

    def test_create_folder(self):
        etalon = '201'
        result = ya.create_folder(path='New_Folder')
        self.assertTrue(etalon, result)


if __name__ == "__main__":

    ya = YaDisk(token)
    unittest.main()






