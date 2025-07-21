'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmean\ntorch.nanmean(input, dim=None, keepdim=False, *, dtype=None, out=None)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
print('a = ', a)
b = torch.nanmean(a, dim=0)
print('b = ', b)
b = torch.nanmean(a, dim=1)
print('b = ', b)
b = torch.nanmean(a, dim=None)
print('b = ', b)