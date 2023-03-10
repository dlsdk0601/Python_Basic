from random import randint


def app():
    pc_choice = randint(1, 50)
    playing = True

    while playing:
        user_choice = int(input("Choose number."))
        if user_choice == pc_choice:
            print("승")
            playing = False
        elif user_choice > pc_choice:
            print("아래")
        elif user_choice < pc_choice:
            print("위")


if __name__ == '__main__':
    app()
