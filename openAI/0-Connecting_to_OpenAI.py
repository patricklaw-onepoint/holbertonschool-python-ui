#!/usr/bin/python3
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://gbgptnorthcentralus.openai.azure.com/",
    api_key="b323a99819964d2c9551e0d3b51db5b0",
    api_version="2024-02-15-preview",
)

message_text = [
    {
        "role": "system",
        "content": "You are an AI assistant that helps people find information.",
    }
]

CONTENT = "OH NO! THE VOLCANO IS ABOUT TO E"
message_text = [{"role": "system", "content": CONTENT}]

# temperature: Sampling temperature. 0-1; default 0.
# higher makes output more random
# lower makes output more focused and deterministic.
# 0 automatically increases the temperature until certain thresholds are hit.


# top_p: nucleus sampling. 0-1; default 1.
# 0.1 means only the tokens comprising the top 10% probability mass are considered.
def get_ai_response(temp=0.7, p=0.95):
    """Call AI"""
    completion = client.chat.completions.create(
        model="holberton202301_gpt",
        messages=message_text,
        temperature=temp,
        max_tokens=200,
        top_p=p,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )

    print(f"temperature = {temp} | top_p ={p}")
    print(CONTENT, completion.choices[0].message.content, sep="")


if __name__ == "__main__":
    get_ai_response(0.7, 0.95)
    get_ai_response(0, 0.95)
    get_ai_response(0.5, 0.95)
    get_ai_response(1, 0.95)
    get_ai_response(0.7, 0)
    get_ai_response(0.7, 0.5)
    get_ai_response(0.7, 1)

"""
#temperature = 0.7 | top_p =0.95
OH NO! THE VOLCANO IS ABOUT TO ERUPT! QUICK, EVACUATE THE AREA IMMEDIATELY AND SEEK SHELTER IN A SAFE LOCATION AWAY FROM THE VOLCANO. STAY CALM AND FOLLOW THE INSTRUCTIONS OF LOCAL AUTHORITIES TO ENSURE YOUR SAFETY.

temperature = 0 | top_p =0.95
OH NO! THE VOLCANO IS ABOUT TO ERUPT! EVERYONE NEEDS TO EVACUATE IMMEDIATELY TO A SAFE LOCATION. PLEASE FOLLOW THE EVACUATION ROUTE AND STAY CALM. DO NOT DELAY, YOUR SAFETY IS THE TOP PRIORITY.
temperature = 0.5 | top_p =0.95
OH NO! THE VOLCANO IS ABOUT TO ENone
temperature = 1 | top_p =0.95
OH NO! THE VOLCANO IS ABOUT TO ERUPT! WE NEED TO EVACUATE IMMEDIATELY TO A SAFE LOCATION. PLEASE FOLLOW THE EVACUATION ROUTE AND STAY CALM. PROCEED TO THE DESIGNATED ASSEMBLY POINT AWAY FROM THE VOLCANO. STAY SAFE EVERYONE!       

temperature = 0.7 | top_p =0
OH NO! THE VOLCANO IS ABOUT TO ERUPT! EVERYONE NEEDS TO EVACUATE IMMEDIATELY TO A SAFE LOCATION. PLEASE FOLLOW THE EVACUATION ROUTE AND STAY CALM. DO NOT DELAY, YOUR SAFETY IS THE TOP PRIORITY.
temperature = 0.7 | top_p =0.5
OH NO! THE VOLCANO IS ABOUT TO ERUPT! EVERYONE NEEDS TO EVACUATE IMMEDIATELY TO A SAFE LOCATION. PLEASE FOLLOW THE EVACUATION ROUTE AND STAY CALM. DO NOT DELAY, YOUR SAFETY IS THE TOP PRIORITY.
temperature = 0.7 | top_p =1
OH NO! THE VOLCANO IS ABOUT TO ERUPT! TAKE COVER AND SEEK SAFETY IMMEDIATELY!
"""
