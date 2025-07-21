'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nansum\ntorch.nansum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
print('Input data: ', input)
output = torch.nansum(input, dim=1)
print('Output data: ', output)