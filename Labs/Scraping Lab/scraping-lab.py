from bs4 import BeautifulSoup
import requests

# SCRAPING PROBLEMS
# Twitter Scraping (15pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweets located on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

#  print("{} {}!".format("Hello", "World"))
print("{} {}!".format("Hello", "World"))

twit_url = "https://twitter.com/arielhelwani"
twit_page = requests.get(twit_url)

twit_soup = BeautifulSoup(twit_page.text, "html.parser")
print(twit_soup.prettify())

# tweets = twit_soup.find_all(aria_label="Timeline: Ariel Helwani’s Tweets", class_="css-1dbjc4n")
# tweet_divs = twit_soup.find_all(id="accessible-list-2")
tweet_divs = twit_soup.find_all("div", class_="tweet")
print(tweet_divs[0].text)


for i in range(5):
    print(tweet_divs[i].text)

# Weather Scraping (15pts)
# Below is a link to a 10-day weather forecast at weather.com
# Pick the weather for a city that has the first letter as your name.
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (5pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.
# if the sentence is a little different than shown, that will work; do what you can.  Don't forget about our friend string.format()

print("{} {}!".format("Hello", "World"))

weather_url = "https://weather.com/weather/tenday/l/368d5a4e7d156c3f508cb653f95018ec2747fdacb01e8d8d17386237f84962ac"
weather_page = requests.get(weather_url)

weather_soup = BeautifulSoup(weather_page.text, "html.parser")
print(weather_soup.prettify())


