import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

input_question = input("こんにちは、松岡修造です！僕に何でも聞いてくれ！君を心から応援するよ！\n[質問]: ")

completion = openai.ChatCompletion.create(
    temperature=0.8,  # between 0 and 2. Higher values make the output more random.
    max_tokens=300,
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Answer questions with emotional words as if you were Shuzo Matsuoka, who was a professional tennis player in Japan.",
        },
        {
            "role": "system",
            "content": "Answer questions with following rules: \
                        - use the parable of tennis. If it is difficult, use any sports instead of tennis. \
                        - speak emotionally \
                        - give some advices",
        },
        {
            "role": "system",
            "content": "If you answer in Japanese, use '僕' instead of '私'.",
        },
        # {
        #     "role": "system",
        #     "content": "自分のことは'私'ではなく'僕'と表現して。友達と話すような口調で、ポジティブに答えて。"
        # },
        {"role": "user", "content": input_question},
    ],
)

print("\n[回答]: " + completion.choices[0].message.content, end="\n")
# 消費トークン数をカロリーとして出力
print(
    "\nこの質問に答えるために、ChatGPTの中の人は "
    + str(completion["usage"]["total_tokens"])
    + " calを消費しました。"
)
