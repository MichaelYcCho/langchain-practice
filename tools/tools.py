from langchain_community.tools.tavily_search import TavilySearchResults


# Tavily는 LLM과 접합하여 검색에 최적화된 엔진을 제공한다. # https://app.tavily.com/
def get_profile_url_tavily(name: str):
    """Searches for Linkedin or Twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res