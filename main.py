from src.configuration.mongo_db_connection import MongoDBClient
from src.exception import CustomException
import os
import sys
from src.logger import logging
from src.pipeline import training_pipeline
from src.pipeline.training_pipeline import TrainingPipeline
from src.utils.main_utils import read_yaml_file


def main():
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)


if __name__ == "__main__":
    main()
