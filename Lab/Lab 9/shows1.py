import requests

BASE_URL = "https://api.tvmaze.com/"

def get_shows(query):
    url = BASE_URL + 'search/shows?q=' + query.lower()
    respose = requests.get(url)

    return respose.json()

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
            print(str(n) + ". " + show['name'])
            n += 1

if __name__ == "__main__":
    main()