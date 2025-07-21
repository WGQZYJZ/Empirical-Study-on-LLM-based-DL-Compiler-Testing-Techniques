"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
a = torch.rand(3, 3)
b = torch.rand(3, 3)
print('a:', a)
print('b:', b)
print('torch.norm(a):', torch.norm(a))
print('torch.norm(a, p=2):', torch.norm(a, p=2))
print('torch.norm(a, p=1):', torch.norm(a, p=1))
print('torch.norm(a, p=inf):', torch.norm(a, p=float('inf')))
print('torch.norm(a, dim=0):', torch.norm(a, dim=0))
print('torch.norm(a, dim=1):', torch.norm(a, dim=1))
print('torch.norm(a, dim=(0, 1)):', torch.norm(a, dim=(0, 1)))