from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("Welcome to the google bot!")

search_item = input("What would you like to search in google: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

bot = webdriver.Chrome(options=chrome_options)
bot.get("https://google.com")

search = bot.find_element(By.NAME, "q")
search.send_keys(search_item, Keys.ENTER)
