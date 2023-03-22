from bs4 import BeautifulSoup
from requests import get


def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="

    response = get(f"{base_url}{keyword}")

    if response.status_code != 200:
        return 0
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        pagination = soup.find("ul", class_="pagination-list")
        if pagination is None:
            return 1
        else:
            pages = pagination.find_all("li", recursive=False)
            count = len(pages)
            if count >= 5:
                return 5
            else:
                return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs?q="
        response = get(f"{base_url}{keyword}&start={page*10}")

        if response.status_code != 200:
            print("bad")
        else:
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
                        'company': company.string.replace(",", " "),
                        'location': location.string.replace(",", " "),
                        'position': title.replace(",", " "),
                    }
                    results.append(job_data)
            for result in results:
                print(result, "\n/////\n")
    return results