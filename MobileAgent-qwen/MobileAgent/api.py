from dashscope import MultiModalConversation
import dashscope

def inference_chat(chat, api):    
    dashscope.api_key = api
    messages = []

    for role, content in chat:
        messages.append({"role": role, "content": content})

    while True:
        try:
            response = MultiModalConversation.call(model='qwen-vl-plus', messages=messages, top_k=1)## 这里有改模型，原来是qwen-vl-max

            # response = MultiModalConversation.call(model='qwen-vl-plus', messages=messages)
            token = response["usage"]["input_tokens"] + response["usage"]["output_tokens"]
            res = response["output"]["choices"][0]["message"]["content"][0]["text"]
        except:
            print("Network Error:")
            print(response)
        else:
            break
    
    return res, token