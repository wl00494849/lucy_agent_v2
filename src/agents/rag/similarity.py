from src.infrastructure.llms.openai_client import OpenAIClient
import numpy as np

def get_cosine_similarity(term1:str,term2:str,model_size:bool=False):

    client = OpenAIClient()

    vec1 = client.get_vector(term1,model_size)
    vec2 = client.get_vector(term2,model_size)

    similarity = cosine_similarity(vec1,vec2)

    return similarity

def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    return dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2))