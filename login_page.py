class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://zenclass.in/login")

    def is_login_page_loaded(self):
        return "zenclass.in" in self.driver.current_url

    def login(self, user, pwd):
        # Zen uses Google OAuth — simulated step
        pass

    def logout(self):
        self.driver.get("https://zenclass.in/login")
