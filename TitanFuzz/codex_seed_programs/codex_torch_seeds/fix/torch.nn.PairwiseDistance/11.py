'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PairwiseDistance\ntorch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch
x1 = torch.rand(1, 3)
x2 = torch.rand(1, 3)
print('x1: ', x1)
print('x2: ', x2)
pairwise_distance = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
distance = pairwise_distance.forward(x1, x2)
print('distance: ', distance)