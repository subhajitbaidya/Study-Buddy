from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from pydantic import BaseModel
import os


class ModelInput(BaseModel):
    model: str
    user_prompt: str


class InvokeModel(ModelInput):

    def Model(self):
        return ChatOllama(
            model=self.model,
            reasoning=False,
            temperature=0.6,
            num_predict=256,
        )

    def getResponse(self) -> str:
        prompt_template = PromptTemplate.from_template(
            "Tell me a sentence about {prompt}"
        )

        chain = prompt_template | self.Model() | StrOutputParser()

        response = chain.invoke({"prompt": self.user_prompt})
        return response

    # def tutor_agent(self) -> str:
    #     llm = self.Model()
    #     tools = load_tools(['wikipedia'], llm=llm)

    #     agent = initialize_agent(
    #         tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True, handle_parsing_errors=True
    #     )

    #     response = agent.run(
    #         f"""You are an AI assistant using the ReAct format. When answering, always use:
    #             Thought: ...
    #             Action: ...
    #             Action Input: ...
    #         {self.user_prompt}"""
    #     )

    #     parser = StrOutputParser()

    #     result = parser.invoke(response)
    #     return result


if __name__ == "__main__":
    load_dotenv()
    m1 = os.getenv('DEEPSEEK')
    m2 = os.getenv('QWEN')

    model_instance = InvokeModel(
        user_prompt="Tigers", model=m1)
    print("deepseek:", model_instance.getResponse())
    print('\n')
    model_instance2 = InvokeModel(
        user_prompt="Tigers", model=m2)
    print("qwen:", model_instance2.getResponse())
    # print('\n')
    # agent_instance = InvokeModel(user_prompt="How old is New Delhi", model=m1)
    # print("Deepseek agent: ", agent_instance.tutor_agent())
