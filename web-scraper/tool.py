import os

from griptape.tools import WebScraperTool
from griptape.loaders import WebLoader
from griptape.drivers import (
    TrafilaturaWebScraperDriver,
    ProxyWebScraperDriver,
)


def init_tool() -> WebScraperTool:
    driver = TrafilaturaWebScraperDriver()
    # Check the environment variable to determine which driver to use
    if (zenrows_api_key := os.getenv("ZENROWS_API_KEY")) is not None:
        # best effort default params
        zenrows_params = [
            "js_render=true",
            "wait=5000",
            "premium_proxy=true",
            "markdown_response=true",
        ]
        proxy = (
            f"http://{zenrows_api_key}:{'&'.join(zenrows_params)}@api.zenrows.com:8001"
        )
        proxies = {"http": proxy, "https": proxy}
        params = {
            "verify": False,
            "timeout": 120,
        }
        driver = ProxyWebScraperDriver(proxies=proxies, params=params)

    return WebScraperTool(
        web_loader=WebLoader(web_scraper_driver=driver),
    )
