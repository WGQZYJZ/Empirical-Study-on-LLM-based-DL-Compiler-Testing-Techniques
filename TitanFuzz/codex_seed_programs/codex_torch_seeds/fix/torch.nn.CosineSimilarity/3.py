'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
x1 = torch.rand(2, 3)
x2 = torch.rand(2, 3)
cosine_similarity = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
y = cosine_similarity(x1, x2)
print(y)