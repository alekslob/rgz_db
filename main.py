from vk import Vk
from db import DataBase

def main():
    vk = Vk()
    vk.createUsers()

    # # Печать таблиц
    # db = DataBase()
    # db.getUsers()
    # db.getCompanies()

if __name__ == "__main__":
	main()