import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.165 Safari/537.36")
options.add_argument("accept=*/*")

s = Service(executable_path='C:\Program Files (x86)\Google')
driver = webdriver.Chrome(service=s, options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
  '''
})

driver.maximize_window()

def get_html(url):
    try:
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source,"lxml")
        find_element = soup.find("div",class_="col col--8").find_all("p")
        with open ("test.txt","w",encoding= 'utf-8') as file:
             for item in find_element: 
                 file.write(item.text)       

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_html("https://scrapeops.io/selenium-web-scraping-playbook/python-selenium-undetected-chromedriver/")


if __name__ == "__main__":
    main()
