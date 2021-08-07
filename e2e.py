import os
from selenium import webdriver


def test_scores_service():
    Edge_driver = webdriver.Edge(executable_path="C:/Users/imanu/Downloads/edgedriver_win32/msedgedriver.exe")
    Edge_driver.get("http://localhost:8777/")
    score = Edge_driver.find_element_by_tag_name("scores").text
    if 1 <= int(score) <= 1000:
        return True
    return False


def main():
    if test_scores_service():
        return 0
    else:
        os._exit(-1)


main()
