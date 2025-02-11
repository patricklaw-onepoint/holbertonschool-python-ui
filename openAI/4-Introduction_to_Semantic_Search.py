#!/usr/bin/python3
import numpy as np
from openai import AzureOpenAI


def cosine_similarity(a, b, normalized=False):
    if normalized:
        return np.dot(a, b)
    else:
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def main():
    """Main app"""
    client = AzureOpenAI(
        azure_endpoint="https://gbgptnorthcentralus.openai.azure.com/",
        api_key="b323a99819964d2c9551e0d3b51db5b0",
        api_version="2024-02-15-preview",
    )

    response = client.embeddings.create(
        input="Your text string goes here", model="holberton202301_e"
    )

    #print(response.model_dump_json(indent=2))

    print(
        np.linalg.norm(response.data[0].embedding)
    )  # 1.000000013538145, which is close enough to 1 to consider it normalised.

if __name__ == "__main__":
    main()
