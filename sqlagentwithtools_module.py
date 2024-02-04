from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

def fewshots():
    # from langchain.agents.agent_toolkits import create_retriever_tool
    # from langchain_community.agent_toolkits import create_retriever_tool
    from langchain.tools.retriever import create_retriever_tool

    # few_shots = {"Find the length of the street with name 'Walsh Ct'." : " SELECT ST_Length(geom) FROM nyc_streets WHERE name = 'Walsh Ct'; "}
    few_shots = {"How many buildings are there in 'Tiong Bahru'?" : " select building, name, way from planet_osm_polygon where building != 'null' and name like '%Tiong Bahru%'; ",
    "Where is the National Cancer Centre Singapore located?" : """SELECT name, ST_AsText(way) as coordinates
    FROM planet_osm_polygon AS outer_poly
    WHERE ST_Contains(outer_poly.way, (
        SELECT way 
        FROM planet_osm_polygon 
        WHERE name = 'National Cancer Centre Singapore' 
        ORDER BY way_area DESC 
        LIMIT 1
    ));"""}

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

# Use an SQL query to retrieve proper nouns from tables, and pass them into the propernounlists.
# TODO: Write this SQL query in the dbsearch_module.
# propernounsearchtool returned is to be appended to the custom_tool_list
def propernounsearchtool(propernounlist1, propernounlist2):
    from langchain.tools.retriever import create_retriever_tool
    vector_db = FAISS.from_texts(propernounlist1 + propernounlist2, OpenAIEmbeddings(openai_api_key="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"))
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
    # from langchain.agents.agent_types import AgentType
    # from langchain.agents import create_sql_agent
    # from langchain.agents.agent_toolkits import SQLDatabaseToolkit
    from langchain_community.agent_toolkits import SQLDatabaseToolkit
    from langchain_community.utilities import SQLDatabase
    # from langchain.utilities import SQLDatabase
    from langchain_openai import ChatOpenAI
    # from langchain.llms import OpenAI

    # db = SQLDatabase.from_uri("postgresql://postgres:postsuperzax@localhost:5432/nyc")
    db = SQLDatabase.from_uri("postgresql://postgres:postsuperzax@localhost:5432/osm2pgsqldb")
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

    # custom_suffix = """
    # You are an agent designed to interact with a SQL database.
    # DO NOT check their schemas to understand their structure.
    # You do not care about the database schema.
    # You will ALWAYS search for my search_proper_nouns tool that works.
    # You will ALWAYS combine the output from my search_proper_nouns tool that works into a string.
    # You should first get the similar examples you know.
    # If the examples are enough to construct the query, you can build it.
    # DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
    # If the question does not seem related to the database, just return "I do not know" as the answer.
    # """

    # prefix_template = """You are an agent designed to interact with a SQL database.

    # DO NOT check their schemas to understand their structure.

    # You do not care about the database schema.

    # You will ALWAYS search for my search_proper_nouns tool that works.

    # You will ALWAYS combine the output from my search_proper_nouns tool that works into a string. Create a short rhyme with the output and this will be your final answer.

    # DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

    # If the question does not seem related to the database, just return "I do not know" as the answer.
    # """

    prefix_template = """You are an agent designed to interact with a SQL database.

    You will ALWAYS search for my search_proper_nouns tool that works.

    You will ALWAYS combine the output from my search_proper_nouns tool that works into a string.

    DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

    If the question does not seem related to the database, just return "I do not know" as the answer.
    """

    agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    prefix=prefix_template,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    extra_tools=custom_tool_list,
    suffix=custom_suffix,
    )

    return agent