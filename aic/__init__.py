from google.cloud import storage
from jsonschema import validate
from typing import List
import json

BUCKET_NAME="ai-characters"


class AICharacter:
    def __init__(self, version: str, roleName: str, backstory: str, tools: List[str]):
        self.version = version
        self.roleName = roleName
        self.backstory = backstory
        self.tools = tools


def load_character(key: str) -> AICharacter:
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob_name = f"public/{key}/character.json"
    blob = bucket.blob(blob_name)
    character_json = blob.download_as_text()
    character_data = json.loads(character_json)
    validate(instance=character_data, schema=schema)

    # Create an AICharacter instance from the JSON data
    character = AICharacter(
        version=character_data['version'],
        roleName=character_data['roleName'],
        backstory=character_data['backstory'],
        tools=character_data['tools']
    )
    
    return character