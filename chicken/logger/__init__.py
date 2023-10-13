import logging  
import sys 
import os 
from datetime import datetime
logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"
log_dir_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

log_dir = "logs"
log_filepath = os.path.join(log_dir, log_dir_name)

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level = logging.INFO, 
                    format = logging_str, 
                    handlers=[logging.FileHandler(log_filepath),
                              logging.StreamHandler(sys.stdout) 
                              ]
)

logger = logging.getLogger("chickenlogger")