# 1. 导入第三方库
import openai
import os
from dotenv import load_dotenv, find_dotenv

# 2. 读取系统中的环境变量
_ = load_dotenv(find_dotenv())

# 3. 设置 API_KEY
# 3.1）可从系统环境变量中读取
openai.api_key  = os.getenv('OPENAI_API_KEY')
# 3.2）也可直接提供
# openai.api_key  = 'API_KEY' # 此处需将API_KEY替换成正常的

# 4. 一个封装 OpenAI 接口的函数，参数为 Prompt，返回对应结果
def get_completion(prompt, model="gpt-3.5-turbo"):
    '''
    prompt: 对应的提示
    model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # 模型输出的温度系数，控制输出的随机程度，值越低则输出文本随机性越低
    )
    # 调用 OpenAI 的 ChatCompletion 接口
    return response.choices[0].message["content"]

# 5. 需要总结的文本内容
text = f"""
你应该提供尽可能清晰、具体的指示，以表达你希望模型执行的任务。\
这将引导模型朝向所需的输出，并降低收到无关或不正确响应的可能性。\
不要将写清晰的提示与写简短的提示混淆。\
在许多情况下，更长的提示可以为模型提供更多的清晰度和上下文信息，从而导致更详细和相关的输出。
"""

# 6. 指令内容，使用 ``` 来分隔指令和待总结的内容
prompt = f"""
把用三个反引号括起来的文本总结成一句话。
```{text}```
"""

# 7. 输出
response = get_completion(prompt)
print(response)