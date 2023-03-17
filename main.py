from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from extractors.wwr import extract_wwr_jobs

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

def app():
    jobs = extract_wwr_jobs("python")
    base_url = "https://kr.indeed.com/jobs?q="
    keyword = "python"

    response = browser.get(f"{base_url}{keyword}")

    if response.status_code != 200:
        print("bad")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        job_list = soup.find("ul", clss_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)
        for job in jobs:
            print(job)
        print("good")


if __name__ == '__main__':
    app()
