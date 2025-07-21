'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
input = torch.rand(2, 2)
print(input)
result = torch.argmin(input, dim=1)
print(result)