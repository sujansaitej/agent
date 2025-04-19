from excel_funcs import run_steps_sequentially, run_steps_from_excel
import asyncio
import os

if __name__ == '__main__':
    action = "amazon" # Pick here which action to run

    if action == "xls":
        result = asyncio.run(run_steps_from_excel("demo.xlsx"))

    elif action == "google":
        result = asyncio.run(run_steps_sequentially([
            "Go to google.com",
            "Search for cats",
            "Click 'search'",
            "Click on images",
            "Search for dogs",
            "Click 'search'",
            "Switch to regular search",
            "Search for python programming",
            "Click 'search'",
            "Click on first link",
            "Go back to Google.com",
            "Type in 'hello world' to the search bar",
            "Go to youtube.com",
            "Search for 'funny cat videos'",
            "Click 'search'",
            "Get the name and URL of the first result",
        ]))

    elif action == "amazon":
        username = os.getenv("AMAZON_USER")
        password = os.getenv("AMAZON_PASS")
        result = asyncio.run(run_steps_sequentially([
            "Open amazon.in",
            "Click on sign in",
            "Enter this as email/Username : " + username,
            "Click continue", # <-- added
            "If there's a captcha, solve it (note that there are no spaces in the captcha). Try many times if you fail at first.", # <-- added
            "Enter password: " + password,
            "Click sign in",
            "click on amazon search bar",
            "Search for oppo mobile charger original c type",
            "Click on the first product under results",
            "Click on add to cart ",
            "if asked for extended warranty skip the process",
            "click on go to cart",
            "click on proceed to buy",
        ]))

    print(result)

    print("\nFinal result:", result[0])
