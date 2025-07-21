"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
x = torch.randn(3, 3)
print(x)
print(x.norm(p=2, dim=1, keepdim=True))
print(x.norm(p=2, dim=1, keepdim=False))