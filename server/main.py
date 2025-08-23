from fastapi import FastAPI, WebSocket
from langchain_ollama import ChatOllama
from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = FastAPI()


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


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        model_instance = InvokeModel(prompt=data)
        response = model_instance.getResponse()
        await websocket.send_text(f"AI: {response}")
