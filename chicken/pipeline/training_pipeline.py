from chicken.config.config import *
from chicken.components.data_ingestion import *
from chicken.logger import logger

Stage_name = "Data Ingestion Stage"


class DataIngestionTrainingPipeline():
    def __init__(self):
        pass 
    def main(self):
        try:
            logger.info(f"started the ingestion process")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e