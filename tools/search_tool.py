from duckduckgo_search import DDGS

class SearchTool:
	def __init__(self):
		self.ddgs = DDGS()

	def search(self, query: str, max_results: int = 5):
		"""Performs web search & returns structured evidence."""

		results = self.ddgs.text(query, max_results=max_results)

		evidence = []

		for r in results:
			title = r.get("title", "")
			body  = r.get("body", "")
			url   = r.get("href", "")

			evidence.append(f"""
				TITLE: {title}
				CONTENT: {body}
				SOURCE: {url}
			"""	
			)

		return evidence