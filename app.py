import imp
from flask import Flask
from Housing.Exception import HousingException
from Housing.Logger import logging
try: 
    import sys
except ImportError:
    pass   
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info("hello there")
    return "hello bebe"    



if __name__ =="__main__":
    app.run(debug=False)