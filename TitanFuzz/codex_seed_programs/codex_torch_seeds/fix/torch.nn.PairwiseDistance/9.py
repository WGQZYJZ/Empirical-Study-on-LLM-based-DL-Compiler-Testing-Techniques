'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PairwiseDistance\ntorch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)\n'
import torch
x = torch.randn(3, 5)
y = torch.randn(3, 5)
print(x)
print(y)
dist = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
print(dist(x, y))