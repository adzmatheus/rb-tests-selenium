from abc import ABC

# Implementações do POM (PageObjectModel)

# Funções do browser
class SeleniumObject:
    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)

# Funções das página
class Page(ABC, SeleniumObject):
    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url
        self._reflection()

    def open (self):
        self.webdriver.get(self.url)

    def _reflection(self):
        for attribute in dir(self):
            real_attribute = getattr(self, attribute)
            if isinstance(real_attribute, PageElement):
                real_attribute.webdriver = self.webdriver

# Funções dos elementos
class PageElement(ABC, SeleniumObject):
    def __init__(self, webdriver=None):
        self.webdriver = webdriver

