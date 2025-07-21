"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
x = torch.randn(3, 3)
print(x)
y = torch.norm(x, p='fro')
print(y)
y = torch.norm(x, dim=1)
print(y)
y = torch.norm(x, dim=0)
print(y)
y = torch.norm(x, dim=1, keepdim=True)
print(y)
y = torch.norm(x, dim=0, keepdim=True)
print(y)