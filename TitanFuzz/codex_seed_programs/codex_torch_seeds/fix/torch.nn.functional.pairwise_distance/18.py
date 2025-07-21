'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
x1 = torch.rand(100, 10)
x2 = torch.rand(100, 10)
dis = torch.nn.functional.pairwise_distance(x1, x2)
print(dis)