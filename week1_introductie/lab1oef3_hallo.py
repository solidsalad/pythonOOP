naam = input("wat is je naam? ")
interesses = input("wat zijn je interesses? (telkens gescheiden door een komma): ")
interesses = interesses.replace(", ", "\n")

print(f"naam:\n{naam}\n\ninteresses:\n{interesses}")