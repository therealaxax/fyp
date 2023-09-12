from langchain.llms import OpenAI
from langchain.schema import HumanMessage
from langchain import OpenAI, SQLDatabase
# from langchain.chat_models import ChatOpenAI

# llm = OpenAI(openai_api_key = "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")
# chat_model = ChatOpenAI(openai_api_key = "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")

# llm.predict("hi!")
# chat_model.predict("hi!")
# text = "What would be a good company name for a company that makes colorful socks?"

# llm.predict(text)
# from langchain.llms import OpenAI
#################################################################
llm = OpenAI(openai_api_key = "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", temperature=0.9)
text = "What would be a good company name for a company that makes colorful socks?"
response = llm(text)
print(response)
#################################################################
# messages = [HumanMessage(content=text)]
# llm.predict_messages(messages)
# print(llm(text))
# llm.predict(text)

exit = input("Press any key to continue")

###############################################

# user inputs a query into the program
# My program takes the query and inputs into the llm
# llm formulates a query to feed into the postgis
# postgis returns a result to the llm
# llm return answer to the user