import shutil
import logging
import schedule

logging.basicConfig(filename="day9/schedular_proj/logs.txt",level="INFO",)
def check_disk():
    disk = shutil.disk_usage("/")
    per_used = (disk.total - disk.free)/disk.total*100
    if per_used > 20:
        logging.warning("disk almostFUll")
    elif per_used > 95:
        logging.critical("disk full")

schedule.every(10).seconds.do(check_disk)

while True:
    schedule.run_pending()