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


def get_seasons(show_id):
    url = BASE_URL + "shows/" + show_id + "/seasons"
    return requests.get(url).json()


def format_season_name(season):
    number = str(season['number'])
    if (season['episodeOrder'] == None):
        ep = "?"
    else:
        ep = str(season['episodeOrder'])
    if (season['premiereDate'] == None):
        s_year = "?"
    else:
        s_year = season['premiereDate'][:4]
    if (season['endDate'] == None):
        e_year = "?"
    else:
        e_year = season['endDate'][:4]
        return 'Season ' + number + " (" + s_year + " - " + e_year + "), " + ep + " episodes"


def get_show_name(show_id):
    url = BASE_URL + "shows/" + show_id
    return requests.get(url).json()["name"]


def main():
    query = input("Search for a show: ")
    results_show = get_shows(query)
    if (not results_show):
        print("\nNo results found")
    else:
        n = 1
        show_id_list = []
        print("\nHere are the results:")
        for result in results_show:
            show = result["show"]
            print(str(n) + ". " + format_show_name(show))
            show_id_list.append(str(show['id']))
            n += 1

    show_index = int(input("\nSelect a show: ")) - 1
    show_id = show_id_list[show_index]
    results_seasons = get_seasons(show_id)
    print("Season of " + get_show_name(show_id) + ": ")
    season_id_list = []
    for season in results_seasons:
        print(format_season_name(season))
        season_id_list.append(str(season['id']))


if __name__ == "__main__":
    main()