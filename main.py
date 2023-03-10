from random import randint


def app():
    user_choice = int(input("Choose number."))
    pc_choice = randint(1, 50)

    if user_choice == pc_choice:
        print("승")
    elif user_choice > pc_choice:
        print("아래", pc_choice)
    elif user_choice < pc_choice:
        print("위", pc_choice)


if __name__ == '__main__':
    app()
