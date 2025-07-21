'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pdist\ntorch.nn.functional.pdist(input, p=2)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
input = torch.randn(3, 3)
print(F.pdist(input))
print(F.pdist(input, p=1))
print(F.pdist(input, p=float('inf')))