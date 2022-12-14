from datetime import date, datetime
import logging
import os


class App_Logger:
    def __init__(self) -> None:
        pass

    def log(self,file_object,log_message):
        self.now  = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_object.write( str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message +"\n")

