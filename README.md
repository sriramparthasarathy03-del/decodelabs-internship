# Project 4 - The Serverless Logic

## Objective

Deploy a serverless calculator using AWS Lambda.

## AWS Service Used

- AWS Lambda

## Runtime

Python 3.x

## Features

- Accepts two numbers
- Performs addition
- Returns JSON output
- No server management required

## Sample Input

```json
{
  "num1": 10,
  "num2": 20
}
```

## Sample Output

```json
{
  "statusCode": 200,
  "body": {
    "Number1": 10,
    "Number2": 20,
    "Result": 30
  }
}
```

## Author

Sriram
