import os

from prettytable import PrettyTable

from get_icons_champions import get_icons_champions
from get_splash_champions import get_splash_champions


def print_menu():
    table = PrettyTable()
    table.field_names = ["Option", "Action"]
    table.add_row(["1", "Получить все иконки чемпионов"])
    table.add_row(["2", "Получить все сплеши чемпионов"])
    table.add_row(["3", "Выйти"])
    print(table)


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            get_icons_champions()
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            get_splash_champions()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1 или 2.")


if __name__ == "__main__":
    main()
