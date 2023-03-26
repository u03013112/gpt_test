import os

import sys
sys.path.append('D:\git\gpt_test')

from config import openaiAPIKey

import openai
import requests


os.environ["HTTP_PROXY"] = "http://127.0.0.1:10809"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:10809"

# 配置OpenAI API密钥和会话
openai.api_key = openaiAPIKey

# 使用OpenAI API
response = openai.Completion.create(
    # engine="text-davinci-002",
    engine="gpt-3.5-turbo",
    prompt="Hello, I am a friendly chatbot. How are you today?",
    max_tokens=150,
    temperature=0.5,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0,
)

print(response.choices[0].text)
