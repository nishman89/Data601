from parametrize import parametrize

from main.tdd import fizz_buzz

@parametrize("n,expected",[(1,"1"), (2,"2"), (4,"4")])
def test_given_a_number_return_its_string(n,expected):
    assert fizz_buzz(n)  == expected