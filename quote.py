import json
from RequestEasy import request as r

def GetQuote():
    response = r("quotes-api-self.vercel.app/quote")

    try:
        data = json.loads(response.text)  # Parse the JSON string
        quote = data["quote"]
        author = data["author"]
        
        things = [f"quote: {quote}", f"author: {author}"] # Creates the list
        return things

    except json.JSONDecodeError:
        print("Error: Could not decode JSON. Invalid JSON format.")