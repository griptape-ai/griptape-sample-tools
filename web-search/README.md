# Web Search Tool

[![Deploy_to_Griptape](https://github.com/griptape-ai/griptape-cloud/assets/2302515/4fd57873-5c93-44a8-8fa3-ac1bf7d73bcc)](https://cloud.griptape.ai/tools/create/web-search)

This is a cloud-hosted version of the Griptape framework's [Web Search Tool](https://docs.griptape.ai/stable/griptape-tools/official-tools/web-search-tool/).

The tool will dynamically check the environment to decide which [Web Search Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-search-drivers/) to use, in the following priority order:

- If `TAVILY_API_KEY` is present in the environment, the tool will use the [Tavily Web Search Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-search-drivers#tavily).
- If `EXA_API_KEY` is present in the environment, the tool will use the [Exa Web Search Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-search-drivers#exa).
- If none of the above are present, the tool will use the [DuckDuckGo Web Search Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-search-drivers#duckduckgo). 

```env
# Set the Tavily API key if you want to use the Tavily Web Search Driver
TAVILY_API_KEY=

# Set the Exa API key if you want to use the Exa Web Search Driver
EXA_API_KEY=

# Set the number of search results to return
# If not set, the default value is 5
WEBSEARCH_RESULTS_COUNT=
```
