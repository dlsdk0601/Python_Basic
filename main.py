from flask import Flask, render_template, request, redirect, send_file

from extractors.wwr import extract_wwr_jobs

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)


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
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs?q="

        response = get(f"{base_url}{keyword}")

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


def app():
    extract_indeed_jobs()


if __name__ == '__main__':
    app()
