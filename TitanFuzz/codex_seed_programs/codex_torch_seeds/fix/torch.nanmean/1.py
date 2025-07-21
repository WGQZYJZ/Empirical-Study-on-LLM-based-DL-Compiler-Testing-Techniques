'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmean\ntorch.nanmean(input, dim=None, keepdim=False, *, dtype=None, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
input[(0, 1)] = float('nan')
input[(1, 2)] = float('nan')
print('Input: ', input)
output = torch.nanmean(input, dim=0)
print('Output: ', output)