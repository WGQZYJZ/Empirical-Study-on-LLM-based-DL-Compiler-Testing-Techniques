'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
data = torch.randn(1, 3)
print('Input data: ', data)
result = torch.floor(data)
print('Result: ', result)