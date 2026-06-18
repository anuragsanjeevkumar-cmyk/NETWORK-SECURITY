# Network Security Phishing Detection System

## Overview

This project is an End-to-End Machine Learning Pipeline for detecting malicious or phishing network traffic. The system automates data ingestion, validation, transformation, model training, evaluation, experiment tracking, and batch prediction using FastAPI.

## Features

* Data Ingestion from MongoDB
* Data Validation
* Data Transformation & Feature Engineering
* Model Training
* Model Evaluation
* MLflow & DagsHub Experiment Tracking
* FastAPI Deployment
* Batch Prediction using CSV Upload
* Model & Preprocessor Serialization
* Logging and Exception Handling

## Project Structure

```bash
NetworkSecurity/
│
├── Networksecurity/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── batch_prediction.py
│   │
│   ├── entity/
│   ├── constant/
│   ├── exception/
│   ├── logging/
│   └── utils/
│
├── final_model/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── prediction_output/
│   └── output.csv
│
├── templates/
│   └── table.html
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

## Tech Stack

* Python
* Scikit-Learn
* Pandas
* NumPy
* FastAPI
* MongoDB
* MLflow
* DagsHub
* Jinja2
* Uvicorn

## Workflow

1. Data Collection from MongoDB
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Evaluation
6. MLflow Experiment Tracking
7. Model Saving
8. Batch Prediction
9. FastAPI Deployment

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/NETWORK-SECURITY.git
cd NETWORK-SECURITY
```

Create virtual environment:

```bash
python -m venv mvenv
```

Activate environment:

```bash
mvenv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Training Pipeline

Run the training pipeline:

```bash
python main.py
```

Artifacts generated:

```bash
Artifacts/
final_model/model.pkl
final_model/preprocessor.pkl
```

## Running FastAPI

Start API server:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Batch Prediction

1. Open Swagger UI
2. Use `/predict` endpoint
3. Upload CSV file
4. Download prediction results

Output file:

```text
prediction_output/output.csv
```

## MLflow Tracking

Experiments are tracked using:

* MLflow
* DagsHub

Metrics tracked:

* F1 Score
* Precision
* Recall

## Future Improvements

* Docker Deployment
* AWS S3 Integration
* CI/CD Pipeline
* Model Monitoring
* Real-Time Prediction API

## Author

**Anurag Kumar**

B.Tech AIML | NIET Greater Noida

## License

This project is developed for educational and learning purposes.
