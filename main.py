from requests import get

def app():
    websites = (
        "google.com",
        "https://airbnb.com",
        "twitter.com",
        "facebook.com"
    )

    for website in websites:
        if not website.startswith("https://"):
            print("fixed")
            website = f'https://{website}'



if __name__ == '__main__':
    app()
