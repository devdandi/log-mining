from main.connection.serv import Serv
import configparser
import glob
import threading
import time


class Gather():

    def __init__(self):
        self.data = Serv()
        self.directory_logs = {
                "APACHE2" : "C:/xampp/apache/logs",
                "NGINX" : "C:/xampp/nginx/logs"
            }
        

    def _GatherLogApplication(self):
        files = glob.glob('properties/*production.properties')
        config = configparser.ConfigParser()
        config.read(files)
        config.sections()
        self.data._connect()

        apps = config['ApplicationSection']['app.name'].split(',')

        for app in apps:
            log_files = glob.glob(self.directory_logs[app] +'/*.log')
            
            for log in log_files:

                f = open(log, 'r')

                while True:
                    line = ''
                    while len(line) == 0 or line[-1] != '\n':
                        tail = f.readline()

                        if tail == '':
                            time.sleep(1)
                            continue
                        line += tail
                    print(line)
                    self.data.sendMessage(line)


    def run(self):
        return True
        
            


if __name__ == '__main__':
    gather = Gather()
    gather._GatherLogApplication()