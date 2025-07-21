'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logcumsumexp\ntorch.logcumsumexp(input, dim, *, out=None)\n'
import torch
input_data = torch.rand(100)
print('Input data is: ', input_data)
result = torch.logcumsumexp(input_data, dim=0)
print('Result is: ', result)