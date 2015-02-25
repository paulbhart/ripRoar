__author__ = 'paulhart'
from selenium import webdriver
from config import RECOMMENDED_URL, BALANCE_URL
import ipdb


class RipRoar():

    def __init__(self):
        self._scenerios = {}
        self._DRIVER = webdriver.Firefox()

    def _find_recommended_data(self, sceneriolist):

        return [self._get_recommended_scenerio_data(scenerio) for scenerio in sceneriolist]

    def parse_recommended(self):
        self._DRIVER.get(RECOMMENDED_URL)

        raw_scenerio_data = []
        for type in ("SmallCount", "LargeCount"):
            raw_scenerio_data = raw_scenerio_data + \
                                self._find_recommended_data(self._DRIVER.find_elements_by_class_name(type))
        self._scenerios += raw_scenerio_data

    @staticmethod
    def _get_recommended_scenerio_data(scenerio):
        raw_data = []
        i = 0
        title = ""
        sid = ""
        for element_data in scenerio.find_elements_by_xpath("td"):
            value = element_data.get_attribute("innerHTML")
            if i == 0:
                title = value
                i += 1
                continue
            elif i == 1:
                sid = value
                i += 1
                continue
            elif i == 2:
                title += "+"
                title += sid
                raw_data.append(title)
                title = ""
                sid = ""
            raw_data.append(value)
        return raw_data

    def parse_balance(self):
        self.DRIVER.get(BALANCE_URL)
        raw_scenerio_data = []

        tables_of_scenerios = [table for table in self._DRIVER.find_elements_by_xpath("tbody")]
        scenerios = [scenerio for scenerio in tables_of_scenerios.find_elements_by_xpath("tr")]
        print scenerios
        # self._scenerios += raw_scenerio_data


def main():
    parser = roarParser()
    # parser.parse_recommended()
    parser.parse_balance()

if __name__ == "__main__":
    main()