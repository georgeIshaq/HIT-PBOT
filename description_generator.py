import openai
from web_scraper import get_prod_title_desc
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI()


def rewrite_description(title, description):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    prompt = f"Your goal is to re-write and clarify the following product description for an online electronics store. Maintain information accuracy and a simple yet clear writing style. The output should be in the following format: [SHORT INTRODUCTION] [MAIN FEATURES] [TECHNICAL SPECIFICATIONS] Remove any unnecessary information about deals, sales, seller info, product origin, etc. Keep only the information about the product itself. \n \n Title: {title} \n Description: {description}"

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    return completion.choices[0].message


def main():
    url = 'https://vi.aliexpress.com/item/1005005707583364.html'
    title, description = get_prod_title_desc(url)
    new_description = rewrite_description(title, description)
    print("\nRewritten Description:")
    print(new_description)


if __name__ == "__main__":
    main()
