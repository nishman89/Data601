

def fizz_buzz(n):
    output = ""
    if n % 3 == 0:
        output = "Fizz"
    if n % 5 == 0:
        output += "Buzz"
    if output == "":
        output = str(n)
    return output

# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17
#  Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz