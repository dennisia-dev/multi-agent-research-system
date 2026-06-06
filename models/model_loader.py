import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "microsoft/phi-2"

print("Loading model... (this may take time on first run)")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
	MODEL_NAME,
	device_map="auto",
	torch_dtype=torch.float16
)

model.eval()

print("Model loaded successfully.")