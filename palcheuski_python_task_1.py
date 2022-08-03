from re import match


def data_validation(data: str) -> bool:
    """
    Checking if a number is valid.
    :param data: str
    :return: bool
    """
    if match(r"^0$|^-?0\.\d+$|^-?[1-9]\d*(\.\d+)?$", data):
        return True
    else:
        return False


def data_conversion(data: str) -> float:
    """
    Convert data to float().
    :param data: str
    :return: float
    """
    try:
        converted_number = float(data)
    except ValueError:
        print("Error converting data to float().")
    else:
        return converted_number


def print_hello(number: float) -> None:
    """
    If the number is greater than 7, then print "Привет".
    :param number: float
    :return: None
    """
    if number > 7:
        print("Привет")


def main() -> None:
    entered_data = input("Enter the number:\n")
    if data_validation(entered_data):
        result_data_conversion = data_conversion(entered_data)
        print_hello(result_data_conversion)
    else:
        print("You entered an invalid number.")


if __name__ == '__main__':
    print("Palcheuski _ Python 3.10 _ Task 1")
    while True:
        main()
