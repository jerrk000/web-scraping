import helium
from bs4 import BeautifulSoup

# you have to have Chrome installed to use the chromedriver
# you have to add the chromedriver to your PATH, so that helium (and selenium) can find it

# Alternative, if you don't want to add the chromedriver to your PATH
# disclaimer: if you do that, you have to rewrite code a little.
# from selenium import webdriver
# driver = webdriver.Chrome('/path/to/chromedriver')

url = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz?sfId=48526452-d134-4338-9860-849ae2aa136f&isNavigation=true&keyword=Yugioh"

driver = helium.start_chrome(url, headless=True)

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Change tag and classname for things you are looking for
#                      tag              classname
boxes = soup.find_all('div', {'class': 'Box-sc-wfmb7k-0 txlGb'})

for item in boxes:
    name = item.find('h3', {'class': 'Text-sc-10o2fdq-0 bsRRaI'}).text
    print(name)