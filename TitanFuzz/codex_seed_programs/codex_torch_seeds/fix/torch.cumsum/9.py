'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
input_data = torch.randn(3, 5)
print('input_data: ', input_data)
print('torch.cumsum(input_data, dim=1): ', torch.cumsum(input_data, dim=1))
print('torch.cumsum(input_data, dim=0): ', torch.cumsum(input_data, dim=0))