# Web Scraper Tool

[![Deploy_to_Griptape](https://github.com/griptape-ai/griptape-cloud/assets/2302515/4fd57873-5c93-44a8-8fa3-ac1bf7d73bcc)](https://cloud.griptape.ai/tools/create?sample-name=web-scraper&type=sample)

This is a cloud-hosted version of the Griptape framework's [Web Scraper Tool](https://docs.griptape.ai/stable/griptape-tools/official-tools/web-scraper-tool/).

The tool will dynamically check the environment to decide which [Web Scraper Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-scraper-drivers/) to use, in the following priority order:

- If `ZENROWS_API_KEY` is present in the environment, the tool will use the [Proxy Web Scraper Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-scraper-drivers#proxy) with the web scraping service [ZenRows](https://www.zenrows.com/).
- If none of the above are present, the tool will use the [Trafilatura Web Scraper Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/web-scraper-drivers#trafilatura). 

```env
# Set the ZenRows API key if you want to use the Proxy Web Scraper Driver with ZenRows
ZENROWS_API_KEY=

```
