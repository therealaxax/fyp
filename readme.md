Instructions:

Dependencies: PostgreSQL with PostGIS, langchain, OpenAI API, sqlalchemy, geopandas (installed using conda), python

geopandas was installed in a conda env, remember to run "conda activate env_name", in my directory, env_name is called geoenv

Then you can run the program(s) using python

Remember to set the environment variables to be able to use conda from cmd.exe too

IMPORTANT
RUN ON THESE VERSIONS
langchain version 0.0.353
openai version 1.7.0
langchain-openai version 0.0.2

IF THE CODE BREAKS AT ANY OF THESE PARTS, PIP INSTALL THE CORRECT VERSIONS TO SEE IF IT RESOLVES
e.g. pip install langchain==0.0.353

"# fyp"

# FYP Project

## Introduction

The advent of ChatGPT and other Large Language Models in recent years has caused a surge in popular interest in Artificial Intelligence and its capabilities. Although Large Language Models may seem capable of an endless variety of tasks, there are still areas it struggles in such as the hallucination problem or in its understanding of non-textual data, like geospatial data. This project seeks to address this issue by exploring methodologies for Large Language Models to interpret and use geospatial data more accurately, and to develop an easily operable workflow that uses PostGIS and LangChain, among other technologies. This workflow will be grounded in theoretical concepts like few-shot learning. An application user interface incorporating this workflow will be built in Flask, and it is hoped that the results presented here will be useful for the future development of software wishing to best utilize Large Language Models for processing geospatial data.

This project was built in Windows and is written in Python with HTML and CSS used for the user interface.

## Setting Up Dependencies

1. Setup a PostgreSQL database and install the PostGIS extension. Remember to enable the PostGIS extension as well if necessary. Refer to https://postgis.net/documentation/getting_started/#installing-postgis

2. It is recommended to use conda for managing dependencies. Install conda following the instructions at https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html This Anaconda Distribution installer was used for this project.

3. Create a new conda environment. 'geoenv' in the command below denotes the name of the environment.
   `conda create -n geoenv`

4. Activate the conda environment.
   `conda activate geoenv`

5. Install geopandas. https://geopandas.org/en/stable/getting_started/install.html The command below installs geopandas via the conda-forge channel.
   `conda install --channel conda-forge geopandas`

6. Install the rest of the dependencies into the same conda environment.
   `pip install psycopg2`  
   `pip install Flask`  
   `pip install langchain==0.0.353`  
   `pip install langchain_community==0.0.10`  
   `pip install openai==1.7.0`  
   `pip install langchain_openai==0.0.2`

## Running The Project

1. git clone this project

2.
