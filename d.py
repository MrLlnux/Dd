import requests
from urllib.parse import urlparse
import threading

def check_site_status(url):
    if not urlparse(url).scheme:
        url = 'https://' + url

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successful - Status Code 200")
        elif response.status_code == 404:
            print("Not Found - Status Code 404")
        else:
            print(f"Unexpected Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def check_sites_concurrently(site, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=check_site_status, args=(site,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    site = input("Enter the site URL:\n==> ")
    num_threads = int(input("Enter the number of threads to use:\n==> "))
    check_sites_concurrently(site, num_threads)
