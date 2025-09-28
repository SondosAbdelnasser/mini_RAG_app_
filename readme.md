mini-rag
This is a minimal implementation of the RAG model for question answering.

Requirements
Python 3.8 or later
Install Python using MiniConda
Download and install MiniConda from here
Create a new environment using the following command:
$ conda create -n mini-rag python=3.8
Activate the environment:
$ conda activate mini-rag
(Optional) Setup you command line interface for better readability
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
Installation
Install the required packages
$ pip install -r requirements.txt
Setup the environment variables
$ cp .env.example .env