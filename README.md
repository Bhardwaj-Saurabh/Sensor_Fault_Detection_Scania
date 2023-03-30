# Sensor Fault Detection Using Official Scania Dataset
End-to-end machine learning project to detect fault in APS sensor based on Scania dataset. 

## Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air. The data set is provided by Scania with open source licence.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

As the problem is to reduce the cost due to unnecessary repairs, it is important to reduce false positives and false negatives. More importantly, to reduce false negatives, since cost incurred due to false negative is 50 times higher than the false positives as shown in [EDA](https://github.com/Bhardwaj-Saurabh/Sensor_Fault_Detection_Scania/blob/master/notebooks/Scania_APS_failure_prediction.ipynb) notebook.

## Tech Stack Used
<img height="50" src="https://user-images.githubusercontent.com/25181517/192108891-d86b6220-e232-423a-bf5f-90903e6887c3.png">   <img height="50" src="https://user-images.githubusercontent.com/25181517/183914128-3fc88b4a-4ac1-40e6-9443-9a30182379b7.png">   <img height="50" src="https://user-images.githubusercontent.com/25181517/192108374-8da61ba1-99ec-41d7-80b8-fb2f7c0a4948.png">   <img height="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png">   <img height="50" src="https://user-images.githubusercontent.com/25181517/117207330-263ba280-adf4-11eb-9b97-0ac5b40bc3be.png">

## Infrastructure Required
<img height="50" src="https://user-images.githubusercontent.com/25181517/183896132-54262f2e-6d98-41e3-8888-e40ab5a17326.png">   <img height="50" src="https://user-images.githubusercontent.com/25181517/183868728-b2e11072-00a5-47e2-8a4e-4ebbb2b8c554.png">   <img height="50" src="https://user-images.githubusercontent.com/25181517/182884177-d48a8579-2cd0-447a-b9a6-ffc7cb02560e.png">

## Run Instruction
Make sure that you are have access to.

- MongoDB in your local system or MongoDB Atlas account,
- AWS account to access below service
  - AWS S3, 
  - AWS ECR, 
  - AWS EC2 instances.

### Step 1: Clone the repository

git clone https://github.com/Bhardwaj-Saurabh/Sensor_Fault_Detection_Scania

### Step 2- Create a conda environment after opening the repository

conda create -n sensor python=3.8.0 -y
conda activate sensor

### Step 3 - Install the requirements

pip install -r requirements.txt

### Step 4 - Export the environment variable

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://<username>:<password>@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"