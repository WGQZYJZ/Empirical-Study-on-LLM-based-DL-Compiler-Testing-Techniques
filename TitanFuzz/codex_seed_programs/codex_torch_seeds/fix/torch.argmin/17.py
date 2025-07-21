'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
input = torch.randn(3, 4)
print(input)
min_index = torch.argmin(input, dim=0)
print(min_index)
min_index = torch.argmin(input, dim=1)
print(min_index)