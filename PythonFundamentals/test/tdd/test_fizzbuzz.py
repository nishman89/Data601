from parametrize import parametrize

from main.tdd import fizz_buzz

@parametrize("n,expected",[(1,"1"), (2,"2"), (4,"4")])
def test_given_a_number_return_its_string(n,expected):
    assert fizz_buzz(n)  == expected


@parametrize("n", [3, 6, 9, 12, 18])
def test_given_number_divisible_by_three_but_not_five_return_fizz(n):
    """Given a number divisible by 3 but not 5, return 'Fizz'."""
    assert fizz_buzz(n) == "Fizz"


def test_given_five_return_buzz():
    """Given 5, return 'Buzz'."""
    assert fizz_buzz(5) == "Buzz"


@parametrize("n", [5, 10, 20])
def test_given_number_divisible_by_five_but_not_three_return_buzz(n):
    """Given a number divisible by 5 but not 3, return 'Buzz'."""
    assert fizz_buzz(n) == "Buzz"


def test_given_fifteen_return_fizzbuzz():
    """Given 15, return 'FizzBuzz'."""
    assert fizz_buzz(15) == "FizzBuzz"


@parametrize("n", [15, 30, 45])
def test_given_number_divisible_by_fifteen_return_fizzbuzz(n):
    """Given a number divisible by 15, return 'FizzBuzz'."""
    assert fizz_buzz(n) == "FizzBuzz"