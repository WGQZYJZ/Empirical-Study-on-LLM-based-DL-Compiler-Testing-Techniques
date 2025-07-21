"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
x = torch.randn(3, 3)
print(torch.norm(x))
print(torch.norm(x, 1))
print(torch.norm(x, 2))
print(torch.norm(x, 3))
print(torch.norm(x, float('inf')))