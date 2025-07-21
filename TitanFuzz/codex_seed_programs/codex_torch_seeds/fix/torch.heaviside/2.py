'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.heaviside\ntorch.heaviside(input, values, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input data: ', input)
print('Input data type: ', input.dtype)
values = torch.tensor([0.5, 1.0, 2.0])
print('Values: ', values)
print('Values data type: ', values.dtype)
output = torch.heaviside(input, values)
print('Output: ', output)
print('Output data type: ', output.dtype)