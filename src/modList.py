import os
import openai

import sys
sys.path.append('D:\git\gpt_test')

from config import openaiAPIKey
import proxy

openai.api_key = openaiAPIKey
models = openai.Model.list()

for model in models["data"]:
    print(model["id"])