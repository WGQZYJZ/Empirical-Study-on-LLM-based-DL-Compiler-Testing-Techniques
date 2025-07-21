'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
data = torch.randn(2, 3)
print(data)
print(torch.argmin(data, dim=0))
print(torch.argmin(data, dim=1))
print(torch.argmin(data, dim=1, keepdim=True))