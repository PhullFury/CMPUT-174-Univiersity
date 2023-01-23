'''
This program takes the temperature in celcius and converts it into fahrenheit
Author: Harmanpreet Singh Phull
When: January 16th, 2023
'''

celcius = int(input("What's the temperature in Canada: "))  
fahrenheit = (celcius * 9 / 5) + 32 #fahrenheit is being calculated

print(str(celcius) + " degrees in Canada would be " + str(round(fahrenheit)) + " degrees in Springfield. D'oh!") 