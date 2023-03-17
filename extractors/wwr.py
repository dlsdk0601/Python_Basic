from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    res = get(f"{base_url}{keyword}")

    if res.status_code != 200:
        print("Can not request website")
    else:
        results = []
        print("res")
        soup = BeautifulSoup(res.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        for section in jobs:
            job_posts = section.find_all("li")
            job_posts.pop(-1)  # view_all 태그 지우기
            for post in job_posts:
                anchors = post.find_all("a")
                anchor = anchors[1]
                link = anchor["href"]
                company, kind, region = anchor.find_all("span", class_="company")
                title = anchor.find("span", class_="title")
                job_date = {
                    'company': company.string,
                    'region': region.string,
                    'position': title.string
                }
                results.append(job_date)

        return results

