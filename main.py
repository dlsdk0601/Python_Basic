from requests import get

def app():
    websites = (
        "google.com",
        "https://airbnb.com",
        "twitter.com",
        "facebook.com"
    )

    results = {}

    for website in websites:
        if not website.startswith("https://"):
            print("fixed")
            website = f'https://{website}'

        res = get(website)
        print("res")
        print(res)
        print(res.status_code)
        if res.status_code == 200:
            print(f'{website} is Ok')
            results[website] = "OK"
        else:
            print(f'{website}is not Ok')
            results[website] = "FAIL"


if __name__ == '__main__':
    app()
