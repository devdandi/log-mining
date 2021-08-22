from main.connection.serv import Serv
import configparser
import glob
import threading
import time
import logging
import re


class Gather():

    def __init__(self):
        self.data = Serv()
        self.directory_logs = {
                "APACHE2" : "C:/xampp/apache/logs",
                "NGINX" : "/var/log/nginx",
                "PM2" : "$HOME/.pm2/logs/XXX-error.log"
                ## add manualy
            }

    def run(self, files, app):
        f = open(files, 'r')
        while True:
            line = ''
            while len(line) == 0 or line[-1] != '\n':
                
                tail = f.readline()
                
                if tail == '':
                    time.sleep(1)
                    configparser
                line+=tail

            # print(line)
            # self.data.sendMessage("{}".format(line)) # sending message to mosquitto 
            self.data.sendMessage(str({"APP_NAME" : app, 'LOG' : line}))
            # return True



            


if __name__ == '__main__':
    ths = []
    gather = Gather()
    gather.data._connect()
    config = configparser.ConfigParser()
    config.read(glob.glob('properties/*production.properties'))
    config.sections()

    for app in config['ApplicationSection']['app.name'].split(','):
        log_files = glob.glob(gather.directory_logs[app] +'/*.log')
        

        for files in log_files:

            th = threading.Thread(target=gather.run, args=(files, app,))
            ths.append(th)

    for t in ths:
        t.start()



        



    # gather._GatherLogApplication()
    # logging.info("RUNNING APP")
    # th = threading.Thread(target=Gather()._GatherLogApplication(), args=(), daemon=True)
    # th.join()
    
    # th.start()


