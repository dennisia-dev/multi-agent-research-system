from models.model_loader import model, tokenizer
import torch

# What critic contributes:
# 1. Judge its own output
# 2. Detecte missing information
# 3. Improve reasoning quality
# Therefore it is a self-reflective agent pattern.

class Critic:
	def review(self, question: str, draft: str):
		"""Evaluates drafts answer and returns feedback."""

		prompt = f"""
		You are a strict AI critic.

		Evaluate the following answer.

		Check for:
		1. Missing important points
		2. Incorrect information
		3. Clarity and structure issues

		Question:
		{question}

		Draft Answer:
		{draft}

		Return bullet-point feedback only.
		"""

		inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

		outputs = model.generate(**inputs, max_new_tokens=200, temperature=0.3)

		feedback = tokenizer.decode(outputs[0], skip_special_tokens=True)

		return feedback