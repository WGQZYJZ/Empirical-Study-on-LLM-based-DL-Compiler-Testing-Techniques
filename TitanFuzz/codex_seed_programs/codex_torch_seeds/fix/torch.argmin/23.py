'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
import torch
input = torch.randn(2, 3)
torch.argmin(input, dim=None, keepdim=False)
print('The input data is:')
print(input)
print('The argmin is:')
print(torch.argmin(input, dim=None, keepdim=False))