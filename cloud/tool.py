from schema import Literal, Schema
import requests
import os
from griptape.artifacts import BaseArtifact, ErrorArtifact, TextArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity


class AssistantTool(BaseTool):
    def __init__(self, api_key: str, base_url: str):
        super().__init__()
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })

    @activity(
        config={
            "description": "Creates a new assistant with the specified configuration",
            "schema": Schema(
                {
                    Literal(
                        "request_content",
                        description="Assistant configuration content to create a new assistant"
                    ): {
                        "name": str,
                        "description": str | None,
                        "input": str | None,
                        "knowledge_base_ids": list[str] | None,
                        "ruleset_ids": list[str] | None,
                        "structure_ids": list[str] | None,
                        "tool_ids": list[str] | None,
                    },
                }
            )
        }
    )
    def create_assistant(self, params: dict) -> BaseArtifact:
        try:
            request_content = params["values"]["request_content"]
            response = self.session.post(
                f"{self.base_url}/assistants",
                json=request_content
            )
            response.raise_for_status()
            result = response.json()
            return TextArtifact(f"Assistant created successfully with ID: {result['id']}")
        except requests.RequestException as e:
            return ErrorArtifact(f"API error creating assistant: {str(e)}")
        except Exception as e:
            return ErrorArtifact(f"Error creating assistant: {str(e)}")

    @activity(
        config={
            "description": "Deletes an existing assistant by ID",
            "schema": Schema(
                {
                    Literal(
                        "assistant_id",
                        description="The ID of the assistant to delete"
                    ): str,
                }
            )
        }
    )
    def delete_assistant(self, params: dict) -> BaseArtifact:
        try:
            assistant_id = params["values"]["assistant_id"]
            response = self.session.delete(
                f"{self.base_url}/assistants/{assistant_id}"
            )
            response.raise_for_status()
            return TextArtifact(f"Assistant {assistant_id} deleted successfully")
        except requests.RequestException as e:
            return ErrorArtifact(f"API error deleting assistant: {str(e)}")
        except Exception as e:
            return ErrorArtifact(f"Error deleting assistant: {str(e)}")


def init_tool() -> BaseTool:
    api_key = os.getenv("GRIPTAPE_API_KEY")
    base_url = os.getenv("API_BASE_URL")
    return AssistantTool(api_key=api_key, base_url=base_url)
