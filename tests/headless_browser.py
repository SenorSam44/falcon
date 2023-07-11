import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")  # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
with open("../config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)
    PATH = config["headless_browser_path"]

driver = webdriver.Chrome(PATH, options=chrome_options)
start_url = "https://duckgo.com"
driver.get(start_url)
print(driver.page_source.encode("utf-8"))
driver.quit()
