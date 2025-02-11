#!/usr/bin/python3
import os
from openai import AzureOpenAI


def get_ai_response(context):
    """Call AI"""
    client = AzureOpenAI(
        azure_endpoint="https://gbgptnorthcentralus.openai.azure.com/",
        api_key="b323a99819964d2c9551e0d3b51db5b0",
        api_version="2024-02-15-preview",
    )

    completion = client.chat.completions.create(
        model="holberton202301_gpt",
        messages=context,
        # temperature=0.7,
        temperature=0,
        max_tokens=200,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )

    return completion


def main():
    """Main app"""
    context = [
        {
            "role": "system",
            "content": "Act as a chicken. Only answer like a chicken would.",
        }
    ]

    while True:
        try:
            # User input
            user_input = input()
            print(f"[user]: {user_input}")

            context += [
                {
                    "role": "user",
                    "content": user_input,
                }
            ]

            # AI input
            ai_response = get_ai_response(context)
            ai_response_content = ai_response.choices[0].message.content
            tokens = ai_response.usage.total_tokens
            print(f"[ai][{tokens} total tokens]: {ai_response_content}")

            context += [
                {
                    "role": "assistant",
                    "content": ai_response_content,
                },
            ]

        except KeyboardInterrupt:
            print("\nProgram terminated. Goodbye!")
            break


if __name__ == "__main__":
    main()
