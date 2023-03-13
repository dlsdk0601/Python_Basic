from requests import get
from bs4 import BeautifulSoup


def app():
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    search_term = "python"
    res = get(f"{base_url}{search_term}")

    if res.status_code != 200:
        print("Can not request website")
    else:
        print("res")
        soup = BeautifulSoup(res.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        print(jobs)


if __name__ == '__main__':
    app()
