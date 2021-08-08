import random
import requests
import os
from requests.exceptions import HTTPError

SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    os.system('cls')  # this is working on Windows


def validate_input(user_input, valid_start, valid_end):
    if float(valid_start) <= float(user_input) <= float(valid_end):
        return True
    else:
        raise ValueError
        return False


def generate_random_number(min, max):
    return random.randint(int(min), int(max))


def get_user_input(number_of_entries, min, max):
    user_list = []
    while True:
        print("\nPlease enter your guessed number : ")
        user_input = input()
        try:
            float_user_input = float(user_input)
        except ValueError:
            print("You entered invalid input such as string\nCannot convert", user_input,
                  "to float\nPlease try again...")
        else:
            if float_user_input >= 0:
                if max is not None:
                    try:
                        if validate_input(user_input, min, max):
                            user_list.append(float(user_input))
                    except ValueError:
                        print("\nYou entered a number outside the range of", min, "and", max, "\nPlease try again...")
                else:
                    user_list.append(float(user_input))
            else:
                print("\nYou entered a negative number\nPlease try again...")

            # stop asking for numbers when we reach size of difficulty,
            # this guarantees both lists sizes will always be the same
            if len(user_list) == int(number_of_entries):
                return user_list


def get_fx_rate():
    while True:
        ccy1 = input("\nPlease enter your FROM currency : ")
        ccy2 = input("Please enter your TO currency : ")

        # currencies on this url must be lowercase
        url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/"
        url += ccy1.lower()
        url += "/"
        url += ccy2.lower()
        url += ".json"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as e:
            print("HTTP error occurred: ", e.args, "\nPlease try again...")
        except Exception as e:
            print("Error occurred trying to access URL:", e.args, "\nPlease try again...")
        else:  # return currency1, currency2 and FX rate
            return \
                ccy1.upper(), \
                ccy2.upper(), \
                float(round(response.json()[ccy2.lower()], 2))  # return FX rate 2 decimals
