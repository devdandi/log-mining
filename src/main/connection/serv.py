import glob 
from paho.mqtt import client as mqtt_client
import time 
import configparser

class Serv():


    def __init__(self):
        self.client = None 
        self.statusConnection = False
        self.config = None

    def _connect(self):

        if self.statusConnection == False:
            config = self._getConfig()

            try: 
                config = config['ProtocolSection']
                client = mqtt_client.Client('log-mining-{}'.format(range(0, 10000)))
                client.username_pw_set(config['app.user'], config['app.password'])
                client.connect(config['app.host'])
                print("Connected to {}".format(config['app.host']))
                self.client = client
                self.runTest()
                print("Running test successful")
            except: 
                print("Error connection to host {}".format(config['ProtocolSection']['app.host']))

    def _getConfig(self):

        files = glob.glob('properties/*production.properties')
        config = configparser.ConfigParser()
        
        for file in files:
            config.read(file)
            config.sections()
            self.config = config

            return config

    def sendMessage(self, message):
        self.client.publish(self.config['ProtocolSection']['app.topic'], message)
    
    def runTest(self):
        self.client.publish('server/log', 'Yey, message was delivered')


if __name__ == '__main__':
    main = Serv()
    main._connect()