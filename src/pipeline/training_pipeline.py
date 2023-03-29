from src.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.components.data_ingestion import DataIngestion
from src.exception import CustomException
from src.logger import logging
import sys


class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion_config=DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting Data Ingestion")

        except Exception as e:
            raise CustomException(e, sys)
        

    def start_data_validation(self)->DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_data_transformation(self)->DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_model_trainer(self)->DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_data_evaluation(self)->DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_model_pusher(self)->DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
        
    def run_pipeline(self)->DataIngestionArtifact:
        try:
            data_ingestion_artifact:DataIngestionArtifact=self.start_data_ingestion()
        except Exception as e:
            raise CustomException(e, sys)
