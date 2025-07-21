'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mode\ntorch.mode(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
data = torch.randn(3, 3)
print(data)
print(torch.mode(data))
print(torch.mode(data, dim=0))
print(torch.mode(data, dim=1))
print(torch.mode(data, dim=1, keepdim=True))