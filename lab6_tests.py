import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    import unittest

    class TestSelectionSortBooks(unittest.TestCase):
        def test_empty_list(self):
            books = []
            selection_sort_books(books)
            self.assertEqual(books, [])

        def test_sort_books_by_title(self):
            books = [
                Book(["Author A"], "Zoo"),
                Book(["Author B"], "Apple"),
                Book(["Author C"], "Lemon")
            ]
            selection_sort_books(books)
            expected = [
                Book(["Author B"], "Apple"),
                Book(["Author C"], "Lemon"),
                Book(["Author A"], "Zoo")
            ]
            self.assertEqual(books, expected)

    if __name__ == '__main__':
        unittest.main()

    # Part 2
    import unittest

    class TestSwapCase(unittest.TestCase):
        def test_mixed_case_string(self):
            self.assertEqual(swap_case("Hello World!"), "hELLO wORLD!")

        def test_non_english_letters(self):
            self.assertEqual(swap_case("Ærø Island"), "æRØ iSLAND")

        def test_numbers_and_symbols(self):
            self.assertEqual(swap_case("123 ABC def!"), "123 abc DEF!")

        def test_empty_string(self):
            self.assertEqual(swap_case(""), "")

    if __name__ == '__main__':
        unittest.main()

    # Part 3
    import unittest

    class TestStrTranslate(unittest.TestCase):
        def test_replacement(self):
            self.assertEqual(str_translate('abcdcba', 'a', 'x'), 'xbcdcbx')

        def test_no_replacement_needed(self):
            self.assertEqual(str_translate('hello', 'z', 'y'), 'hello')

        def test_multiple_replacements(self):
            self.assertEqual(str_translate('mississippi', 'i', 'o'), 'mossossoppo')

        def test_empty_string(self):
            self.assertEqual(str_translate('', 'a', 'b'), '')

    if __name__ == '__main__':
        unittest.main()

    # Part 4
import unittest

class TestHistogram(unittest.TestCase):
    def test_basic_count(self):
        self.assertEqual(histogram("apple banana apple"), {'apple': 2, 'banana': 1})

    def test_empty_string(self):
        self.assertEqual(histogram(""), {})

    def test_multiple_words(self):
        self.assertEqual(histogram("cat dog cat dog bird"), {'cat': 2, 'dog': 2, 'bird': 1})

    def test_single_word(self):
        self.assertEqual(histogram("test"), {'test': 1})


if __name__ == '__main__':
    unittest.main()




if __name__ == '__main__':
    unittest.main()
