class ProblemSolver:
    # Basic Questions
    def sum_even_numbers(self, numbers):
        """
        Returns the sum of all even numbers in the input list.
        Args:
            numbers (list): List of integers
        Returns:
            int: Sum of even numbers
        Example:
            sum_even_numbers([1, 2, 3, 4, 5, 6]) -> 12 (2 + 4 + 6)
        """
        results = [num for num in numbers if num % 2 == 0 and num > 0]

        return sum(results)


    def count_vowels(self, text):
        """
        Counts the number of vowels (a, e, i, o, u) in the input string, case-insensitive.
        Args:
            text (str): Input string
        Returns:
            int: Number of vowels
        Example:
            count_vowels("Hello World") -> 3
        """
        vowels = "aeiouAEIOU"
        count = 0

        for char in text:
            if char in vowels:
                count += 1
        return count


    def reverse_string(self, text):
        """
        Reverses the input string.
        Args:
            text (str): Input string
        Returns:
            str: Reversed string
        Example:
            reverse_string("hello") -> "olleh"
        """
        return text[::-1]
    

    def is_positive(self, number):
        """
        Checks if the input number is positive.
        Args:
            number (int): Input number
        Returns:
            bool: True if positive, False otherwise
        Example:
            is_positive(5) -> True
        """
        return number > 0
    

    def find_max(self, numbers):
        """
        Returns the maximum number in the list.
        Args:
            numbers (list): List of integers
        Returns:
            int: Maximum number, or None if list is empty
        Example:
            find_max([1, 5, 3, 9, 2]) -> 9
        """
        if not numbers:
            return None
        return max(numbers)
    

    def count_occurrences(self, text, char):
        """
        Counts occurrences of a specific character in the string, case-sensitive.
        Args:
            text (str): Input string
            char (str): Single character to count
        Returns:
            int: Number of occurrences
        Example:
            count_occurrences("banana", "a") -> 3
        """
        count = 0

        for item in text:
            if item == char:
                count += 1
        return count

    # Intermediate Questions
    def longest_word(self, sentence):
        """
        Returns the longest word in the sentence. If multiple words have the same length,
        return the first one. Ignore punctuation.
        Args:
            sentence (str): Input sentence
        Returns:
            str: Longest word
        Example:
            longest_word("The quick brown fox jumps.") -> "quick"
        """
        
        if not sentence:
            return ""
        
        punctuation = "!@#$%^&*?><.,"
        
        sentence_list = "".join([char for char in sentence if char not in punctuation]).split()
        longest_word = 0
        idx = 0

        for index, item in enumerate(sentence_list):
            if item in punctuation:
                continue

            if len(item) >= longest_word:
                longest_word = len(item)
                idx = index
        return sentence_list[idx]



    def is_palindrome(self, text):
        """
        Checks if the input string is a palindrome, ignoring case, spaces, and punctuation.
        Args:
            text (str): Input string
        Returns:
            bool: True if palindrome, False otherwise
        Example:
            is_palindrome("A man, a plan, a canal: Panama") -> True
        """
        cleaned_text = ""

        for char in text.lower():
            if char.isalpha():
                cleaned_text += char
        
        return cleaned_text == cleaned_text[::-1]

    def remove_duplicates(self, numbers):
        """
        Returns a list with duplicates removed, preserving the original order.
        Args:
            numbers (list): List of integers
        Returns:
            list: List with duplicates removed
        Example:
            remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
        """
        result = []

        for num in numbers:
            if num in result:
                continue
            else:
                result.append(num)
        return result

    def factorial(self, n):
        """
        Calculates the factorial of a non-negative integer.
        Args:
            n (int): Non-negative integer
        Returns:
            int: Factorial of n
        Raises:
            ValueError: If n is negative
        Example:
            factorial(5) -> 120
        """
        if n < 0:
            raise ValueError

        factor = 1

        for i in range(1, n+1):
            factor *= i
        return factor

    def capitalize_words(self, sentence):
        """
        Capitalizes the first letter of each word in the sentence.
        Args:
            sentence (str): Input sentence
        Returns:
            str: Sentence with each word capitalized
        Example:
            capitalize_words("hello world") -> "Hello World"
        """
        return sentence.title()

    def sum_of_squares(self, numbers):
        """
        Returns the sum of squares of all numbers in the list.
        Args:
            numbers (list): List of integers
        Returns:
            int: Sum of squares
        Example:
            sum_of_squares([1, 2, 3]) -> 14 (1^2 + 2^2 + 3^2)
        """
        return sum(num**2 for num in numbers)

    # Advanced Questions
    def find_pairs_with_sum(self, numbers, target):
        """
        Returns a list of tuples, each containing indices of two numbers that sum to the target.
        Each number can only be used once.

        Hint:
            - You need to find all unique pairs of indices (i, j) such that numbers[i] + numbers[j] == target.
            - Make sure that each index is only used in one pair.
            - Consider how to avoid using the same element twice in different pairs.

        Args:
            numbers (list): List of integers
            target (int): Target sum
        Returns:
            list: List of tuples with indices of pairs summing to target
        Example:
            find_pairs_with_sum([2, 7, 11, 15], 9) -> [(0, 1)]
        """
        pass


    def max_subarray_sum(self, numbers):
        """
        Finds the maximum sum of a contiguous subarray.

        Hint:
            - Think about how you can keep track of the current sum and the maximum sum as you iterate through the list.
            - Consider what to do when the current sum becomes negative.

        Args:
            numbers (list): List of integers
        Returns:
            int: Maximum sum of any contiguous subarray
        Example:
            max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6
        """
        pass

    def rotate_list(self, numbers, k):
        """
        Rotates the list to the right by k steps. k can be larger than list length.

        Hint:
            - Think about how to handle cases where k is greater than the length of the list.
            - Consider how slicing can help you rearrange the list efficiently.

        Args:
            numbers (list): List of integers
            k (int): Number of steps to rotate
        Returns:
            list: Rotated list
        Example:
            rotate_list([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
        """
        pass

    def is_valid_parentheses(self, s):
        """
        Checks if a string of parentheses is valid (properly nested and closed).

        Hint:
            - Use a stack to keep track of opening brackets.
            - Make sure each closing bracket matches the most recent opening bracket.

        Args:
            s (str): String containing parentheses (), {}, []
        Returns:
            bool: True if valid, False otherwise
        Example:
            is_valid_parentheses("({[]})") -> True
        """
        pass

    def merge_sorted_lists(self, list1, list2):
        """
        Merges two sorted lists into a single sorted list.

        Hint:
            - Use two pointers to traverse both lists.
            - Compare elements at each pointer and add the smaller one to the result.

        Args:
            list1 (list): First sorted list of integers
            list2 (list): Second sorted list of integers
        Returns:
            list: Merged sorted list
        Example:
            merge_sorted_lists([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
        """
        pass

    def fibonacci_up_to(self, n):
        """
        Generates Fibonacci numbers up to n (inclusive).

        Hint:
            - Start with the first two Fibonacci numbers.
            - Continue generating the next number by summing the previous two until you reach or exceed n.

        Args:
            n (int): Upper bound
        Returns:
            list: Fibonacci numbers up to n
        Example:
            fibonacci_up_to(10) -> [0, 1, 1, 2, 3, 5, 8]
        """
        pass

    def merge_sorted_lists(self, list1, list2):
        """
        Merges two sorted lists into a single sorted list.

        Hint:
            - Use two pointers to traverse both lists.
            - Compare elements at each pointer and add the smaller one to the result.

        Args:
            list1 (list): First sorted list of integers
            list2 (list): Second sorted list of integers
        Returns:
            list: Merged sorted list
        Example:
            merge_sorted_lists([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
        """
        return sorted(list1 + list2)

    def fibonacci_up_to(self, n):
        """
        Generates Fibonacci numbers up to n (inclusive).

        Hint:
            - Start with the first two Fibonacci numbers.
            - Continue generating the next number by summing the previous two until you reach or exceed n.

        Args:
            n (int): Upper bound
        Returns:
            list: Fibonacci numbers up to n
        Example:
            fibonacci_up_to(10) -> [0, 1, 1, 2, 3, 5, 8]
        """
        pass

if __name__ == "__main__":
    pass