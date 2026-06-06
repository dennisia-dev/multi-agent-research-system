from agents.planner import Planner
from tools.search_tool import SearchTool
from memory.memory import Memory
from agents.critic import Critic

from models.model_loader import model, tokenizer

import torch

class ResearchAgent:
	def __init__(self):
		self.planner = Planner()
		self.search_tool = SearchTool()
		self.memory = Memory()
		self.critic = Critic()

	def execute_task(self, task: str):
		"""
		Executes a single research task:
		- searches web
		- stores evidence in memory
		"""

		print(f"\nSearching: {task}")

		results = self.search_tool.search(task)

		for item in results:
			self.memory.add(item)

	def write_report(self, query: str):
		"""Generates final report using collected memory"""

		context = self.memory.get_recent(10)

		prompt = f"""
		You are a professional research assistant.

		Question:
		{query}

		Use the following evidence to write a clear, structured report:

		Evidence:
		{context}

		Write a detailed final answer with headings and explanation.
		"""

		inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

		outputs = model.generate(**inputs, max_new_tokens=400, temperature=0.7)

		return tokenizer.decode(outputs[0], skip_special_tokens=True)

	def run(self, query: str):
		print("\nCreating plan...\n")

		tasks = self.planner.create_plan(query)
		print(tasks)

		print("\nExeucting tasks...\n")

		for task in tasks:
			self.execute_task(task)

		print("\nWriting draft...\n")

		draft = self.write_report(query)

		print("\nCritic reviewing...\n")

		feedback = self.critic.review(query, draft)

		print("\nFeedback : \n")
		print(feedback)

    print("\n🔁 Improving final answer...\n")

    final_prompt = f"""
	Improve this answer using feedback.

	Question:
	{query}

	Draft:
	{draft}

	Feedback:
	{feedback}

	Write a final improved answer:
	"""

	inputs = tokenizer(final_prompt, return_tensors="pt").to(model.device)

	outputs = model.generate(**inputs, max_new_tokens=500, temperature=0.7)	

	final_report = tokenizer.decode(outputs[0], skip_special_tokens=True)

	return final_report