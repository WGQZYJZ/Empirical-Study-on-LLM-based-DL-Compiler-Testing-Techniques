"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
x = torch.rand(3, 3)
print(x)
print(torch.norm(x))
print(torch.norm(x, dim=0))
print(torch.norm(x, p=2))
print(torch.norm(x, dim=1, p=2))
print(torch.norm(x, dim=1, keepdim=True))