# Deploy Deep Learning CNN using Azure Machine Learning
## Overview
In this repository there are a number of tutorials in Jupyter notebooks that have step-by-step instructions on how to deploy a pretrained deep learning model on a GPU enabled Kubernetes cluster throught Azure Machine Learning (AzureML). The tutorials cover how to deploy models from the following deep learning frameworks on specific deployment target:

- [Deploy Keras(TensorFlow) model on Azure Kubernetes Service (AKS) Cluster with GPUs](Keras_Tensorflow)
- [Deploy FastAI model using CVBP model on Azure Kubernetes Service (AKS) Cluster with GPUs](cvbp)


![alt text](https://happypathspublic.blob.core.windows.net/aksdeploymenttutorialaml/example.png "Example Classification")
 
 For each framework, we go through the following steps:
 * Create an AzureML Workspace
 * Model development where we load the pretrained model and test it by using it to score images
 * Develop the API that will call our model 
 * Building the Docker Image with our REST API and model and testing the image
 * AKS option
     * Creating our Kubernetes cluster and deploying our application to it
     * Testing the deployed model
     * Testing the throughput of our model
     * Cleaning up resources
 
## Design

As described on the associated [Azure Reference Architecture page](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/ai/realtime-scoring-python), the application we will develop is a simple image classification service, where we will submit an image and get back what class the image belongs to. The application flow for the deep learning model is as follows:
1)	Deep learning model is registered to AzureML model registry.
2)	AzureML creates a docker image including the model and scoring script.
3)	AzureML deploys the scoring image on the chosen deployment compute target (AKS or IoT Edge) as a web service.
4)	The client sends a HTTP POST request with the encoded image data.
5)	The web service created by AzureML preprocesses the image data and sends it to the model for scoring.
6)	The predicted categories with their scores are then returned to the client.


**Deploying with GPUS:** For a detailed comparison of the deployments of various deep learning models, see the blog post [here](https://azure.microsoft.com/en-us/blog/gpus-vs-cpus-for-deployment-of-deep-learning-models/) which provides evidence that, at least in the scenarios tested, GPUs provide better throughput and stability at a lower cost.



# Getting Started

To get started with the tutorial, please proceed with following steps **in sequential order**.

 * [Prerequisites](#prerequisites)
 * [Setup](#setup)


<a id='prerequisites'></a>
## Prerequisites
1. Linux (x64) with GPU enabled.
2. [Anaconda Python](https://www.anaconda.com/download)
3. [Docker](https://docs.docker.com/v17.12/install/linux/docker-ee/ubuntu) installed.
4. [Azure account](https://azure.microsoft.com).

The tutorial was developed on an [Azure Ubuntu
DSVM](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro),
which addresses the first three prerequisites.

<a id='setup'></a>
## Setup
To set up your environment to run these notebooks, please follow these steps.  
1. Clone the repo
```bash
git clone https://github.com/msalvaris/aksdemo
```

2. Follow the instructions for your chosen framework
  - [Keras(TensorFlow)](Keras_Tensorflow/README.md)
  - [CVBP](cvbp/README.md)

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.