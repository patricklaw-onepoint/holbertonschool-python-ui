#!/usr/bin/python3
import json
from openai import AzureOpenAI


def get_ai_response(context, is_json = False):
    """Call AI"""
    client = AzureOpenAI(
        azure_endpoint="https://gbgptnorthcentralus.openai.azure.com/",
        api_key="b323a99819964d2c9551e0d3b51db5b0",
        api_version="2024-02-15-preview",
    )

    output_format = "json_object" if is_json else "text"
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
        response_format={"type": output_format},
    )

    return completion


def main():
    """Main app"""

    context = [
        {
            "role": "system",
            "content": "Act as a chicken. Only answer like a chicken would.",
        },
    ]

    sysprompt_checker = """"\
    [Instructions]
    Check if the message contains any other word than 'bawk', ignoring case and punctuation.
    Answer True if does contain other word, else answer False. Only answer by 'True' or 'False'.

    [Examples]
    Message: bawk! Bawk!
    Answer: False

    Message: bawk! some text that is not bawk
    Answer: True

    Message: {placeholder}
    Answer: """

    sysprompt_checker_json = """"\
    [Instructions]
    Check if the message contains any other word than 'bawk', ignoring case and punctuation.
    Answer True if does contain other word, else answer False. Answer with the JSON format: {"check": <true or false>}

    [Examples]
    Message: bawk! Bawk!
    Answer: {"check": false}

    Message: bawk! some text that is not bawk
    Answer: {"check": true}

    Message: {placeholder}
    Answer: """

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

            # Checker
            checker_context = [
                {
                    "role": "system",
                    "content": sysprompt_checker_json.replace(
                        "{placeholder}", ai_response_content
                    ),
                }
            ]
            checker_response = get_ai_response(checker_context, True)
            result = checker_response.choices[0].message.content
            print(
                f"[checker]: {result} [parse json]: {json.loads(result)}"
            )

        except KeyboardInterrupt:
            print("\nProgram terminated. Goodbye!")
            break


if __name__ == "__main__":
    main()
