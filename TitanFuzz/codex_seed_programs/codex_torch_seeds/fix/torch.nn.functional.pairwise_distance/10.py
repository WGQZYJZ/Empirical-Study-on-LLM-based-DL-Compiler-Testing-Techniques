'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
x1 = torch.rand(3, 5)
x2 = torch.rand(3, 5)
print('x1: ', x1)
print('x2: ', x2)
print('torch.nn.functional.pairwise_distance(x1, x2): ', torch.nn.functional.pairwise_distance(x1, x2))
print('torch.nn.functional.pairwise_distance(x1, x2, p=1): ', torch.nn.functional.pairwise_distance(x1, x2, p=1))
print('torch.nn.functional.pairwise_distance(x1, x2, p=2): ', torch.nn.functional.pairwise_distance(x1, x2, p=2))
print('torch.nn.functional.pairwise_distance(x1, x2, p=3): ', torch.nn.functional.pairwise_distance(x1, x2, p=3))