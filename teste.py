from selenium import webdriver
from time import sleep
from senhas import instagram

class insta_bot:
    def __init__(self, user, senha):
        #Define o driver que estou usando
        self.driver = webdriver.Chrome()

        #Salva o nome de usuário em uma variável
        self.user = user

        #Abre o instagram
        self.driver.get("https://instagram.com")
        sleep(2)

        #Essa parte preenche usuário e senha no login e obtém acesso à conta desejada
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(user)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(senha)
        self.driver.find_element_by_xpath('//button[@type= "submit"]')\
            .click()
        sleep(4)

        #Essa parte ignora os pop ups
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
        .click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
        .click()
        sleep(3)

        #Acessa o perfil do usuário
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.user))\
        .click()
        sleep(3)
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1.5)

        

        # SCROLL_PAUSE_TIME = 0.5

        # # Get scroll height
        # last_height = self.driver.execute_script("return document.body.scrollHeight")

        # while True:
        #     # Scroll down to bottom
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #     # Wait to load page
        #     sleep(SCROLL_PAUSE_TIME)

        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = self.driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height
        
        sleep(100)


    

insta_bot('andorinhasdoamor', instagram)