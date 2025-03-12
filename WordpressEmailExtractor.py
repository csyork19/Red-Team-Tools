import requests
import re
from urllib.parse import urlparse


def get_html(url):
    """Fetch HTML content from a given URL."""
    headers = {'User-Agent': 'Mozilla/5.0'}  # To mimic a real browser request
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text


def extract_emails(html):
    """Extract email addresses from the given HTML content."""
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com')
    return set(email_pattern.findall(html))  # Use a set to remove duplicates


def process_urls(urls):
    """Process a list of URLs and return a dictionary of emails found per URL."""
    results = {}
    for url in urls:
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = "https://" + url  # Ensure URL has a scheme

        try:
            html = get_html(url)
            emails = extract_emails(html)
            results[url] = list(emails)
        except requests.RequestException as e:
            results[url] = f"Error: {e}"
    return results


def main():
    urls = [
        "https://camp.nc/tenant/armada-skate-shop/",
        "https://charlotteareaparanormal.org",
        "https://digitalchores.co/charlotte-web-design/",
        "https://www.cityofbelmont.org",
        "https://bio-nomic.com/",
        "https://www.queencityanimalhospital.com/",
        "https://defensys.ai",
        "https://canvastattoos.com/",
        "https://www.thecultureshopclt.com",
        "https://charlottewebdesignstudio.com",
        "https://belovdigital.agency/wp-login.php?redirect_to=https%3A%2F%2Fbelovdigital.agency%2Fwp-admin%2F&reauth=1",
        "https://www.michellejonescreative.com/wordpress-website-portfolio",
        "https://lazaruscharlotte.com",
        "https://www.briscoweb.com/business-website-design/",
        "https://wpsupportcharlotte.com/wordpress-support-services/wordpress-developers-and-designers/",
        "https://www.andyre.com/fastest-growing-neighborhoods-charlotte",
        "https://charlotteunlimited.com/best-restaurants-in-noda-charlotte/",
        "https://charlottepoi.com/noda/",
        "https://thetouristchecklist.com/things-to-do-in-noda-nc/",
        "https://www.charlotteonthecheap.com/cat-cafes-charlotte/",
        "https://copperbuilders.com/noda-charlotte-neighborhood/",
        "https://secretcharlotte.co/best-noda-breweries-charlotte/",
        "https://livemusicclt.com/live-music-noda-north-davidson/",
        "https://uigus.com/blog/insurance-broker-leads-near-davidson-nc-ultimate-guide-to-growing-your-local-insurance-business-in-2024/",
        "https://www.davidsondavie.edu/small-business-center/starting-a-business-resources/",
        "https://www.lakenormanchamber.org",
        "https://newsofdavidson.org/local-businesses/",
        "https://business.daviechamber.com/list/member/ddcc-small-business-center-326",
        "https://davidsoncountyncalive.com/davidson-county-business-and-organization-directory",
        "https://lakenorman.com/davidson-a-small-town-on-lake-norman/",
        "https://lknconnectcommunity.com/home-services-flooring-burgess-supply-co-inc-huntersville/",
        "https://qcsignscharlotte.com/sign-shop-huntersville-nc/",
        "https://business.mooresvillenc.org/list",
        "https://businessnc.com/town-square-huntersville-is-a-quaint-suburban-charlotte-boomtown/",
        "https://www.vikingmergers.com/market/business-brokers-lake-norman-nc/",
        "https://brandtlawnc.com",
        "https://www.lakenormanpublications.com/front-page/",
        "https://www.offtheeatenpathblog.com/local-gift-guide/",
        "https://travelmustdos.com/must-do-places-to-visit-in-charlotte-nc/",
        "https://www.scoopcharlotte.com/2021/08/24/here-are-10-uptown-businesses-that-should-be-on-every-clt-womans-radar/",
        "https://southendclt.org/about/south-ends-story",
        "https://qcitymetro.com/2025/02/04/south-end-minority-owned-businesses/",
        "https://southendmkt.com",
        "https://www.roadtripsandcoffee.com/south-end-charlotte/",
        "https://plazamidwood.org/events/#!event/2024/5/3/home-and-garden-tour",
        "https://qcnerve.com/plaza-midwood-neighborhood-guide/",
        "https://whatnowcharlotte.com/2025/02/18/bartaco-expected-to-join-commonwealth-development-in-plaza-midwood/",
        "https://styleblueprint.com/charlotte/everyday/insiders-guide-navigating-plaza-midwood/",
        "https://downtownbelmont.org/shop/",
        "https://advancedmovingnc.com",
        "https://charlottequiltersguild.org/member-businesses/",
        "https://www.gastonbusiness.com",
        "https://apluslawnandlandscapinginc.com",
        "https://carolinasignsnc.com",
        "https://raleigh.teddslist.com"
    ]

    results = process_urls(urls)

    for url, emails in results.items():
        print(f"\nURL: {url}")
        if isinstance(emails, list) and emails:
            print("Emails found:")
            for email in emails:
                print(email)
        else:
            print("No email addresses found or error occurred.")


if __name__ == "__main__":
    main()
