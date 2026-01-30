import unittest
from main import ProblemSolver

class TestProblemSolver(unittest.TestCase):
    def setUp(self):
        self.solver = ProblemSolver()

    def test_sum_even_numbers(self):
        self.assertEqual(self.solver.sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)
        self.assertEqual(self.solver.sum_even_numbers([]), 0)
        self.assertEqual(self.solver.sum_even_numbers([1, 3, 5]), 0)
        self.assertEqual(self.solver.sum_even_numbers([-2, -4, 3, 6]), 6)

    def test_count_vowels(self):
        self.assertEqual(self.solver.count_vowels("Hello World"), 3)
        self.assertEqual(self.solver.count_vowels("AEIOU"), 5)
        self.assertEqual(self.solver.count_vowels("xyz"), 0)
        self.assertEqual(self.solver.count_vowels(""), 0)

    def test_reverse_string(self):
        self.assertEqual(self.solver.reverse_string("hello"), "olleh")
        self.assertEqual(self.solver.reverse_string("Python"), "nohtyP")
        self.assertEqual(self.solver.reverse_string(""), "")
        self.assertEqual(self.solver.reverse_string("a"), "a")

    def test_is_positive(self):
        self.assertTrue(self.solver.is_positive(5))
        self.assertFalse(self.solver.is_positive(0))
        self.assertFalse(self.solver.is_positive(-3))
        self.assertTrue(self.solver.is_positive(1))

    def test_find_max(self):
        self.assertEqual(self.solver.find_max([1, 5, 3, 9, 2]), 9)
        self.assertEqual(self.solver.find_max([1]), 1)
        self.assertIsNone(self.solver.find_max([]))
        self.assertEqual(self.solver.find_max([-1, -5, -2]), -1)

    def test_count_occurrences(self):
        self.assertEqual(self.solver.count_occurrences("banana", "a"), 3)
        self.assertEqual(self.solver.count_occurrences("hello", "l"), 2)
        self.assertEqual(self.solver.count_occurrences("test", "z"), 0)
        self.assertEqual(self.solver.count_occurrences("", "a"), 0)


    def test_longest_word(self):
        self.assertEqual(self.solver.longest_word("The quick brown fox jumps."), "jumps")
        self.assertEqual(self.solver.longest_word(""), "")
        self.assertEqual(self.solver.longest_word("Hello, world!!"), "world")
        self.assertEqual(self.solver.longest_word("cat dog fox"), "fox")

    def test_is_palindrome(self):
        self.assertTrue(self.solver.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.solver.is_palindrome("race a car"))
        self.assertTrue(self.solver.is_palindrome(""))
        self.assertTrue(self.solver.is_palindrome("a"))

    def test_remove_duplicates(self):
        self.assertEqual(self.solver.remove_duplicates([1, 2, 2, 3, 1, 4]), [1, 2, 3, 4])
        self.assertEqual(self.solver.remove_duplicates([]), [])
        self.assertEqual(self.solver.remove_duplicates([1, 1, 1]), [1])
        self.assertEqual(self.solver.remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_factorial(self):
        self.assertEqual(self.solver.factorial(5), 120)
        self.assertEqual(self.solver.factorial(0), 1)
        self.assertEqual(self.solver.factorial(1), 1)
        with self.assertRaises(ValueError):
            self.solver.factorial(-1)

    def test_capitalize_words(self):
        self.assertEqual(self.solver.capitalize_words("hello world"), "Hello World")
        self.assertEqual(self.solver.capitalize_words("the quick fox"), "The Quick Fox")
        self.assertEqual(self.solver.capitalize_words(""), "")
        self.assertEqual(self.solver.capitalize_words("a"), "A")

    def test_sum_of_squares(self):
        self.assertEqual(self.solver.sum_of_squares([1, 2, 3]), 14)
        self.assertEqual(self.solver.sum_of_squares([]), 0)
        self.assertEqual(self.solver.sum_of_squares([2]), 4)
        self.assertEqual(self.solver.sum_of_squares([-2, 3]), 13)


    def test_find_pairs_with_sum(self):
        self.assertEqual(self.solver.find_pairs_with_sum([2, 7, 11, 15], 9), [(0, 1)])
        self.assertEqual(self.solver.find_pairs_with_sum([1, 2, 3], 10), [])
        result = self.solver.find_pairs_with_sum([1, 4, 3, 2, 5], 7)
        self.assertEqual(len(result), 2)
        flat_indices = [i for pair in result for i in pair]
        self.assertEqual(len(set(flat_indices)), 4)
        nums = [1, 4, 3, 2, 5]
        for i, j in result:
            self.assertEqual(nums[i] + nums[j], 7)
        self.assertEqual(self.solver.find_pairs_with_sum([], 5), [])

    # def test_max_subarray_sum(self):
    #     self.assertEqual(self.solver.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
    #     self.assertEqual(self.solver.max_subarray_sum([1]), 1)
    #     self.assertEqual(self.solver.max_subarray_sum([-1, -2, -3]), -1)
    #     self.assertEqual(self.solver.max_subarray_sum([]), 0)

    # def test_rotate_list(self):
    #     self.assertEqual(self.solver.rotate_list([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
    #     self.assertEqual(self.solver.rotate_list([1, 2, 3], 0), [1, 2, 3])
    #     self.assertEqual(self.solver.rotate_list([1], 5), [1])
    #     self.assertEqual(self.solver.rotate_list([], 3), [])

    # def test_is_valid_parentheses(self):
    #     self.assertTrue(self.solver.is_valid_parentheses("({[]})"))
    #     self.assertFalse(self.solver.is_valid_parentheses("(]"))
    #     self.assertTrue(self.solver.is_valid_parentheses(""))
    #     self.assertFalse(self.solver.is_valid_parentheses("([)]"))

    def test_merge_sorted_lists(self):
        self.assertEqual(self.solver.merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.solver.merge_sorted_lists([], [1, 2]), [1, 2])
        self.assertEqual(self.solver.merge_sorted_lists([1], []), [1])
        self.assertEqual(self.solver.merge_sorted_lists([], []), [])

    # def test_fibonacci_up_to(self):
    #     self.assertEqual(self.solver.fibonacci_up_to(10), [0, 1, 1, 2, 3, 5, 8])
    #     self.assertEqual(self.solver.fibonacci_up_to(1), [0, 1, 1])
    #     self.assertEqual(self.solver.fibonacci_up_to(0), [0])
    #     self.assertEqual(self.solver.fibonacci_up_to(-1), [])

if __name__ == "__main__":
    unittest.main()