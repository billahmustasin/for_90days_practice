import logging

logging.basicConfig(format="%(asctime)s %(message)s",filename ='my_server_logs.log',datefmt='%d/%m/%Y', level=logging.INFO)

print(dir(logging))
logging = logging.getLogger()
print(dir(logging))

logging.info("this is fine")

logging.warning("this code may break") 

logging.error("this is an error, need to fix")

logging.critical("this is critical error, fix it")