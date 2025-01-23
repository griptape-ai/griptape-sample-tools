from datetime import datetime

from schema import Literal, Schema

from griptape.artifacts import BaseArtifact, ErrorArtifact, TextArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity


class DateTimeTool(BaseTool):
    @activity(config={"description": "Can be used to return current date and time."})
    def get_current_datetime(self) -> BaseArtifact:
        try:
            current_datetime = datetime.now()

            return TextArtifact(str(current_datetime))
        except Exception as e:
            return ErrorArtifact(f"error getting current datetime: {e}")


def init_tool() -> BaseTool:
    return DateTimeTool()
