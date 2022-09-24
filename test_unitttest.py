import unittest
from unittest.mock import patch
from parameterized import parameterized
# import os
# import sys
# from io import StringIO
from app import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, add_new_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, show_document_info,  add_new_doc, secretary_program_start
import unittest.mock


# print(check_document_existance('11-2'))
# print(get_doc_owner_name())
# print(get_all_doc_owners_names())
# print(delete_doc())
# print(add_new_shelf(1))
# print(get_doc_shelf())
# print(add_new_doc())
# print(secretary_program_start())


class TestFunction(unittest.TestCase):
    # def setUp(self) -> None:
    #     print('Setup ===>')
    #
    #
    # def tearDown(self) -> None:
    #     print('tearDown ===>')
    # @parameterized.expand(
    #     [
    #         (True, '11-2'),
    #         (True, '2207 876234'),
    #         (True, '10006'),
    #     ]
    # )
    # def test_check_document_existance(self, etalon, arg):
    #     result = check_document_existance(arg)
    #     self.assertEqual(etalon, result)
    # @parameterized.expand(
    #     [
    #         ('11-2', 'Геннадий Покемонов'),
    #         ('2207 876234', 'Василий Гупкин'),
    #         ('10006', 'Аристарх Павлов'),
    #     ]
    # )
    # def test_input(self, num_doc, etalon):
    #     with unittest.mock.patch('builtins.input', return_value=num_doc):
    #         assert input() == num_doc
    #         result = get_doc_owner_name()
    #         self.assertEqual(etalon, result)

    # @parameterized.expand(
    #     [
    #         ('', {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'}),
    #         ('', {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'}),
    #         ('', {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'}),
    #     ]
    # )
    # def test_get_all_doc_owners_names(self, a, etalon):
    #     with unittest.mock.patch('builtins.input', return_value=a):
    #         assert input() == a
    #         result = get_all_doc_owners_names()
    #         self.assertEqual(etalon, result)
    #
    #
    # def test_remove_doc_from_shelf(self):
    # @parameterized.expand(
    #     [
    #         ('1', ('1', False)),
    #         ('2', ('2', False)),
    #         ('3', ('3', False)),
    #         ('4', ('4', True)),
    #     ]
    # )
    # def test_add_new_shelf(self, num_shelf, etalon):
    #     with unittest.mock.patch('builtins.input', return_value=num_shelf):
    #         assert input() == num_shelf
    #         result = add_new_shelf()
    #         self.assertEqual(etalon, result)
    # @parameterized.expand(
    #     [
    #         ('11-2', ('11-2', True)),
    #         ('2207 876234',('2207 876234', True)),
    #         ('10006',('10006', True)),
    #     ]
    # )
    # def test_delete_doc(self, num_doc, etalon):
    #     with unittest.mock.patch('builtins.input', return_value=num_doc):
    #         assert input() == num_doc
    #         result = delete_doc()
    #         self.assertEqual(etalon, result)
    #
    # @parameterized.expand(
    #     [
    #         ('11-2', '1'),
    #         ('2207 876234','1'),
    #         ('10006', '2'),
    #     ]
    # )
    # def test_get_doc_shelf(self, num_doc, etalon):
    #     with unittest.mock.patch('builtins.input', return_value=num_doc):
    #         assert input() == num_doc
    #         result = get_doc_shelf()
    #         self.assertEqual(etalon, result)
    @parameterized.expand(
        [
            (('11-2', '1'),('11-2', '1')),
            (('2207 876234','1'), ('2207 876234','1')),
            (('10006', '2'), ('10006', '2')),
        ]
    )
    def test_move_doc_to_shelf(self, doc_num, etalon):
        with unittest.mock.patch('builtins.input', return_value=doc_num):
            assert input() == doc_num
        # with unittest.mock.patch('builtins.input', return_value=shelf_num):
        #     assert input() == shelf_num
            result = move_doc_to_shelf()
            self.assertEqual(etalon, result)
    #
    # @parameterized.expand(
    #     [
    #         ('11-2', ('invoice', '11-2', 'Геннадий Покемонов')),
    #         ('2207 876234',('passport', '2207 876234', 'Василий Гупкин')),
    #         ('10006', ('insurance', '10006', 'Аристарх Павлов')),
    #     ]
    # )
    # def test_show_document_info(self,doc_num, etalon):
    #     esult = show_document_info()
    #         self.assertEqual(etalon, result)



