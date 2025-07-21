'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lt\ntorch.lt(input, other, *, out=None)\n'
import torch
data = torch.rand(10, 10)
result = torch.lt(data, 0.5)
print('input data:\n', data)
print('result:\n', result)