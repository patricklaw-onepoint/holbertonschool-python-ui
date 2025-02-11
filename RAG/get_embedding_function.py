from langchain_aws import BedrockEmbeddings
import boto3


def get_embedding_function():
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="ap-southeast-2",
    )

    embeddings = BedrockEmbeddings(
        region_name="ap-southeast-2",
        client=bedrock_client,
    )
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
