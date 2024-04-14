from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from FYP import dbsearch_module

def fewshots():
    from langchain.tools.retriever import create_retriever_tool

    connection = dbsearch_module.create_connection("fewshots")
    few_shots = dbsearch_module.select_query("SELECT * from fewshotexamples;", connection)

    few_shot_docs = [
        Document(page_content=question, metadata={"sql_query": few_shots[question]})
        for question in few_shots.keys()
    ]
    embeddings = OpenAIEmbeddings(openai_api_key="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")
    vector_db = FAISS.from_documents(few_shot_docs, embeddings)
    retriever = vector_db.as_retriever()

    tool_description = """
    This tool will help you understand similar examples to adapt them to the user question.
    If possible, invoke the database query as-is directly from the similar examples.
    Input to this tool should be the user question.
    """

    retriever_tool = create_retriever_tool(
        retriever, name="sql_get_similar_examples", description=tool_description
    )
    custom_tool_list = [retriever_tool]
    return custom_tool_list

def propernounsearchtool():
    from langchain.tools.retriever import create_retriever_tool
    connection = dbsearch_module.create_connection("fewshots")
    propernounlist = dbsearch_module.select_query_list("SELECT * from propernouns;", connection)
    print(propernounlist)
    vector_db = FAISS.from_texts(propernounlist, OpenAIEmbeddings(openai_api_key="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"))
    retriever = vector_db.as_retriever(search_kwargs={"k": 5})
    description = """Use to look up values to filter on. Input is an approximate spelling of the proper noun, output is \
    valid proper nouns. Use the noun most similar to the search."""
    retriever_tool = create_retriever_tool(
    retriever,
    name="search_proper_nouns",
    description=description,
    )
    return retriever_tool

def createsqlagentwithtools(custom_tool_list):
    from langchain.agents import AgentType, create_sql_agent
    from langchain_community.agent_toolkits import SQLDatabaseToolkit
    from langchain_community.utilities import SQLDatabase
    from langchain_openai import ChatOpenAI

    db = SQLDatabase.from_uri("postgresql://postgres:postsuperzax@localhost:5432/osm2pgsqldb")
    llm = ChatOpenAI(temperature=0, openai_api_key="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", model_name="gpt-4")
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    custom_suffix = """
    I should first get the similar examples I know after checking that the proper nouns are spelled correctly.
    If the examples are enough to construct the query, I can build it. I will not copy the example directly, but adapt the example to fit the user question.
    Otherwise, I can then look at the tables in the database to see what I can query.
    Then I should query the schema of the most relevant tables
    """

    prefix_template = """You are an agent designed to interact with a SQL database.

    You will ALWAYS search for my search_proper_nouns tool that works.

    You will ALWAYS combine the output from my search_proper_nouns tool that works into a string.

    You will ALWAYS adapt the example from my sql_get_similar_examples tool to fit the user question.

    DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

    If the question does not seem related to the database, just return "I do not know" as the answer.
    """

    agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    # agent_executor_kwargs={"return_intermediate_steps": True},
    prefix=prefix_template,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    extra_tools=custom_tool_list,
    suffix=custom_suffix,
    )

    return agent