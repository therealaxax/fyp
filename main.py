import dbsearch_module
import sqlagent_module
import sqlagentwithtools_module

# database = 'nyc'
# connection = dbsearch_module.create_connection(database)
# x = input('press to continue')

# sql = 'SELECT * FROM nyc_neighborhoods'

# This query retrieves all table names
# sql = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog'AND schemaname != 'information_schema' AND tablename != 'spatial_ref_sys' AND tablename != 'geometries';"
# print(dbsearch_module.select_query(sql, connection)[0][0])
# print(dbsearch_module.select_query(sql, connection))

################################################################################################################

# agent_executor = sqlagent_module.createsqlagent()
# agent_executor.run("What neighborhood is the 'Broad St' station in?")
# agent_executor.run("Using the nyc_neighborhoods table and other tables, what neighborhood is the 'Broad St' station in?")
# agent_executor.run("What neighborhood is the 'Broad St' station in?")

################################################################################################################

# We can try to use these example queries to explore finding mispellings in proper nouns to use as column filters

# This query produces an error because it generates the query 'SELECT ST_Length(geom) FROM nyc_streets WHERE streetname = 'Walsh Ct' LIMIT 10' but streetname is not in the table
# agent_executor.run("What is the length of the street 'Walsh Ct'?")

# No error with this query
# agent_executor.run("What is the length of the street with name 'Walsh Ct'?")

################################################################################################################

# We can use these example queries to explore the inclusion of few-shot examples

# Correct result
# agent_executor.run("What is the length of the street with name 'Walsh Ct'?")

# Wrong result
# agent_executor.run("How long is 'Walsh Ct'?")

################################################################################################################

custom_tool_list = sqlagentwithtools_module.fewshots()
# custom_tool_list.append(sqlagentwithtools_module.propernounsearchtool(["Brooklyn"],["Staten Island"]))
# print(custom_tool_list)
agent_executor = sqlagentwithtools_module.createsqlagentwithtools(custom_tool_list)
# print(agent_executor)
# agent_executor.run("How long is 'Walsh Ct'?")
# agent_executor.run("How long is 'Avenue O'?")
# agent_executor.run("How many homicides are there in 'Sten Iand'?")
# agent_executor.run("How many buildings are there in 'Tiong Bahru'?")
agent_executor.run("Where is Tekka Centre located?")