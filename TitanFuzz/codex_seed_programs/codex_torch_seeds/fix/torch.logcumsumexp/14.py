'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logcumsumexp\ntorch.logcumsumexp(input, dim, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data: ', input_data)
print('\nOutput: ', torch.logcumsumexp(input_data, dim=1))