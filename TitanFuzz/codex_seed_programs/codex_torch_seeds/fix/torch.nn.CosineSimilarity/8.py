'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
import torch
x = torch.rand(3, 4)
y = torch.rand(3, 4)
cosine_similarity = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
output = cosine_similarity(x, y)
print(output)