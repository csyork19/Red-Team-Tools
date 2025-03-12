from duckduckgo_search import DDGS
import requests


def find_wp_content_urls(query, num_results=500, search_limit=500):
    wp_urls = set()  # Use a set to avoid duplicates

    # Perform DuckDuckGo search
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=search_limit)

    for result in results:
        url = result["href"]
        if url in wp_urls:  # Skip duplicates
            continue

        try:
            # Fetch HTML content
            response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})

            if response.status_code == 200 and "wp-content" in response.text:
                wp_urls.add(url)

            # Stop when we reach the desired number of results
            if len(wp_urls) >= num_results:
                break

        except requests.exceptions.RequestException:
            continue  # Skip any URLs that cause errors

    return list(wp_urls)  # Convert back to a list for final output


# Search for local businesses in Charlotte
query = "Noda Charlotte NC local businesses"
query2 = "Davidson NC local businesses"
query3 = "Huntersville  NC local businesses"
query4 = "Uptown Charlotte NC local businesses"
query5 = "South End Charlotte NC local businesses"
query6 = "Plaza Midwood Charlotte NC local businesses"
query7 = "Belmont Charlotte NC local businesses"
query8 = "Gastonia Charlotte NC local businesses"



wordpress_urls = find_wp_content_urls(query, num_results=500, search_limit=500)
wordpress_urls2 = find_wp_content_urls(query2, num_results=500, search_limit=500)
wordpress_urls3 = find_wp_content_urls(query3, num_results=500, search_limit=500)
wordpress_urls4 = find_wp_content_urls(query4, num_results=500, search_limit=500)
wordpress_urls5 = find_wp_content_urls(query5, num_results=500, search_limit=500)
wordpress_urls6 = find_wp_content_urls(query6, num_results=500, search_limit=500)
wordpress_urls7 = find_wp_content_urls(query7, num_results=500, search_limit=500)
wordpress_urls8 = find_wp_content_urls(query8, num_results=500, search_limit=500)



# Output the found URLs
print("Noda WordPress-based local business URLs: \n", wordpress_urls)
print("Davidson WordPress-based local business URLs: \n", wordpress_urls2)
print("Huntersville WordPress-based local business URLs: \n", wordpress_urls3)
print("Uptown WordPress-based local business URLs: \n", wordpress_urls4)
print("Southend WordPress-based local business URLs:", wordpress_urls5)
print("Plaza Midwood WordPress-based local business URLs:", wordpress_urls6)
print("belmont WordPress-based local business URLs:", wordpress_urls7)
print("gastonia WordPress-based local business URLs:", wordpress_urls8)

