'''
This program takes the episode info from the user and changes its format using find() and string slicing
Author: Harmanpreet Singh Phull
When: January 16th, 2023
'''

ep_info = input("Write the name of the episode name: ")

first_break = ep_info.find("_") #finding the position of the first underscore
second_break = ep_info.rfind("_") #finding the position of the second underscore
season_number = ep_info[1:first_break] #storing the season number using string slicing
ep_number = ep_info[first_break+2:second_break] #storing the episode number using string slicing
ep_name = ep_info[second_break+1:len(ep_info)] #storing the episode name using string slicing

print("Season " + season_number + ", Episode " + ep_number + ": " + ep_name + " (The Simpsons)") 

'''
documention for rfind() can be found on this website: https://www.programiz.com/python-programming/methods/string/find
'''