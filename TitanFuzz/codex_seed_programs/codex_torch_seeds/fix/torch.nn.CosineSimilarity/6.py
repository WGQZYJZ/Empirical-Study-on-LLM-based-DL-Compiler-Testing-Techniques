'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
import torch.nn as nn
input1 = torch.randn(10, 3)
input2 = torch.randn(10, 3)
cosine_similarity = nn.CosineSimilarity(dim=1, eps=1e-08)
output = cosine_similarity(input1, input2)
print(output)