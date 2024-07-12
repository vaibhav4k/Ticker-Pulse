#Code to retrive H1 from the mentioned website and print it
from selenium import webdriver  #Used for webdriver functionality implementations
from selenium.webdriver.common.keys import Keys      #Used to use the keyboard keysṇ
from selenium.webdriver.common.by import By     #Used to locate elements in a web page

def priceFetch(symbl):
    driver = webdriver.Chrome()                        #Opens a Chrome Instance
    driver.get("https://in.tradingview.com/symbols/"+symbl+"/")   #Navigates to the Symbols Price Page
    try:
        symbol=(driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]/span[1]/div[1]/span[1]")).text
        name = (driver.find_element(By.XPATH, "//h1[contains(@class, 'apply-overflow-tooltip title-HFnhSVZy')]")).text
        exchange=(driver.find_element(By.XPATH, "//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]/span[1]/div[1]/span[2]")).text
        market_price=(driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/span[1]/span[1]")).text
        price_fetch_time=(driver.find_element(By.XPATH, "//div[3]/div[1]/div[1]/div[3]/span[1]/span[1]")).text
        #technical_recomendation=(driver.find_element(By.XPATH, "//div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/span[5]")).text
        #market_capitalization=

        return (symbol,name,exchange,market_price,price_fetch_time)
    except:
        if((driver.find_element(By.XPATH, "//h1[contains(@class, 'tv-http-error-page__title')]")).text=="This isn't the page you're looking for"):
            return ("Symbol not found",'','','','')
    finally:
        driver.quit()

if __name__ == "__main__":
    print(priceFetch(input()))