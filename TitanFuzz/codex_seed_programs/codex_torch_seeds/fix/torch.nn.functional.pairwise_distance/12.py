'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import numpy as np
import torch
x1 = torch.tensor([[1, 2, 3, 4], [1, 2, 3, 4]])
x2 = torch.tensor([[1, 2, 3, 4], [1, 2, 3, 4]])
torch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)
print('x1: ', x1)
print('x2: ', x2)
print('pairwise_distance: ', torch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False))
print('x1: ', x1)
print('x2: ', x2)