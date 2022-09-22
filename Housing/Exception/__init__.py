import os
import sys

class HousingException(Exception):
    
    def __init__(self,error_message:Exception,error_details:sys):
        super().__init__(error_message) #passing error message to parent class
        self.error_message = error_message 

    #staticmethod is called to get the detail error message
    #can be called without creating object
    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        
        #since the return type is string so converted to str
        _,_,exec_tb = error_detail.exc_info()
        #exc_info() return the information about 
        # the most recent exception caught
        #exec_tb is traceback of error traced other is size and value
        line_number = exec_tb.tb_frame.f_lineno

        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in script:[{file_name}] at line number:[{line_number}] and error message is [{error_message}]"

        return error_message    
    
    #information that can be displayed in print 
    def __str__(self) :
        return self.error_message

    #representation of the object
    def __repr__(self)-> str:
        return HousingException.__name__.str()    


