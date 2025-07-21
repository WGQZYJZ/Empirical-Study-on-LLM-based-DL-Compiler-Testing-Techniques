'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
x1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
x2 = torch.tensor([[1, 2, 3], [4, 5, 6]])
res = F.pairwise_distance(x1, x2)
print(res)
import torch
import torch.nn.functional as F
x1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
x2 = torch.tensor([[1, 2, 3], [4, 5, 6]])
res = F.pairwise_distance(x1, x2, p=1)
print(res)