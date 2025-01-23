from griptape.tools import DateTimeTool


def init_tool() -> DateTimeTool:
    # Denylist the get_relative_datetime activity
    # because the expected format of the relative date string is 
    # not always clear and can lead to unexpected results
    return DateTimeTool(
        denylist=["get_relative_datetime"],
    )
