def app():
    age = int(input("how old r u?"))
    print(age)

    # typeof 함수
    print(type(age))

    if age > 18:
        print("어른")
    # elif age > 18 and age < 35:
    elif 18 < age < 35:
        print("애")
    elif age == 60 or age == 70:
        print("늙은이")


if __name__ == '__main__':
    app()
