'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch
x1 = torch.randn(2, 3)
print('x1: ', x1)
x2 = torch.randn(2, 3)
print('x2: ', x2)
distance = torch.nn.functional.pairwise_distance(x1, x2)
print('distance: ', distance)