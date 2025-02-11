#!/usr/bin/python3
import numpy as np
from openai import AzureOpenAI
from sklearn.metrics.pairwise import cosine_similarity as cs


def main():
    """Main app"""
    client = AzureOpenAI(
        azure_endpoint="https://gbgptnorthcentralus.openai.azure.com/",
        api_key="b323a99819964d2c9551e0d3b51db5b0",
        api_version="2024-02-15-preview",
    )

    actions = [
        "the cat turned left",
        "the dog went forward",
        "the cat went backward",
        "the dog turned right",
        "the cat is cold",
        "the dog is hot",
    ]

    response = client.embeddings.create(
        input=actions,
        model="holberton202301_e",
    )

    embeddings = [np.array(e.embedding) for e in response.data]

    with np.printoptions(precision=3, suppress=True):
        print(cs(embeddings))

    question = "who turned right?"
    response = client.embeddings.create(
        input=question, model="holberton202301_e"
    )
    print(question)

    r = cs(embeddings, [np.array(response.data[0].embedding)]).squeeze(1)
    print(actions[np.argmax(r)])


if __name__ == "__main__":
    main()

"""Result:
[[1.    0.863 0.912 0.927 0.865 0.793]
 [0.863 1.    0.898 0.899 0.822 0.862]
 [0.912 0.898 1.    0.859 0.866 0.793]
 [0.927 0.899 0.859 1.    0.807 0.852]
 [0.865 0.822 0.866 0.807 1.    0.86 ]
 [0.793 0.862 0.793 0.852 0.86  1.   ]]
"""
