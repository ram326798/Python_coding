# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class InvalidNegativeInputError(Error):
    """Raised when the input value is too small"""
    pass


class InvalidInputTypeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number


# user guesses a number until he/she gets it right
while True :
    try:
        num = input("Enter a number: ")
        if ((num>='a' and num<='z') or (num>='A' and num<='Z') ))
            raise InvalidInputTypeError
        elif int(num) < 0:
            raise InvalidNegativeInputError
        break
    except InvalidInputTypeError:
        print("only Integers are allowed")
        print()
    except InvalidNegativeInputError:
        print("Enter a positive number")
        print()
print("entered integer value is : "+num)
