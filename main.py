import openai
from dotenv import load_dotenv
import sys
import urllib.request
from bs4 import BeautifulSoup

load_dotenv()

def get_ingredients():
    user_input = "Hamburger"

    response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[ 
                {"role": "system", "content": "Act as a master chef. You will be given the name of a dish and you are to identify the individual ingredients of each dish. Exclude salt and pepper. Return the ingredients in a list format"},
                {"role": "user", "content": f"Here is the name of the dish: {user_input}. Return ONLY the ingredients seperated by commas. No other text"} ]
            )

    print(response.choices[0].message.content)

def get_website_data(ingredient):
    ingredient = ingredient.replace(" ", "%20")

    url = f"https://www.shoprite.com/sm/pickup/rsid/3000/results?q={ingredient}"

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req) as response:
            html_content = response.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        data = [p.text.strip() for p in soup.find_all('p')]

        data = clean_data(data)
        print(data)
        return data
    except urllib.error.URLError as e:
        return f"Error fetching data: {e}"

def get_images_from_website(ingredient):
    ingredient = ingredient.replace(" ", "%20")

    url = f"https://www.shoprite.com/sm/pickup/rsid/3000/results?q={ingredient}"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req) as response:
            html_content = response.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        images = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]

        del images[:2]
        return images
    except urllib.error.URLError as e:
        return f"Error fetching data: {e}"

if __name__ == "__main__":
    #get_ingredients()
    get_website_data("hamburger buns")