'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
x1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
x2 = torch.tensor([[7, 8, 9], [10, 11, 12]])
distance = torch.nn.functional.pairwise_distance(x1, x2)
print('distance = ', distance)