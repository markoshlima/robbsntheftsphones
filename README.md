# **Introduction**

The project aims to create an algorithm or Machine Learning model to predict robberies and thefts in the city of São Paulo based on the profile, cell phone brand and destination location that the user will frequent, the idea is that if the robbery or theft occurs, have the probability of the places where the crime could occur. The intention is also to make the model available on the web so that anyone can enter the values and bring the probability online. The data was collected on the website of the public security department of the state of São Paulo.

# **Notebook to create the model**

To arrive at this model for predicting cell phone robbery and theft in the city of São Paulo, it was necessary to previously obtain the data from the website of the public security department of the state of São Paulo.
To carry out the data study, transformation, training and model generation, Jupyter Lab's Jupyter Notebook in version 4.0.5 was used and [this link contains the notebook used to create the model] (https://raw.githubusercontent.com/markoshlima/robbsntheftsphones/main/notebooks/celulares-roubo-furto.ipynb).

This site was built using [GitHub Pages].

**Architecture**

![alt text](https://raw.githubusercontent.com/markoshlima/robbsntheftsphones/main/doc/architecture.png)

In order to make the model available so that anyone can access the project, the model was packaged using Docker and published on the AWS Cloud Provider.
A static website was created to receive the parameters and show the results to users, the service to publish was the S3 Static Site, the endpoint was inserted into the AWS API Gateway. A Virtual Private Cloud (VPC) and a public Subnet were created to receive restricted services, a Load Balancer and an ECS container orchestrator were published in it, where the model will be located. Still within AWS, container versions are published in ECR (Elastic Container Service).

**Results**

In the figure below we have the 6 main features to be selected by the user. When the user clicks on Predict, the endpoint (API Gateway) is activated, which forwards the request to a Load Balancer, which in turn redirects to a container orchestrator (ECS) task, where we arrive at inference and the final result. is returned to the customer.

![alt text](https://raw.githubusercontent.com/markoshlima/robbsntheftsphones/main/doc/print1.png)

In the figure below we can see the results of the 10 classes and each one with its respective probability where robbery and robbery can occur for that profile.

![alt text](https://raw.githubusercontent.com/markoshlima/robbsntheftsphones/main/doc/print2.png)

# Addition Information & Setup

- The backend: `myflix-hexagonal`is used to create all data in AWS Dynamodb and the backend rules.
- The folder `graphql-config` there is the schema.graphql that could be used inside AWS AppSync
- Also the same folder, there are the resolvers that could be used in the AWS tool as well
- It is needed to created the dynamodb connectors
- The folder `IaaC` there is the the infraestructure code to S3, ECS.