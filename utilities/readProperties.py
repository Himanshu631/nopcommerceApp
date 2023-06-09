import configparser


config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class Read_Config:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info','baseurl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

