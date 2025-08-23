from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))


# example model, you wanted gemma-3-270m-it
# modelName = 'google/gemma-3-270m-it'


# class DownloadModel:
#     def __init__(self, modelName):
#         self.modelName = modelName

#     def getGemmaModel(self):
#         # Download
#         tokenizer = AutoTokenizer.from_pretrained(self.modelName)
#         model = AutoModelForCausalLM.from_pretrained(self.modelName)

#         # Save locally
#         model.save_pretrained("./gemma")
#         tokenizer.save_pretrained("./gemma")


# if __name__ == "__main__":
#     # Only run download once, then comment this out
#     DownloadModel(modelName).getGemmaModel()

#     # Load from local path
#     tokenizer = AutoTokenizer.from_pretrained("./gemma")
#     model = AutoModelForCausalLM.from_pretrained("./gemma")

#     pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
#     print(pipe("Who are you?", max_new_tokens=50))
