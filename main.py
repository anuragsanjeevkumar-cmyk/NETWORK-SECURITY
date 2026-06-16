from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging
from Networksecurity.entity.config_entity import DataIngestionConfig
from Networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()

        # Create an instance, not the class itself
        data_ingestion_config = DataIngestionConfig(
            training_pipeline_config=training_pipeline_config
        )

        data_ingestion = DataIngestion(data_ingestion_config)

        logging.info("Initiate the data ingestion")

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        print(data_ingestion_artifact)

    except Exception as e:
        import traceback

        print("\n=== ORIGINAL ERROR ===")
        print(type(e).__name__)
        print(e)
        traceback.print_exc()