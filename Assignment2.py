import re
import requests

def extract_website_details(url):
    try:
        response = requests.get(url)
        content = response.text
        
        # Extract social links
        social_links = re.findall(r'https?://(?:www\.)?(?:facebook\.com|linkedin\.com)/[^\s/$.?#].[^\s]*', content)
        
        # Extract email addresses
        email_addresses = re.findall(r'\S+@\S+', content)
        
        # Extract contact details
        contact_numbers = re.findall(r'(?:(?:\+\d{1,3}\s?)?\(?\d{1,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}', content)
        
        return social_links, email_addresses, contact_numbers
    except Exception as e:
        print("An error occurred:", e)
        return [], [], [] #if error occured return empty list

# User input for the website URL
website_url = input("Enter the website URL: ")

social_links, email_addresses, contact_numbers = extract_website_details(website_url)

print("Social links -")
for link in social_links:
    print(link)

print("\nEmail addresses:")
for email in email_addresses:
    print(email)

print("\nContact:")
for contact in contact_numbers:
    print(contact)
