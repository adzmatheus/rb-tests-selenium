from biblioteca import Page, PageElement
from selenium.webdriver.common.by import By

# ---------------- Page Object -----------------
class BasePage(Page):
    navbar = None

class PageConcorrente(Page):
    concorrente = Concorrente()


# ---------------- Page Elements ----------------
class Concorrente(PageElement):
    name = (By.XPATH,"//input[@formcontrolname='name']")
    description = (By.XPATH,"//input[@formcontrolname='description']")
    submit = (By.XPATH,"//span[@class='mdc-button__label'][contains(.,'Salvar')]")


    def create_concorrente(self, name, description):
        self.find_element(self.name).send_keys(name)
        self.find_element(self.description).send_keys(description)
        self.submit.click()
