### 🚀 A Resume Website with Dynamic Visitor Counter and Serverless Backend API

## 📌 Project Overview

I built a personal resume website and deployed it on AWS to showcase my technical skills, experience, and cloud projects.

The website includes a dynamic visitor counter that displays the total number of visits. I developed a serverless backend API using AWS Lambda and API Gateway, with Amazon DynamoDB storing the visitor count.

Amazon S3 is used to store the website files, while Amazon CloudFront delivers the website securely over HTTPS.

This project helped me gain practical experience in cloud computing, serverless architecture, backend API development, and AWS infrastructure.

## ⚙️ Key Features

- 🌐 Personal resume website hosted on AWS.
- 👨‍💻 Professional profile, skills, and project details.
- 📊 Dynamic visitor counter.
- 🔗 Backend API integration.
- ⚡ Serverless backend using AWS Lambda.
- 🗄️ Visitor data stored in DynamoDB.
- 🔒 Secure HTTPS delivery using CloudFront.

## 🛠️ AWS Services Used

- **Amazon S3:** Stores website files.
- **Amazon CloudFront:** Provides secure and fast website delivery.
- **AWS Lambda:** Handles backend visitor-count logic.
- **Amazon API Gateway:** Creates the backend HTTP API.
- **Amazon DynamoDB:** Stores and updates visitor counts.
- **AWS IAM:** Manages secure service permissions.

## 🔄 How It Works

1. A visitor opens my resume website.
2. CloudFront delivers the website content from Amazon S3.
3. JavaScript sends a request to the API Gateway endpoint.
4. API Gateway triggers the AWS Lambda function.
5. Lambda updates the visitor count in DynamoDB.
6. The updated count is returned through the API.
7. JavaScript displays the visitor count on the website.

## 🎯 Skills Demonstrated

- AWS Cloud Services
- Serverless Architecture
- REST API Integration
- Python and JavaScript
- NoSQL Database Management
- IAM and Cloud Security
- Cloud Deployment and Troubleshooting

