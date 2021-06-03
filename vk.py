import vk_api
import getpass

from db import *

NSTU_VK_ID = 670
CURRENT_YEAR = 2021
START_YEAR = 1950

class Vk:
    def __init__(self):
        login = input('Введите логин:\n')
        password = getpass.getpass('Введите пароль:\n')
        vk_session = vk_api.VkApi(login, password, auth_handler = self._auth_handler)
        vk_session.auth()
        self.vk = vk_session.get_api()
        self.bd = DataBase()

    def _auth_handler():
        return input('Введите код:\n'), False
       
    def createUsers(self):
        for year in range(START_YEAR,CURRENT_YEAR):
            users = self.vk.users.search(university = NSTU_VK_ID, university_year = year, count = 1000, fields = 'career')
            self.addInDbUsers(users['items'])

    def addInDbUsers(self,users):
        for item in users: 
            name = ''
            if 'first_name' in item and 'last_name' in item:
                name = f"{item['first_name']} {item['last_name']}"
            elif 'first_name' in item: 
                name = item['first_name']
            elif 'last_name' in item:
                name = item['last_name']
            userId = item['id']
            self.bd.createUser(userId, name)
            if 'career' in item: 
                for career in item['career']:
                    if 'company' in career:
                        self.bd.createCompany(career['company'], userId)

    