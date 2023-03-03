def app():
    def say_hello(user_name, user_age):
        print(f"Hello, {user_name} how r u? your age is {user_age}")
        print("Hello", user_name, "how r u? your age is", user_age)

    say_hello("ina", 30)
    say_hello(user_name="ina", user_age=20)


if __name__ == '__main__':
    app()
