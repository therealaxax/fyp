# IMPORTANT: USE THESE VERSIONS:
# !pip install langchain==0.0.316
# langchain version 0.0.353 seems to work as well
# !pip install openai==0.28.1
# pip show langchain will show the langchain version

from langchain.agents import create_sql_agent

# from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI

def createsqlagent():
    db = SQLDatabase.from_uri("postgresql://postgres:postsuperzax@localhost:5432/nyc")
    # db = SQLDatabase.from_uri("postgresql://postgres:postsuperzax@localhost:5432/anotherlocationtestdb")
    # print(type(db))
    llm = OpenAI(temperature=0, openai_api_key="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", model="gpt-3.5-turbo-instruct")

    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=SQLDatabaseToolkit(db=db, llm=llm),
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

    return agent_executor