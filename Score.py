from Utilities import SCORES_FILE_NAME


def add_score(game_difficulty):
    POINTS_OF_WINNING = int(game_difficulty) * 3 + 5
    try:
        f = open(SCORES_FILE_NAME, "r+")  # open for reading and writing
        try:
            POINTS_OF_WINNING += int(f.read()) # make sure value in scores.txt is a number we can process
            f.seek(0)  # reset file pointer to beginning
            f.truncate(0)  # clear current file content
            f.write(str(POINTS_OF_WINNING))  # write new score to file
            f.close()
        except ValueError:  # if scores.txt does not have a number (for any reason), then re-create file as new
            print("Could not read value from " + SCORES_FILE_NAME + " re-creating as new...")
            f = open(SCORES_FILE_NAME, "w")
            f.write(str(POINTS_OF_WINNING))  # write new score to file
            f.close()
    except IOError: # scores.txt file does not exist, so create it
        print("Could not find " + SCORES_FILE_NAME + " file for reading and writing, creating...")
        f = open(SCORES_FILE_NAME, "w")
        f.write(str(POINTS_OF_WINNING))  # write new score to file
        f.close()
