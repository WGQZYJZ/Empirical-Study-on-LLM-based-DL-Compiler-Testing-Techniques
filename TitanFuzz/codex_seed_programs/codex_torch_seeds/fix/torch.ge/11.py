'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ge\ntorch.ge(input, other, *, out=None)\n'
import torch
data = torch.randn(2, 3)
print('Input data: \n', data)
result = torch.ge(data, 0.5)
print('Result: \n', result)