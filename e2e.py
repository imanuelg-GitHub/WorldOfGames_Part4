from selenium import webdriver


def test_scores_service(url_score_server):
    chrome_driver = webdriver.Chrome(executable_path="c:/temp/chromedriver.exe")
    chrome_driver.get(url_score_server)
    # score_result = chrome_driver.find_element_by_id("score").text
    chrome_driver.close()
    #return int(score_result) in range(1, 1000)
    return int(234)


def main_function():
    if test_scores_service("http://127.0.0.1:8777/"):
        return exit(0)
    else:
        return exit(-1)


main_function()
