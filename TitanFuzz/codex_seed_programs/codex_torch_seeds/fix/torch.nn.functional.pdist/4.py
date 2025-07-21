'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pdist\ntorch.nn.functional.pdist(input, p=2)\n'
import torch
import torch.nn.functional as F
x = torch.randn(3, 5)
print(x)
print(F.pdist(x))
print(F.pdist(x, p=2))
print(F.pdist(x, p=3))
print(F.pdist(x, p=4))
print(F.pdist(x, p=5))
print(F.pdist(x, p=6))
print(F.pdist(x, p=7))
print(F.pdist(x, p=8))
print(F.pdist(x, p=9))
print(F.pdist(x, p=10))
print(F.pdist(x, p=11))
print(F.pdist(x, p=12))
print(F.pdist(x, p=13))