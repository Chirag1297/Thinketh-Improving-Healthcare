# Thinketh-Improving-Healthcare

A decentralised diagnosis platform for every bhamashah id holder.
An innovation which directly provides you an option for appointment booking based on the results of free diagnosis.

# How it works !
The system currently detectes over 40 diseases based on 140 symptoms using a neural network. A decentralized database is created using patients information using Ethereum blockchain and an appointment reciept is generated based on users choice for the nearest specalised doctors.

# Info about Dataset
There are over 4000 data points in the training set. It consists of 0 and 1 values for all the symptoms, and the disease as the label.A dictionary is created to map diseases with a numeric value.A testing set of 40 points is avaliable.A seperate List of diseases and symptoms is also available.

# Disease prediction
It uses an input layer of 132 nodes and output layer of 41 nodes and two hidden layers with 100 and 70 layers respectively.
the net is used to find two most likely diseases.The model was trained in python and the model was exported in javascript.
Neural net can be found in neural-net.py

# Block-chain and Decentralized data
Personal data's security is guaranteed by blockchain as the patient's personal details are hashed cryptographically. So, the meaningful data being useful and the private data is remained secured. Data like address and information about inherited diseases will help mapping diseases with cities. Bhamashah login will gaurentee the integrity of data while being decentralized it also helps in lowering costs for data servers.

# Generated Data
The data stored in blockchain will serve in further improving the accuracy of our model and help it in growing just more than 40 diseases and 130 symptoms. The data will also be made available for lisensing for research purposes.

# Pre-requisites:
1)For using neural network, tensorflow.py is required while tensorflow.js for interacting with model in javascript.
2)To interact with smart contract, metamask plugin should be instaled.
3)To enable metamask and load neural network in javascript, the project firstly should be connected to localhost(private network).
