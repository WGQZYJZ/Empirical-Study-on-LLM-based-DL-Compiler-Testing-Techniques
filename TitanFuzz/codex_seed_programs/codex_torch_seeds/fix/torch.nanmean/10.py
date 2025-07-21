'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmean\ntorch.nanmean(input, dim=None, keepdim=False, *, dtype=None, out=None)\n'
import torch
input = torch.rand(3, 3, 3)
print('Input: \n', input)
output = torch.nanmean(input, dim=2, keepdim=True)
print('Output: \n', output)