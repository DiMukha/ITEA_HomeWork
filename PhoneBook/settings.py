from ITEA_HomeWork.PhoneBook.file_app import config


config.create_config(format='csv')
file_format = config.read_config()

if file_format == 'json':
    from ITEA_HomeWork.PhoneBook.file_app import json_work as file_work
elif file_format == 'pickle':
    from ITEA_HomeWork.PhoneBook.file_app import pickle_work as file_work
elif file_format == 'csv':
    from ITEA_HomeWork.PhoneBook.file_app import csv_work as file_work

load, save = file_work.load, file_work.save