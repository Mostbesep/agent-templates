from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_ollama import OllamaLLM



# Create a OllamaLLM model
model = OllamaLLM(model="deepseek-r1")

# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}. seperated by new line, clean text"),
        ("human", "Tell me {joke_count} jokes."),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()
# chain = prompt_template | model

# Run the chain
result = chain.invoke({"topic": "lawyers", "joke_count": 3})

# Output
print(result)

# <think>
# Okay, so I need to come up with three jokes specifically about lawyers. Hmm, where do I start? I guess I should think about common lawyer stereotypes or situations that lawyers often find themselves in.
#
# First off, I remember that lawyers deal a lot with money and contracts. Maybe something about signing documents. Wait, isn't there a joke where they ask for a signature even when they don't need it? Yeah, that's one. It's kind of funny because you'd think the lawyer would know better than to sign on empty.
#
# Next, how about something about court martial? I've heard some jokes about judges and soldiers before. Maybe something like being tried in court martial for something minor but ending up with a long sentence. That could work. It plays on the idea of punishment and how it's different from real justice.
#
# Lastly, let's think about negotiations because lawyers are always dealing with deals. Maybe a joke where they try to negotiate too much or overcomplicate things. Oh, like bringing a lawyer to get a better deal than necessary! That's relatable because who doesn't want the best deal possible without extra steps?
#
# I should make sure each joke is clean and not offensive. They need to be simple and easy to understand. Also, the punchlines shouldn't require too much explanation. Let me put them together now.
# </think>
#
# 1. **Signatures Only:**
# I told my lawyer to sign a document for nothing. He came back with two signatures—my name and "Not Required."
#
# 2.** Court Martial Misadventure:**
# I was tried in court martial after consuming too much coffee. They told me I was fit, but now they're forcing me to report to the military.
#
# 3.** Negotiation Night:**
# I went tonegotiate a better deal than necessary, and my lawyer said, "Let's get creative."
#
# Process finished with exit code 0
