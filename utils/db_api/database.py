import os
from environs import Env

env = Env()
env.read_env()


class Database:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_data = None
        with open("utils/db_api/database.txt", "r+") as file:
            db = file.readlines()
            print(db)
            is_database = False
            for line in db:
                if str(self.user_id) in line:
                    is_database = True
                    break
            if not is_database:
                file.write(f"{self.user_id}\n")

    def get_data(self):
        with open("utils/db_api/database.txt", "r") as file:
            data = file.readlines()
            for line in data:
                if str(self.user_id) in line:
                    self.user_data = line.split(",")
                    return self.user_data

    def get_channels(self):
        # if self.user_id in env.list("ADMINS"):
        with open("utils/db_api/database.txt", "r") as file:
            data = file.readlines()
            for line in data:
                print(line)
                if str(1737841515) in line:
                    channels = line.split(",")
                    response = []
                    for data in channels:
                        print(response)
                        if data.startswith("channel-"):
                            response.append(data.split('-')[-1])
                    return response

    def add_data(self, data):
        file_path = "utils/db_api/database.txt"
        with open(file_path, "r+") as file:
            db = file.readlines()
            new_db = ""
            for line in db:
                if str(self.user_id) in line:
                    line = line[:-1] + "," + data
                    new_db += (line + "\n")
                else:
                    new_db += line
            os.remove(file_path)
            with open(file_path, "w") as files:
                files.write(new_db)
