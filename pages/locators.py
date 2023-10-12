from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN = (By.XPATH, "//*[@id='login_form']/h2")
    REGISTER = (By.XPATH, "//*[@id='register_form']/h2")