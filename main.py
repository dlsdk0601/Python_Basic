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
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        job_list = soup.find("ul", clss_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone is None:
                anchor = job.select("h2 a")
                title = anchor["aria-label"]
                link = anchor["href"]
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link': f"https://kr.indeed.com/{link}",
                    'company': company.string,
                    'location': location.string,
                    'position': title,
                }
                results.append(job_data)
        for result in results:
            print(result, "\n/////\n")


if __name__ == '__main__':
    app()
