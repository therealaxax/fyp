# FYP Project

## Introduction

The advent of ChatGPT and other Large Language Models in recent years has caused a surge in popular interest in Artificial Intelligence and its capabilities. Although Large Language Models may seem capable of an endless variety of tasks, there are still areas it struggles in such as the hallucination problem or in its understanding of non-textual data, like geospatial data. This project seeks to address this issue by exploring methodologies for Large Language Models to interpret and use geospatial data more accurately, and to develop an easily operable workflow that uses PostGIS and LangChain, among other technologies. This workflow will be grounded in theoretical concepts like few-shot learning. An application user interface incorporating this workflow will be built in Flask, and it is hoped that the results presented here will be useful for the future development of software wishing to best utilize Large Language Models for processing geospatial data.

This project was built in Windows and is written in Python with HTML and CSS used for the user interface.

## Database Setup

1. Setup PostgreSQL databases and install the PostGIS extension. Remember to enable the PostGIS extension as well if necessary. Set the user to "postgres", the host to "localhost" and the port number to 5432. Refer to https://postgis.net/documentation/getting_started/#installing-postgis

2. Create 2 databases named "fewshots" and "osm2pgsqldb". There is no need to create any tables in "osm2pgsqldb".

3. In the "fewshots" database, create a table named "fewshotexamples". "fewshotexamples" should have 2 columns named "question" and "query" for containing text data.

4. In the "fewshots" database, create a table named "propernouns". "propernouns" should have 1 column named "propernoun" for containing text data.

## Setting Up Dependencies

1. It is recommended to use conda for managing dependencies. Install conda following the instructions at https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html This Anaconda Distribution installer was used for this project.

2. Create a new conda environment. 'geoenv' in the command below denotes the name of the environment.
   `conda create -n geoenv`

3. Activate the conda environment.
   `conda activate geoenv`

4. Install geopandas. https://geopandas.org/en/stable/getting_started/install.html The command below installs geopandas via the conda-forge channel.
   `conda install --channel conda-forge geopandas`

5. Install the rest of the dependencies into the same conda environment. This project was built using the versions of langchain, langchain_community, openai, and langchain_openai listed in the commands below.
   `pip install psycopg2`  
   `pip install Flask`  
   `pip install langchain==0.0.353`  
   `pip install langchain_community==0.0.10`  
   `pip install openai==1.7.0`  
   `pip install langchain_openai==0.0.2`

6. This project uses the OpenAI "gpt-4" model and requires an OpenAI API key. Details of OpenAI models can be found at https://platform.openai.com/docs/models/overview . Set up an OpenAI API key following the instructions at https://platform.openai.com/docs/quickstart?context=python and note down the key. Note that each API call will be charged by OpenAI.

## Running The Project

The data used in this project is OpenStreetMap data for Malaysia, Singapore, and Brunei. However, it is possible to use geospatial data from other regions, by downloading different data files from the Geofabrik server in step 4.

1. git clone this project

2. In the command line, change the working directory to osm2pgsql. Then inside the osm2pgsql folder, change the working directory to osm2pgsql-bin.

3. Create a new directory folder named osmdata_geofabrik inside the osm2pgsql/osm2pgsql-bin directory folder.

4. Download the data file named "malaysia-singapore-brunei-latest.osm.pbf" from https://download.geofabrik.de/asia/malaysia-singapore-brunei.html into the osmdata_geofabrik directory.

5. In the importdata.py file, change the string of the directory variable to the path of the osm2pgsql-bin folder on the local machine.

6. In dbsearch_module.py, in the create_connection(database) function, change the string of the password variable to the one used for setting up the local PostgreSQL databases.

7. In the sqlagentwithtools_module.py file, change the string of the openai_api_key variable to the OpenAI API key. Do this inside the 3 functions, fewshots(), propernounsearchtool(), and createsqlagentwithtools(custom_tool_list).

8. Change the working directory to the flaskr folder.

9. Run the project with the following command:  
   `flask --app flaskapp.py run --debug`

10. Go to http://127.0.0.1:5000/langchainmodel/input to view the landing site of the project.

## Configuring Few-Shot Examples and Proper Nouns

1. Go to http://127.0.0.1:5000/langchainmodel/dataimportview and click on "Import Data" to import the downloaded OpenStreetMap data for Malaysia, Singapore, and Brunei into the "osm2pgsqldb" database. Note that the database password will have to be entered into the terminal as part of the import process when prompted.

2. Go to http://127.0.0.1:5000/langchainmodel/fewshotsview . Pairs of few-shot example questions and SQL queries can be entered row-by-row on this page. The original pairs of few-shot example questions and SQL queries used can be found from Tables 4 and 5 from this project's report, which is also contained in this git repository. Click "Insert" to perform the insertion.

3. Proper nouns can also be entered one-by-one in http://127.0.0.1:5000/langchainmodel/fewshotsview . The original list of proper nouns used can also be found from Table 6 of this project's report. Click "Insert" to perform the insertion.

4. Natural language questions about the geospatial data can be entered in http://127.0.0.1:5000/langchainmodel/input . The original test cases used are documented in the "Application Testing" section of this project's report.
