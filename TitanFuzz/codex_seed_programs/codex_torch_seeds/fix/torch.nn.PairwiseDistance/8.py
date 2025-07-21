'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PairwiseDistance\ntorch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)\n'
import torch
X = torch.randn(10, 3)
Y = torch.randn(10, 3)
print(X)
print(Y)
pairwise_distance = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
output = pairwise_distance(X, Y)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
X = torch.randn(10, 3)
Y = torch.randn(10, 3)
print(X)
print(Y)