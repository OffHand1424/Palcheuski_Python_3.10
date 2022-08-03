from re import match


def collect_arr(arr: str) -> list:
    """
    Assembling an array from incoming data.
    :param arr: str
    :return: list
    """
    arr = arr.split(" ")
    return arr


def conversion_arr(convert_arr: list) -> list:
    """
    Converting the elements of the input array to float().
    :param convert_arr: list
    :return: list
    """
    new_arr = []
    for data_arr in convert_arr:
        if match(r"^0$|^-?0\.\d+$|^-?[1-9]\d*(\.\d+)?$", data_arr):
            try:
                data_arr = float(data_arr)
            except TypeError:
                print(f"Value {data_arr} is not number.")
            except ValueError:
                print(f"Can't convert {data_arr} to float.")
            else:
                new_arr.append(data_arr)
        else:
            print(f"{data_arr} not a number")
    return new_arr


def search_for_multiples_of_three(arr: list) -> list:
    """
    Finding multiples of three.
    :param arr: list
    :return: list
    """
    arr = [data_arr for data_arr in arr if data_arr % 3 == 0]
    return arr


def main() -> list:
    """
    Program Entry Point.
    :return: list
    """
    entered_arr = input(f"Enter an array delimited by ' ':\n")
    result_collect_arr = collect_arr(entered_arr)
    result_conversion_arr = conversion_arr(result_collect_arr)
    result_search_for_multiples_of_three = search_for_multiples_of_three(result_conversion_arr)
    return result_search_for_multiples_of_three


if __name__ == '__main__':
    print("Palcheuski _ Python 3.10 _ Task 3")
    while True:
        result = main()
        print(result)
