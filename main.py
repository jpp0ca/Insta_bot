#Ler caderno para entender as alterações.

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
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
        .click()
        sleep(3)

        #Acessa o perfil do usuário
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.user))\
        .click()
        sleep(3)
    
    def pegar_dados(self):
        #Salva o número de publicações do perfil do instagram
        n_publi = self.driver.find_element_by_xpath('//div[@id="react-root"]/section/main/div/header/section/ul//li[1]/span/span').text
        
        #Roda cada uma das publicações
        for n in range(1, int(n_publi) + 1):
            if n % 3 != 0:
                #Abre a Publicação
                self.driver.find_element_by_xpath('//div[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[{}]/a'.format(n))\
                .click()
                sleep(2)

                # #Abre o Insights
                # self.driver.find_element_by_xpath("//button[contains(text(), 'Ver insights')]")\
                # .click()
                # sleep(3)

                # '''Inserir aqui codigo que coleta os dados dos insights'''

                # #Fecha o Insights
                # self.driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[1]/div/div[2]/button')\
                # .click()
                # sleep(2)

                #Fecha a publicação
                self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/button')\
                .click()
                sleep(2)

            else:
                #Abre a Publicação
                self.driver.find_element_by_xpath('//div[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[{}]/a'.format(n))\
                .click()
                sleep(2)

                '''Inserir Aqui forma de dar scroll down'''
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight/3)")
                sleep(2)

                # Abre o Insights
                # self.driver.find_element_by_xpath("//button[contains(text(), 'Ver insights')]")\
                # .click()
                # sleep(3)

                # '''Inserir aqui codigo que coleta os dados dos insights'''

                # Fecha o Insights
                # self.driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[1]/div/div[2]/button')\
                # .click()
                # sleep(2)

                # Fecha a publicação
                self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/button')\
                .click()
                sleep(2)
            

        self.driver.close()   

'''Ler melhor sobre como efetuar esse scroll down
   Não acho que a função abaixo é a melhor opção.
'''

# def ScrollDown():
#     driver = webdriver.Chrome()
#     SCROLL_PAUSE_TIME = 0.5

#     # Get scroll height
#     last_height = driver.execute_script("return document.body.scrollHeight")

#     while True:
#         # Scroll down to bottom
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#         # Wait to load page
#         sleep(SCROLL_PAUSE_TIME)

#         # Calculate new scroll height and compare with last scroll height
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height

#/html/body/div[7]/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/span
#//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[2]/div[1]/a
#/html/body/div[7]/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div[2]/span

#/html/body/div[7]/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/span

#/html/body/div[5]/div[3]/button

#//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a
#//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a
#//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div/div[1]/a

#//div[@id="react-root"]/section/main/div/div[2]/article/div/div/div/div[2]/a

#/html/body/div[6]/div[3]/button

bot = insta_bot("andorinhasdoamor", instagram)
bot.pegar_dados()