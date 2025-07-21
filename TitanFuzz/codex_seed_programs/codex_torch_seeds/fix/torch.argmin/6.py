'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
input = torch.randn(1, 3)
print('Input:', input)
output = torch.argmin(input, dim=1, keepdim=True)
print('Output:', output)