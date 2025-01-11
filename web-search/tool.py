import os

from griptape.tools import WebSearchTool
from griptape.drivers import (
    DuckDuckGoWebSearchDriver,
    TavilyWebSearchDriver,
    ExaWebSearchDriver,
)


def init_tool() -> WebSearchTool:
    driver = DuckDuckGoWebSearchDriver()
    # Check the environment variable to determine which driver to use
    if os.getenv("TAVILY_API_KEY") is not None:
        driver = TavilyWebSearchDriver(api_key=os.getenv("TAVILY_API_KEY"))
    elif os.getenv("EXA_API_KEY") is not None:
        driver = ExaWebSearchDriver(api_key=os.getenv("EXA_API_KEY"))

    driver.results_count = os.getenv("WEBSEARCH_RESULTS_COUNT", 5)

    return WebSearchTool(web_search_driver=driver)
