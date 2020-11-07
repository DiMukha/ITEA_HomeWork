import configparser

def create_config(**format):
    config = configparser.ConfigParser()
    config['file'] = format
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    file_format = config['file']['format']
    return file_format
