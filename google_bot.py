from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def google_search(search_text):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    bot = webdriver.Chrome(options=chrome_options)
    bot.get("https://google.com")

    search = bot.find_element(By.NAME, "q")
    search.send_keys(search_text, Keys.ENTER)
