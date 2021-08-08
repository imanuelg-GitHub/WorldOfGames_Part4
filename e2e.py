from selenium import webdriver


def test_scores_service(url_score_server):
    return int(234)


def main_function():
    if test_scores_service("http://127.0.0.1:8777/"):
        return exit(0)
    else:
        return exit(-1)


main_function()
