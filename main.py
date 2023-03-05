def app():
    def say_hello(user_name="default"):
        print("hello", user_name)

    say_hello("hello")
    say_hello()

    def plus(a=0, b=0):
        print(a+b)

    plus()


if __name__ == '__main__':
    app()
