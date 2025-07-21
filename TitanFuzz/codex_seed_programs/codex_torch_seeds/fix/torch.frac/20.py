'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
data = torch.randn(5, 5)
print('Input data: ', data)
result = torch.frac(data)
print('Result: ', result)