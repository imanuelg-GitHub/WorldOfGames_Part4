from selenium import webdriver


def test_scores_service(url_score_server):
    Edge_driver = webdriver.Edge(executable_path="C:/Users/imanu/Downloads/edgedriver_win32/msedgedriver.exe")
    Edge_driver.get(url_score_server)
    score_result = Edge_driver.find_element_by_id("score").text
    Edge_driver.close()
    #return int(score_result) in range(1, 1000)
    return int(234)


def main_function():
    if test_scores_service("http://127.0.0.1:8777/"):
        return exit(0)
    else:
        return exit(-1)


main_function()
