class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def title_matches(self):
        # title matches
        return "Arbisoft" in self.driver.title

    def test_nav_links(self):
        nav_links = self.driver.find_elements_by_xpath("/html/body/header/div/div/div[2]/div/div/div/ul")







