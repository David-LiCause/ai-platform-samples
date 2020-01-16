# Online Prediction with scikit-learn and Custom Routines

## Overview

In this tutorial, we go over the steps to deploy a model trained with scikit-learn to AI-Platform.
We will be using the model that was trained using custom routines. We will deploy the model and pass
the custom routine package alongside the model object.
Finally, we will then use the deployed model to make some predictions.
Optionally, we will delete the resources created in this sample.

## Prerequisites

* Complete the [training tutorial with custom routines](../../../../training/sklearn/structured/custom_routines).
* Change the directory to this sample and run `python setup.py install`.

## Sample Structure

* [scripts](./scripts) directory: command-line scripts to train the model locally or on AI Platform.
  * [deploy.sh](./scripts/deploy.sh) creates a model resource, and a model version for the newly trained model.
  * [cleanup.sh](./scripts/cleanup.sh) deletes all the resources created in this tutorial.
* [prediction](./prediction) contains the Python sample code to invoke the model for prediction.
  * [predict.py](./prediction/predict.py) invokes the model for making predictions.
* [setup.py](./setup.py): installs all the required Python packages for this tutorial.


## Running the Sample

After you go over the steps in the prerequisites section, you are ready to run the sample code.
Here are the steps you need to take:

1. Run `source ./scripts/deploy.sh`. This script will create a Model Resource in AI-Platform.
It will then deploy the model object which was created in the training sample as a new model
with an assigned model version.
Note that we are passing the custom routine package as we deploy the model using the 
environment variable `CUSTOM_ROUTINE_PATH` which was created by the [training sample](../../../../training/sklearn/structured/custom_routines).

2. Once the model is deployed, you may use it to make predictions - run 
`python ./prediction/predict.py`. This sample code sends a prediction request for two 
instances and prints the result to the console.

3. You may want to delete the resources you created in this tutorial --
run `source ./scripts/cleanup.sh` which deletes the model version and resouce, and also
the model object from GCS.
