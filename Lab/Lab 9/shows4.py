import requests

BASE_URL = "https://api.tvmaze.com/"

def get_shows(query):
    url = BASE_URL + 'search/shows?q=' + query.lower()
    return requests.get(url).json()


def format_show_name(show):
    name = show['name']  # gets the name of the show
    if (show['premiered'] == None):  # checks if the starting date exists
        s_year = "?"
    else:
        s_year = show['premiered'][:4]  # gets just the year from the entire date
    if (show['ended'] == None):  # checks if the ending date exists
        e_year = "?"
    else:
        e_year = show['ended'][:4]  # gets just the year from the entire date
    if (len(show['genres']) == 0):  # checks if the genres are listed or not
        genres = "?"
    else:  # this piece of code converts the list of genres into a list
        genres = ""
        number = len(show['genres'])
        for i in range(number):
            if (i == 0):
                genres = show['genres'][i]
            else:
                genres = genres + ", " + show['genres'][i]
    return name + " (" + s_year + " - " + e_year + ", " + genres + ")"  # returns the formatted name


def get_seasons(show_id):
    url = BASE_URL + "shows/" + show_id + "/seasons"
    return requests.get(url).json()


def format_season_name(season):
    number = str(season['number'])  # gets the season number
    if (season['episodeOrder'] == None):  # checks if the episode number exists
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
    return requests.get(url).json()["name"]  # returns just the name of the show


def get_episodes_of_season(season_id):
    url = BASE_URL + "seasons/" + season_id + "/episodes"
    return requests.get(url).json()


def format_episode_name(episode):
    s_number = episode["season"]
    if (episode["number"] == None):
        e_number = "?"
    else:
        e_number = episode["number"]
    if (episode["name"] == None):
        name = "?"
    else:
        name = episode["name"]
    if (episode["rating"]["average"] == None):
        rating = "?"
    else:
        rating = episode["rating"]["average"]
    return "S" + str(s_number) + "E" + str(e_number) + " " + name + " (rating: " + str(rating) + ")"


def main():
    query = input("Search for a show: ")  # gets the query from the user
    results_show = get_shows(query)  # gets the results
    if (not results_show):  # checks whether shows with the query name exist
        print("\nNo results found")
    else:
        n = 1
        show_id_list = []  # stores the id's of the shows
        print("\nHere are the results:")
        for result in results_show:  # loops through all the results
            show = result["show"]
            print(str(n) + ". " + format_show_name(show))  # formats the name
            show_id_list.append(str(show['id']))
            n += 1

    show_index = int(input("\nSelect a show: ")) - 1
    show_id = show_id_list[show_index]  # gets the show's id from the list
    results_seasons = get_seasons(show_id)  # gets the seasons from the selected show
    print("Season of " + get_show_name(show_id) + ": ")
    season_id_list = []  # stores the id's of the seasons
    for season in results_seasons:  # loops through all the seasons
        print(format_season_name(season))
        season_id_list.append(str(season['id']))

    season_index = int(input("\nSelect a season: ")) - 1
    season_id = season_id_list[season_index]  # gets the season id from the list
    results_episodes = get_episodes_of_season(season_id)  # gets the episodes from the selected season
    for episodes in results_episodes:  # loops through all the episodes
        print(format_episode_name(episodes))


if __name__ == "__main__":
    main()