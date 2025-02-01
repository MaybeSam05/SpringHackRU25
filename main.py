import openai
from dotenv import load_dotenv

load_dotenv()

def get_ingredients():
    user_input = "Hamburger"

    response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[ 
                {"role": "system", "content": "Act as a master chef. You will be given the name of a dish and you are to identify the individual ingredients of each dish. Return the ingredients in a list format"},
                {"role": "user", "content": f"Here is the name of the dish: {user_input}. Return ONLY the ingredients seperated by commas. No other text"} ]
            )

    print(response.choices[0].message.content)
        
if __name__ == "__main__":
    get_ingredients()