'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asin\ntorch.asin(input, *, out=None)\n'
import torch
data = torch.randn(1)
print('Input data: ', data)
result = torch.asin(data)
print('Output data: ', result)