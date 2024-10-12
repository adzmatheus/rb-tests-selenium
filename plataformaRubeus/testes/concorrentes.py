from selenium.webdriver import Chrome
from page_objects.cadastroDeConcorrente import PageConcorrente, Concorrente

# --------------- Código de teste ---------------
browser = Chrome()
url = "https://crmdev17.apprbs.com.br/cadastro-concorrente/"

page = PageConcorrente(browser, url)

page.open()

# page.concorrente.create_concorrente(
#     "Exemplo",
#     "Teste de descrição"
# )