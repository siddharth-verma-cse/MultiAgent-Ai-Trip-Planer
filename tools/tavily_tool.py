from tavily import TavilyClient
import os
from dotenv import load_dotenv


load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def tavily_search(query: str):
    """
    Search for a query using Tavily API.

    Args:
        query (str): The search query.
        """

    response = client.search(
        query=query,
        max_results=5
        )

    results = []

    for i, r  in enumerate(response['results'], 1):
        title = r.get('title', 'No Title')
        url = r.get('url', 'No URL')
        snippet = r.get("content", "").strip()

        if len(snippet) > 200:
            snippet = snippet[:200] + "..."
        results.append(f"{i}. {title}\nURL: {url}\nSnippet: {snippet}")

    return "\n\n".join(results)