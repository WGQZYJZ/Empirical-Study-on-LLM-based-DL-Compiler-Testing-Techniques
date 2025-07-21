'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import numpy as np
x1 = torch.randn(1, 3)
x2 = torch.randn(1, 3)
print(torch.nn.functional.pairwise_distance(x1, x2))
print(torch.nn.functional.pairwise_distance(x1, x2, p=1))
print(torch.nn.functional.pairwise_distance(x1, x2, p=3))
print(torch.nn.functional.pairwise_distance(x1, x2, p=np.inf))
print(torch.dist(x1, x2))
print(torch.dist(x1, x2, p=1))
print(torch.dist(x1, x2, p=3))
print(torch.dist(x1, x2, p=np.inf))