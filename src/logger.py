import logging
import os
from datetime import datetime

# print("Curr folder : " , os.path.join(os.getcwd(), 'Logs'))

logs_dir_path =  os.path.join(os.getcwd(), 'Logs')
os.makedirs(os.path.join(os.getcwd(), 'Logs'), exist_ok= True)
log_file_format =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_file_path = os.path.join(logs_dir_path,log_file_format)

# print(logs_dir_path)
# print(log_file_path)

logging.basicConfig(
            filename=log_file_path,
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s -  (Line: %(lineno)d) - [%(filename)s]',
            datefmt= "%Y-%m-%d %H:%M:%S"
            )
