from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.components.data_validation import DataValidation
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging
from Networksecurity.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    TrainingPipelineConfig
)

import sys

if __name__ == "__main__":
    try:
        # Training Pipeline Config
        training_pipeline_config = TrainingPipelineConfig()

        # Data Ingestion Config
        data_ingestion_config = DataIngestionConfig(
            training_pipeline_config=training_pipeline_config
        )

        # Data Ingestion
        data_ingestion = DataIngestion(
            data_ingestion_config=data_ingestion_config
        )

        logging.info("Initiating Data Ingestion")

        data_ingestion_artifact = (
            data_ingestion.initiate_data_ingestion()
        )

        logging.info("Data Ingestion Completed")

        print(data_ingestion_artifact)

        # Data Validation Config
        data_validation_config = DataValidationConfig(
            training_pipeline_config=training_pipeline_config
        )

        # Data Validation
        data_validation = DataValidation(
            data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config=data_validation_config
        )

        logging.info("Initiating Data Validation")

        data_validation_artifact = (
            data_validation.initiate_data_validation()
        )

        logging.info("Data Validation Completed")

        print(data_validation_artifact)

    except Exception as e:
        logging.error(str(e))
        raise NetworkSecurityException(e, sys)