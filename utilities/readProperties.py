import configparser
import os
from pathlib import Path

config = configparser.RawConfigParser()
config.read("Configurations/config.ini")
print(str(config.sections()))


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common_info', 'baseURL')
        print('getting url: ' + url)
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common_info', 'username')
        print('getting username: ' + username)
        return username

    @staticmethod
    def getPassword():
        pwd = config.get('common_info', 'password')
        print('getting passwprd: ' + pwd)
        return pwd
