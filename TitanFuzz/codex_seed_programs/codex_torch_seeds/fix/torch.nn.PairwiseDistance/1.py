'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PairwiseDistance\ntorch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch.nn as nn
x = torch.rand(2, 3)
y = torch.rand(2, 3)
pairwise_distance = nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
distance = pairwise_distance(x, y)
print(distance)