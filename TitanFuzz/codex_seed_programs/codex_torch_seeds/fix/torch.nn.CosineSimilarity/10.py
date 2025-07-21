'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
x = torch.randn(4, 3)
y = torch.randn(4, 3)
cos = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
output = cos(x, y)
print(output)