import openai
from dotenv import load_dotenv
import sys
import urllib.request
from bs4 import BeautifulSoup
import re

load_dotenv()

def get_ingredients(user_input):

    response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[ 
                {"role": "system", "content": "Act as a master chef. You will be given the name of a dish and you are to identify the individual ingredients of each dish. Exclude salt and pepper. Return the ingredients in a list format"},
                {"role": "user", "content": f"Here is the name of the dish: {user_input}. Return ONLY the ingredients seperated by commas. No other text"} ]
            )

    raw_response = response.choices[0].message.content
    ingredients = [ingredient.strip() for ingredient in raw_response.split(",")]
    return ingredients

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

        cleaned_data = clean_data(data)
        cleaned_data = cleaned_data[:4]
        return cleaned_data
    except urllib.error.URLError as e:
        return f"Error fetching data: {e}"

def get_images(ingredient):
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
        images = images[:4]
        return images
    except urllib.error.URLError as e:
        return f"Error fetching data: {e}"

def clean_data(data):
    result = []

    price_pattern = re.compile(r'(.+),\s*\$([\d.]+)$')

    for item in data:
        match = price_pattern.match(item)
        if match:
            name = match.group(1)
            price = match.group(2)
            result.append([name, price])

    return result

def mergeDataImage(data_list, img_list):
    return [item + [img] for item, img in zip(data_list, img_list)]

if __name__ == "__main__":
    dish = "hamburger"
    get_ingredients(dish)
    website = get_website_data("hamburger buns")
    images = get_images("hamburger buns")
    mergeDataImage(website, images)