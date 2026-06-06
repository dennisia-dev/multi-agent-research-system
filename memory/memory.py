class Memory:
	def __init__(self):
		self.notes = []

	def add(self, text: str):
		"""Store a piece of evidence or context."""
		self.notes.append(text)

	def get_all(self):
		"""Return full memory as a single context string."""
		return "\n\n".join(self.notes)

	def get_recent(self, k=5):
		"""Return only recent memory (prevents context overflow)."""
		return "\n\n".join(self.notes[-k:])