'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.expm1\ntorch.expm1(input, *, out=None)\n'
import torch
data = torch.rand(3, 4)
print('Input data:', data)
result = torch.expm1(data)
print('Result:', result)
result = torch.expm1_(data)
print('Result:', result)