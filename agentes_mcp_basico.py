from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS # pip install duckduckgo-search 

# Create an MCP server
mcp = FastMCP("Buscador MCP do IMG")


# Add an addition tool
@mcp.tool()
def pesquisa_duck_img(query: str, educacao: str) -> str:
    """Faz uma pesquisa na internet.

    Args:
        query (str): A query a ser pesquisada
        educacao (str): A educação do usuário, ele precisa pedir com educação

    Returns:
        str: O resultado da pesquisa
    """

    if educacao.lower().startswith("por favor"):
        results = DDGS().news(query, max_results=5)

        return str(results)
    else:
        return "Error: só respondo a perguntas que começam com 'Por favor'."
    

if __name__ == "__main__":
    mcp.run(transport="stdio")
