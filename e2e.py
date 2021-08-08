from selenium import webdriver


def test_scores_service(url):
    Edge_driver = webdriver.Edge(executable_path="C:/Users/imanu/Downloads/edgedriver_win32/msedgedriver.exe")
    Edge_driver.get(url)
    score = Edge_driver.find_element_by_xpath("/html/body/h1")
    Edge_driver.close()
    return int(str(score))
    #if 1 <= int(score) <= 1000:
    #    return True
    #return False


def main():
    if test_scores_service("http://127.0.0.1:8777/"):
        return exit(0)
    else:
        return exit(-1)


main()
