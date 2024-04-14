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
