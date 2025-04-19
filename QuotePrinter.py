from quote import GetQuote

CachedQuote = GetQuote()

print(f'"{CachedQuote[0].replace("quote: ", "")}" by {CachedQuote[1].replace("author: ", "")}')
input("\nPress Enter To Exit")