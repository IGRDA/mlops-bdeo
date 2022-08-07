# mlops


## CHALLENGE: Create needed resources/files to deploy this model in production

It is not necessary to deploy anything from this code in a cloud environment (Demo or Video-demo is optional). We just
want to know how you implement every aspect we requiere and the quality of the implementation and code structure.

Imagine that you have got this model from Data Scientists and you have to deploy this model in production. What would
you implement to deploy this model? Please remind that in real world this code has to be maintainable, the model has
to pass all tests and be deployed in production automatically.

If you want to explain any aspect of your code/implementation please feel free adding descriptions in README.md

Mandatory Requirements:

1. Containerization (Docker, LXC...) **(Docker,ECR (Elastic Container Registry) )**
2. Unit Tests **(tests/unit/* , ci/cd pipelines using GitHub actions)**
2. CI/CD (GitLab, GitHub, Jenkins, Travis...) **(GitHub, GitHub-actions, SonarCloud, Gitflow)**
3. IaC (CDK, Terraform, Ansible...) **(Cloudformation)**
4. Documentation (At least in functional/productive code)

Optional requirements:

- If you want, you can use python package managers such as pipenv, poetry or virtualenv **(docker and usual requirements.txt)**
- Suppose that the model inference call comes from backend, so you can choose either synchronous or asynchronoun communication **(fifo and async queues)**
- You can use a sentry-like application monitoring (Alarms in AWS Cloudwatch...) **(Cloudwatch metrics and dashboards)**
- Persistent data is optional, if you want to save the model events/results in a database **(dynamo table)**



### TO DO:

 - General code cleaning
 - Create Mock classes for integration testing external dependencies (example: dynamo).
 - Create IAM Role for the application and developers group with only the permissions needed (Now deploy are made with AWS admin privileges)
 - Add workflow management if application flow gets more complex (Step Functions, Airflow...)
 - Review alarms and subscribe developers chat (slack, teams) to SNS
 - Add PR messages to developers chat
 - Apply MlOps techniques to the repo that generates the model (doubleit_model.pt):
     - Add data version controlo (DVC)
     - Experiment tracking and visualization (MLflow, TensorBoard)
     - Data drift and concept drift alarms (TensorFlow Extended)
     - Model explainability (SHAP, LIME)
     - Model dashboard for performance monitoring against control group (QuickSight)
     - Model AB testing (canary, blue-green)
 - ...
 


### Repo structure

```
├── events
│   ├── event0.json
│   ├── event1.json
│   └── event.json
├── function
│   ├── Dockerfile
│   ├── doubleit_model.pt
│   ├── inference.py
│   ├── __init__.py
│   └── requirements.txt
├── __init__.py
├── README.md
├── samconfig.toml
├── sonar-project.properties
├── template.yaml
└── tests
    ├── __init__.py
    └── unit
        ├── __init__.py
        └── test_handler.py
```
