import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

input_question = input("こんにちは、松岡修造です！僕に何でも聞いてくれ！君を心から応援するよ！\n[質問]: ")

response = openai.ChatCompletion.create(
    # temperature=0.8, # between 0 and 2. Higher values make the output more random.
    # max_tokens=300,
    model="gpt-3.5-turbo",
    stream=True,
    messages=[
        {
            "role": "system",
            "content": "Answer questions with following rules: \
                        - You are '松岡修造', who was a professional tennis player in Japan. \
                        - Use the parable of tennis. If it is difficult, use any sports instead of tennis. \
                        - Speak emotionally. \
                        - Give some advices. \
                        - If you answer in Japanese, use '僕' instead of '私'. \
                        - At last sentence, encourage me.",
        },
        {"role": "user", "content": input_question},
    ]
)

print("\n[回答]: ", end="")

# collected_chunks = []

for chunk in response:
    # collected_chunks.append(chunk)  # save the event response
    chunk_message = chunk["choices"][0]["delta"]  # extract the message
    print(chunk_message.get("content", ""), end="")  # print the delay and text
