#By: Sabria Fafach
#Date: April 4, 2025
#Title: Employee_class.py

class Employee:
    def __init__(self,name,IDnum,dpmt,title):
        self.__name=name
        self.__IDnum=IDnum
        self.__dpmt=dpmt
        self.__title=title

    def get_name(self):
        return self.__name

    def get_IDnum(self):
        return self.__IDnum

    def get_dpmt(self):
        return self.__dpmt

    def get_Title(self):
        return self.__title





