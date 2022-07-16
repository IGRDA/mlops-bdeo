# mlops


## CHALLENGE: Create needed resources/files to deploy this model in production

It is not necessary to deploy anything from this code in a cloud environment (Demo or Video-demo is optional). We just
want to know how you implement every aspect we requiere and the quality of the implementation and code structure.

Imagine that you have got this model from Data Scientists and you have to deploy this model in production. What would
you implement to deploy this model? Please remind that in real world this code has to be maintainable, the model has
to pass all tests and be deployed in production automatically.

If you want to explain any aspect of your code/implementation please feel free adding descriptions in README.md

Mandatory Requirements:

1. Containerization (Docker, LXC...) (Docker,ECR (Elastic Container Registry) )
2. Unit Tests  (tests/unit/* , ci/cd pipelines using GitHub actions)
2. CI/CD (GitLab, GitHub, Jenkins, Travis...) (GitHub, GitHub-actions, SonarCloud)
3. IaC (CDK, Terraform, Ansible...) (Cloudformation)
4. Documentation (At least in functional/productive code)

Optional requirements:

- If you want, you can use python package managers such as pipenv, poetry or virtualenv (docker and usual requirements.txt)
- Suppose that the model inference call comes from backend, so you can choose either synchronous or asynchronoun communication (fifo and async queues)
- You can use a sentry-like application monitoring (Alarms in AWS Cloudwatch...) (Cloudwatch metrics and dashboards)
- Persistent data is optional, if you want to save the model events/results in a database (dynamo table)



CLOUDWATCH METRICS AND DASHBOARDS
Add dvc (data version control), mlflow (reproducibilty) tensorflow exended data drift concept drift, tensorboard, explainability, model dashboard againts control grous
Ab testing
Block pushes to repo
Integration tests con mocks
Externalizar bucket, cuenta

Mejorar pytest y añadir distintos casos
Cloudwatch dashboard

Limpiar codigo y repo
quitar acount id
solve signed commits

Create custom metrics to new alarms
Create mixed metrics
Seccurity issues (Rols)
Externalize variables
Clean code