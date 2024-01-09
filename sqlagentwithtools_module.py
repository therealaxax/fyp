from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

def fewshots():
    # from langchain.agents.agent_toolkits import create_retriever_tool
    # from langchain_community.agent_toolkits import create_retriever_tool
    from langchain.tools.retriever import create_retriever_tool

    few_shots = {"Find the length of the street with name 'Walsh Ct'." : " SELECT ST_Length(geom) FROM nyc_streets WHERE name = 'Walsh Ct'; "}

    few_shot_docs = [
        Document(page_content=question, metadata={"sql_query": few_shots[question]})
        for question in few_shots.keys()
    ]
    embeddings = OpenAIEmbeddings(openai_api_key="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")
    vector_db = FAISS.from_documents(few_shot_docs, embeddings)
    retriever = vector_db.as_retriever()

    tool_description = """
    This tool will help you understand similar examples to adapt them to the user question.
    Input to this tool should be the user question.
    """

    retriever_tool = create_retriever_tool(
        retriever, name="sql_get_similar_examples", description=tool_description
    )
    custom_tool_list = [retriever_tool]
    return custom_tool_list

def createsqlagentwithtools(custom_tool_list):
    from langchain.agents import AgentType, create_sql_agent
    # from langchain.agents.agent_types import AgentType
    # from langchain.agents import create_sql_agent
    # from langchain.agents.agent_toolkits import SQLDatabaseToolkit
    from langchain_community.agent_toolkits import SQLDatabaseToolkit
    from langchain_community.utilities import SQLDatabase
    # from langchain.utilities import SQLDatabase
    from langchain_openai import ChatOpenAI
    # from langchain.llms import OpenAI

    db = SQLDatabase.from_uri("postgresql://postgres:postsuperzax@localhost:5432/nyc")
    # db = SQLDatabase.from_uri("postgresql://postgres:postsuperzax@localhost:5432/anotherlocationtestdb")
    # print(type(db))
    # llm = OpenAI(temperature=0, openai_api_key="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", model="gpt-3.5-turbo-instruct")
    llm = ChatOpenAI(temperature=0, openai_api_key="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", model_name="gpt-4")
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    custom_suffix = """
    I should first get the similar examples I know.
    If the examples are enough to construct the query, I can build it.
    Otherwise, I can then look at the tables in the database to see what I can query.
    Then I should query the schema of the most relevant tables
    """

    agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    extra_tools=custom_tool_list,
    suffix=custom_suffix,
    )

    return agent