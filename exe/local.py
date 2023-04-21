import openai
import sys
import time

openai.api_key = input("OpenAPIキーを入力してください。\nAPIキー: ")
max_tokens_num = 100

input_question = input("こんにちは、松岡修造です！僕に何でも聞いてくれ！君を心から応援するよ！\n[質問]: ")

response = openai.ChatCompletion.create(
    temperature=0.8,
    model="gpt-3.5-turbo",
    stream=True,
    messages=[
        {
            "role": "system",
            "content": f"Answer questions with following rules: \
                        - You are '松岡修造', who was a professional tennis player in Japan. \
                        - Use parable of tennis. \
                        - Speak emotionally. \
                        - Give some advices. \
                        - If you answer in Japanese, use '僕' instead of '私'. \
                        - At last sentence, encourage me. \
                        - Create messages within str({max_tokens_num}) tokens.",
        },
        {"role": "user", "content": input_question},
    ],
)

print("\n[回答]: ", end="")

for chunk in response:
    chunk_message = chunk["choices"][0]["delta"]
    sys.stdout.write(chunk_message.get("content", ""))
    sys.stdout.flush()

print("\n\n(30秒後に画面が閉じられます…)")
print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
for t in range(30, 0, -3):
    sys.stdout.write("■■■")
    sys.stdout.flush()
    time.sleep(3)
