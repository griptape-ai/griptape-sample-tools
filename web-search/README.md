# Web Search Tool

This is a cloud-hosted version of the Griptape framework's [Web Search Tool](https://docs.griptape.ai/stable/griptape-tools/official-tools/web-search-tool/).

On deployment, the tool will check the environment to decide which [Web Search Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-search-drivers/) to use, in the following priority order:

- If `TAVILY_API_KEY` is present in the environment, the tool will use the [Tavily Web Search Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-search-drivers#tavily).
- If `EXA_API_KEY` is present in the environment, the tool will use the [Exa Web Search Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-search-drivers#exa).
- If none of the above are present, the tool will use the [DuckDuckGo Web Search Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-search-drivers#duckduckgo). 
