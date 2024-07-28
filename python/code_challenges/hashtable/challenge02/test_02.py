# test_repeated_word.py
import pytest
from challenge02 import first_repeated_word

def test_single_repetition():
    input_str = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    assert first_repeated_word(input_str) == "ASAC"

def test_no_repetition():
    input_str = "I am learning programming at ASAC."
    assert first_repeated_word(input_str) == "No Repetition"

def test_multiple_repetitions():
    input_str = "The cat jumped over the dog. The dog barked at the cat."
    assert first_repeated_word(input_str) == "The"

def test_case_insensitivity():
    input_str = "This is a test. This is only a Test."
    assert first_repeated_word(input_str) == "This"

def test_repetition_with_punctuation():
    input_str = "Hello, world! Hello again, world!"
    assert first_repeated_word(input_str) == "world!"

def test_no_words():
    input_str = ""
    assert first_repeated_word(input_str) == "No Repetition"

def test_single_word():
    input_str = "Hello"
    assert first_repeated_word(input_str) == "No Repetition"

def test_special_characters():
    input_str = "@home is where @heart is."
    assert first_repeated_word(input_str) == "No Repetition"

def test_numerical_input():
    input_str = "123 456 123 789"
    assert first_repeated_word(input_str) == "123"

def test_large_input():
    input_str = "a " * 10000 + "b " + "a"
    assert first_repeated_word(input_str) == "a"

def test_large_input_no_repetition():
    input_str = " ".join(str(i) for i in range(100000))
    assert first_repeated_word(input_str) == "No Repetition"


if __name__ == "__main__":
    pytest.main()# Write your test here