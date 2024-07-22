
import pytest
from challenge02 import Ch2

def test_first_repeated_word():
    # Test case 1: A sentence with a repeated word
    input_string1 = "The quick brown fox jumps over the lazy dog. The dog barked."
    assert Ch2.solution(input_string1) == "The"

    # Test case 2: A sentence with no repeated words
    input_string2 = "I am learning programming at ASAC."
    assert Ch2.solution(input_string2) == "No Repetition"

    # Test case 3: A sentence with multiple repeated words (first one should be returned)
    input_string3 = "Hello world! Hello everyone. Welcome to the world of programming."
    assert Ch2.solution(input_string3) == "Hello"

    # Test case 4: A sentence where the repeated word appears immediately after itself
    input_string4 = "Python Python is a popular programming language."
    assert Ch2.solution(input_string4) == "Python"

    # Test case 5: A sentence with punctuation (should handle words correctly)
    input_string5 = "Coding is fun. Yes, coding is very fun!"
    assert Ch2.solution(input_string5) == "is"

    # Test case 6: A sentence with repeated words having different cases
    input_string6 = "JavaScript is great. javascript is versatile."
    assert Ch2.solution(input_string6) == "is"

    # Test case 7: An empty string
    input_string7 = ""
    assert Ch2.solution(input_string7) == "No Repetition"

    # Test case 8: A sentence with special characters
    input_string8 = "Hello, world! Hello, everyone."
    assert Ch2.solution(input_string8) == "Hello,"

if __name__ == "__main__":
    pytest.main()