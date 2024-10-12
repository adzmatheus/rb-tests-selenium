from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# import os
# os.system('Xvfb :99 &')

url_grid = "http://localhost:4444/"

# capabilities = {
#     "browserName": "chrome",
#     "version": "109",
#     "enableVNC": True,
#     "enableVideo": False
# }

# options = webdriver.ChromeOptions()

# driver = webdriver.Remote(
#     command_executor=url_grid,
#     # desired_capabilities=capabilities
#     options=options
# )


# Definir as capacidades para o navegador (Chrome)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Roda no modo headless (opcional)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# URL do Selenium Hub rodando no Docker (localhost)
hub_url = "http://localhost:4444/wd/hub"

# Conectar ao Selenium Hub usando as capacidades do Chrome
driver = webdriver.Remote(
    command_executor=hub_url,
    options=chrome_options
)

# Exemplo: Navegar até o Google e imprimir o título da página
driver.get("https://www.google.com")
print(driver.title)

driver.quit()