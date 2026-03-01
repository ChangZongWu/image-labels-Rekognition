# Image Labels Generator (AWS Rekognition + S3)

Generate labels (with confidence scores) for images stored in an S3
bucket using Amazon Rekognition. Displays bounding boxes for detected
objects.

## Architecture Flow

1)  Upload image to S3\
2)  Rekognition DetectLabels\
3)  Python processes response\
4)  Display labels + bounding boxes

## Tech Stack

-   AWS S3
-   AWS Rekognition
-   IAM
-   AWS CLI
-   Python (boto3, Pillow, matplotlib)

## Setup

### 1. Clone the repository

git clone `<your-repo-url>`{=html} cd `<your-repo-folder>`{=html}

### 2. Create virtual environment (Windows)

python -m venv venv venv`\Scripts`{=tex}`\activate`{=tex}

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure AWS CLI

aws configure

Make sure: Region: us-east-2 Output: json

Verify: aws sts get-caller-identity

## Usage

Edit rekognition_labels.py: bucket = "your-bucket-name" photo =
"your-image.jpg"

Run: python rekognition_labels.py

## Project Structure

. ├─ rekognition_labels.py ├─ requirements.txt ├─ README.md └─
.gitignore

## Notes

-   Use JPG or PNG images (WEBP/AVIF may fail)
-   Ensure IAM permissions include Rekognition and S3 access
