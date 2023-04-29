# import libraries
from bs4 import BeautifulSoup
import requests
import time

def find_jobs(url):
    # Connect to TopCV Website and pull in data
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('div', class_ = 'body')

    #Loop through each job post and extract job title, salary, and location. If salary not "thỏa thuận", save the job details to a text file
    for job in jobs:
        salary = job.find('label', class_ = 'title-salary').text
        if "Thỏa thuận" not in salary:
            job_title = job.find('h3', class_ = 'title').text
            location = job.find('label', class_ = 'address').text
            with open(f'JobPost/JobPosts.txt', 'a', encoding='utf-8') as f:
                f.write(f"Job Title: {job_title.strip()} \n")
                f.write(f"Salary: {salary.strip()} \n")
                f.write(f"Location: {location} \n")
            print(f'File saved: JobPosts')

if __name__ == '__main__':
    # Define the base URL and the number of pages to scrape
    base_url = 'https://www.topcv.vn/tim-viec-lam-marketing?salary=0&exp=1&sort=up_top&exp_btw=0&salary_min=0&salary_max=0&page='
    num_pages = 20

    # Create a list of URLs to scrape by concatenating the base URL with each page number
    urls = [base_url + str(n) for n in range(1, num_pages + 1)]

    #Loop through each URL
    for url in urls:
        find_jobs(url)
        # Runs check_price after a set time
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

print("Done")
