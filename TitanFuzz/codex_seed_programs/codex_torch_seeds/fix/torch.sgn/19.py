'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
data = torch.randn(2, 3)
print('Input data: ', data)
result = torch.sgn(data)
print('Result: ', result)