def main() -> None:
    """
    Program Entry Point.
    :return: None
    """
    entered_data = input("Enter name:\n")
    if entered_data == "Вячеслав":
        print("Привет, Вячеслав")
    else:
        print("Нет такого имени")


if __name__ == '__main__':
    print("Palcheuski _ Python 3.10 _ Task 2")
    while True:
        main()
