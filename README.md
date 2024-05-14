Create an Amazon S3 bucket in the same AWS Region as the workflow for your input and output data.

Cross-origin resource sharing (CORS) setting

[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST",
            "DELETE",
            "HEAD"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]



Step 1: Create a Work Team
Open the SageMaker console at https://console.aws.amazon.com/sagemaker/.

In the navigation pane, choose Labeling workforces under Ground Truth.

Choose Private, then choose Create private team.

Choose Invite new workers by email.

Enter an organization name and contact email.

Choose Create private team.

---

Step 2: Create a Human Review Workflow

Open the Augmented AI console at https://console.aws.amazon.com/a2i to access the Human review workflows page.

Select Create human review workflow.

In Workflow settings, enter a workflow Name, S3 bucket, and the IAM role that you created for this tutorial, with the AWS managed policy AmazonAugmentedAIIntegratedAPIAccess attached.

For Task type, select Textract – Key-value pair extraction or Rekognition – Image moderation.

---

1. Select Trigger a human review for specific form keys based on the form key confidence score or when specific form keys are missing.

2. For Key name, enter Mail Address.

3. Set the identification confidence threshold between 0 and 99.

4. Set the qualification confidence threshold between 0 and 99.

5. Select Trigger a human review for all form keys identified by Amazon Textract with confidence scores in a specific range.

6. Set the identification confidence threshold between 0 and 90.

7. Set the qualification confidence threshold between 0 and 90.

Under Worker task template creation, select Create from a default template.

Enter a Template name.

In Task description field, enter the following text:

Read the instructions carefully and complete the task.

Under Workers, select Private.

Select the private team that you created.

Choose Create.


---

Step 3: Start a Human Loop

use the python code to start Human loop

---

Step 4: View Human Loop Status in Console

work on the task

---

Step 5: Download Output Data






