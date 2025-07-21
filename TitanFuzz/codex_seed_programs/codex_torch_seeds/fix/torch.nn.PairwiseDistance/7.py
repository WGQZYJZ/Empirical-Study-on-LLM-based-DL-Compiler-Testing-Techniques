'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PairwiseDistance\ntorch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch
x1 = torch.randn(3, 4)
x2 = torch.randn(3, 4)
torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)(x1, x2)
print(torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)(x1, x2))
print(torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)(x1, x2).shape)