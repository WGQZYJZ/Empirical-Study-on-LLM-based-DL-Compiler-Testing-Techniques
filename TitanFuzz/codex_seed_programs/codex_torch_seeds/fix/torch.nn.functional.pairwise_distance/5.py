'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
x1 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x2 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(F.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False))