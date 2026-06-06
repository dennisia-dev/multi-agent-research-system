import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from models.model_loader import model, tokenizer

# 1. Structured reasoning
# 2. Predictable output
# 3. Production-style agent design

class Planner:

    def create_plan(self, query: str):

        prompt = f"""
		You are a research planner.

		Break the question into 3 research tasks.

		Return ONLY valid JSON in this format:

		{{
		  "tasks": [
		    "task 1",
		    "task 2",
		    "task 3"
		  ]
		}}

		Question:
		{query}
		"""

        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.4
        )

        text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # extract JSON safely
        try:
            json_start = text.find("{")
            json_text = text[json_start:]
            data = json.loads(json_text)
            return data["tasks"]

        except:
            # fallback if model fails
            return [
                "Analyze the topic",
                "Gather supporting information",
                "Summarize findings"
            ]