import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

app = FastAPI()

# キャラクターの性格を定義
CHARACTER_PERSONA = "あなたは親しみやすく、時にユーモラスで、ユーザーを励ますAIキャラクターです。会話の流れやユーザーの感情に寄り添いながら返答してください。"

# Ollamaのエンドポイント
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

# Langchain LLMインスタンス
llm = Ollama(
    base_url=OLLAMA_HOST,
    model="llama3"
)

# 会話履歴を保持
memory = ConversationBufferMemory()

# プロンプトテンプレート
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=f"""
{persona}

これまでの会話履歴:
{{history}}

ユーザー: {{input}}
AIキャラクター: """
)

# Langchain会話チェーン
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt.partial(persona=CHARACTER_PERSONA)
)

class MessageRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: MessageRequest):
    response = conversation.predict(input=req.message)
    return {"response": response}

@app.get("/")
def root():
    return {"message": "AIキャラクター対話APIです。POST /chat で会話できます。"} 