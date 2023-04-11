import openai
from app.utils import logger
from app.service import Opmessage


class Gpt:
    def ask_chat_stream_gpt(user_id, content):
        messages = Opmessage.merge_history_message(user_id, "user", content)
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=0,
            max_tokens=1024,  # 回复最大的字符数
            stop=None,
            stream=True
        )
        collected_messages = []
        role = ''
        for chunk in response:
            delta = chunk['choices'][0]['delta']
            if delta.get('role') is not None:
                role = delta.get('role')
            if delta.get('content') is not None:
                yield delta.get('content')
            collected_messages.append(delta)

        full_reply_content = ''.join([m.get('content', '')
                                      for m in collected_messages])

        logger.info("[gpt] role=%s, full_reply_content=%s",
                    role, full_reply_content)
        Opmessage.save_message(user_id, role, content, full_reply_content)

    def ask_gpt(user_id, prompt):
        reply = openai.Completion.create(
            model="text-davinci-002",  # 对话模型的名称
            prompt=prompt,
            temperature=0.9,  # 值在[0,1]之间，越大表示回复越具有不确定性
            max_tokens=1024,  # 回复最大的字符数
            top_p=1,
            frequency_penalty=0.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            presence_penalty=0.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            stop=["\n\n\n"],
            stream=True
        )
        full_response = ""
        for response in reply:
            if response.get("choices") is None or len(response["choices"]) == 0:
                raise Exception("OpenAI API returned no choices")
            if response["choices"][0].get("finish_details") is not None:
                break
            if response["choices"][0].get("text") is None:
                raise Exception("OpenAI API returned no text")
            if response["choices"][0]["text"] == "<|endoftext|>":
                break
            # response.choices[0].text
            yield response["choices"][0]["text"]
            full_response += response["choices"][0]["text"]
        # 存储 full_response
