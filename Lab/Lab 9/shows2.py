import requests

BASE_URL = "https://api.tvmaze.com/"

def get_shows(query):
    url = BASE_URL + 'search/shows?q=' + query.lower()
    return requests.get(url).json()

def format_show_name(show):
    name = show['name']
    if (show['premiered'] == None):
        s_year = "?"
    else:
        s_year = show['premiered'][:4]
    if (show['ended'] == None):
        e_year = "?"
    else:
        e_year = show['ended'][:4]
    if (len(show['genres']) == 0):
        genres = "?"
    else:
        genres = ""
        number = len(show['genres'])
        for i in range(number):
            if (i == 0):
                genres = show['genres'][i]
            else:
                genres = genres + ", " + show['genres'][i]
    return name + " (" + s_year + " - " + e_year + ", " + genres + ")"

def main():
    query = input("Search for a show: ")
    results = get_shows(query)
    if (not results):
        print("\nNo results found")
    else:
        n = 1
        print("\nHere are the results:")
        for result in results:
            show = result["show"]
            print(str(n) + ". " + format_show_name(show))
            n += 1

if __name__ == "__main__":
    main()