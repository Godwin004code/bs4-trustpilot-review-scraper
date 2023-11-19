import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML: {e}")
        return None

def scrape_reviews(html):
    if html is None:
        return None

    soup = BeautifulSoup(html, 'html.parser')

    revs = soup.find_all('p', class_="typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn")
    
    reviews = [rev.get_text(strip=True) for rev in revs]
    print(reviews)
    save_to_excel(reviews=reviews)
    

def save_to_excel(reviews, output_file='airbnbreview.xlsx'):
    df = pd.DataFrame({'Reviews': reviews})
    df.to_excel(output_file, index=False)
    print(f"Reviews saved to {output_file}")
    

def main():
    url = 'https://www.trustpilot.com/review/www.airbnb.com'
    html = get_html(url)
   

    if html:
        scrape_reviews(html)
        

if __name__ == "__main__":
    main()
