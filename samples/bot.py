import json
import os
import uuid
import openai
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import (
    ConversationBufferWindowMemory,
    ConversationSummaryMemory,
    ConversationEntityMemory,
)
from langchain.memory import CombinedMemory

# read local .env file
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) 

class Bot:
    def __init__(
        self,
        openai_api_key=os.getenv("AZURE_OAI_KEY"),
        openai_api_base=os.getenv("AZURE_OAI_ENDPOINT"),
        openai_api_version="2020-08-01",
        aoai_deplpoyment_name="openai-workshop-deployment-environment",
        aoai_model_name="gpt-35-turbo",
    ):
        openai.api_type = "azure"
        openai.api_base = openai_api_base
        openai.api_version = openai_api_version
        openai.api_key = openai_api_key

        # The model
        self.llm = AzureOpenAI(
            deployment_name=aoai_deplpoyment_name,
            model_name=aoai_model_name,
            openai_api_key=openai_api_key,
        )
        self.conversations = {}

    # Internal function to create a new conversation, UID as argument
    def _create_conversation(self, conversation_id):
        # Memory
        conv_memory = ConversationBufferWindowMemory(k=4, input_key="input")

        ent_memory = ConversationEntityMemory(
            llm=self.llm,
            input_key="input",
        )

        summary_memory = ConversationSummaryMemory(
            llm=self.llm, memory_key="summary", input_key="input"
        )

        # Combined
        memory = CombinedMemory(memories=[conv_memory, summary_memory, ent_memory])
        TEMPLATE = """
		The following is a friendly conversation between a human and an AI.
        The AI is talkative and provides lots of specific details from its context.
        If the AI does not know the answer to a question, it truthfully says it does not know.

		Context:
		{entities}

		Summary of conversation:
		{summary}

		Last 3 lines of conversation:
		{history}
		Human: {input}
		AI:
		"""
        PROMPT = PromptTemplate(
            input_variables=["summary", "history", "entities", "input"],
            template=TEMPLATE,
        )
        self.conversations[conversation_id] = ConversationChain(
            llm=self.llm,
            # verbose=True,
            memory=memory,
            prompt=PROMPT,
        )

    def generate_response(self, conversation_id: str | None, user_input: str):
        # Create a new conversation if it does not exist
        if conversation_id is None:
            # Create a new GUID
            conversation_id = str(uuid.uuid4())
            self._create_conversation(conversation_id)
        if conversation_id not in self.conversations:
            response = "Sorry, I don't remember you. Let's start over."
        else:
            response = self.conversations[conversation_id].predict(input=user_input)
        # Generate a response to the user input
        return conversation_id, response


if __name__ == "__main__":
    # Load the config
    with open("settings.json", "r") as f:
        settings = json.load(f)
    with open("secrets.json", "r") as f:
        secrets = json.load(f)
    # Create the bot
    bot = Bot(**secrets, **settings)
    # Generate a response
    conversation_id, response = bot.generate_response(None, "Hello! How are you?")
    print(conversation_id, response)
