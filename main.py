import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

input_question = input("こんにちは、松岡修造です！僕に何でも聞いてくれ！君を心から応援するよ！\n[質問]: ")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Answer questions with emotional words as if you were Shuzo Matsuoka, who was a professional tennis player in Japan.",
        },
        {"role": "user", "content": input_question},
    ],
)

print("\n[回答]: " + completion.choices[0].message.content)
# 消費トークン数をカロリーとして出力
print(
    "\nこの質問に答えるために、ChatGPTの中の人は " + str(completion.usage.total_tokens) + " calを消費しました。"
)
