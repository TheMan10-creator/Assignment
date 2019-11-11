import unittest
from tkinter import Tk
import Assignment

root2 = Tk()
a = Assignment.Student_info(root2)


class TestNewAlgorithm(unittest.TestCase):
    def test_sort(self):
        a.sortcombo.set('fname')
        array_test = [('Aashish', 'Lama', '9866950525', 'Hacking'),
                          ('Dipendra', 'Aryal', '9803635098', 'Security')]
        expected_result = [('Dipendra', 'Aryal', '9803635098', 'Security'),
                           ('Aashish', 'Lama', '9866950525', 'Hacking')]

        a.sortcombo.set('lname')
        ac_result=a.bubbleSort(array_test)
        self.assertEqual(expected_result,ac_result)


    def test_search(self):
        array_test = [('Aashish', 'Inaruwa', '9866950525', 'Hacking'),
                      ('Dipendra', 'Kathmandu', '9803635098', 'Security')]
        expected_result = [('Aashish', 'Inaruwa', '9866950525', 'Hacking')]
        a.searchentry.delete(0, 'end')
        a.searchentry.insert(0, 'Aashish')
        a.searchcombo.set('fname')
        ac_result = a.search(array_test)
        self.assertEqual(expected_result, ac_result)



if __name__ == '__main__':
    unittest.main()
