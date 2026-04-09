{
  "Comment": "A description of my state machine",
  "StartAt": "Glue StartJobRun",
  "States": {
    "Glue StartJobRun": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun",
      "Parameters": {
        "JobName": "new_job",
        "Arguments": {
          "--date.$": "$.date"
        }
      },
      "Catch": [
        {
          "ErrorEquals": [
            "States.ALL"
          ],
          "Next": "Failure Lambda Invoke"
        }
      ],
      "Next": "Success Lambda Invoke"
    },
    "Success Lambda Invoke": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "success_lambda"
      },
      "End": true
    },
    "Failure Lambda Invoke": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "failure_lambda"
      },
      "End": true
    }
  }
}