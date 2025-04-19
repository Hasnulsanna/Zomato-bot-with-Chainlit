import chainlit as cl
from src.llm import ask_order

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    response = ask_order(user_input)
    await cl.Message(content=response).send()
