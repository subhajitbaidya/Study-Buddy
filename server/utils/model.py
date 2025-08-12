from langchain_ollama import ChatOllama
from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


class ModelInput(BaseModel):
    prompt: str


class InvokeModel(ModelInput):

    def Model(self):
        return ChatOllama(
            model="deepseek-r1:1.5b",
            reasoning=False,
            temperature=0.6,
            num_predict=256,
        )

    def getResponse(self) -> str:
        prompt_template = PromptTemplate.from_template(
            "Tell me a sentence about {prompt}"
        )

        chain = prompt_template | self.Model() | StrOutputParser()

        response = chain.invoke({"prompt": self.prompt})
        return response
