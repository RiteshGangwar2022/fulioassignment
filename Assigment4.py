import re
from bs4 import BeautifulSoup
import requests

# sample web technologies regx that want to detect in webiste
technologies_to_detect = {
    "jQuery": re.compile(r'jQuery', re.I),
    "React.js": re.compile(r'\bReact\.js\b', re.I),
    "WooCommerce": re.compile(r'WooCommerce', re.I),
    "Bootstrap": re.compile(r'\bBootstrap\b', re.I),
    "Shopify": re.compile(r'Shopify', re.I),
    "Next.js": re.compile(r'\bNext\.js\b', re.I),
    "Materialize CSS": re.compile(r'\bMaterialize\sCSS\b', re.I),
    "PHP": re.compile(r'\bPHP\b', re.I),
    "Python": re.compile(r'\bPython\b', re.I),
    "Google Maps": re.compile(r'Google\sMaps', re.I),
}


# Define the URL of the website we want to analyze
url=input("enter webiste url \n")
website_url =str(url)

# Fetch the website's source code
response = requests.get(website_url)
#print(response)
html_content = response.content
#print(html_content)



# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
#print(soup.prettify)

# Function to detect technologies in the source code
def detect(soup, technologies):
    detected= [] #list will contain all the technologies used to built website

    # Search for each technology in the parsed HTML
    for technology, pattern in technologies.items():
        if soup.find(string=pattern):
            detected.append(technology)

    return detected #returning list of technolgies after detection


#calling function to detect
detected_technologies = detect(soup, technologies_to_detect)



#pinting based on response got after detection
if detected_technologies:
    print("Detected technologies:")
    for tech in detected_technologies:
        print(tech)
else:
    print("No technologies detected.")

