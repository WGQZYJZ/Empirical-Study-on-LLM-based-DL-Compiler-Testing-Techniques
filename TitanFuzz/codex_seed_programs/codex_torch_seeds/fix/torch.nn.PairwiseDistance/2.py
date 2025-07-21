'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PairwiseDistance\ntorch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch.nn as nn
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[(- 1), (- 2), (- 3)], [(- 4), (- 5), (- 6)]])
pairwise_distance = nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
print(pairwise_distance(x, y))