'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
data = torch.randn(2, 2)
print('Input data:\n', data)
output = torch.square(data)
print('Output data:\n', output)