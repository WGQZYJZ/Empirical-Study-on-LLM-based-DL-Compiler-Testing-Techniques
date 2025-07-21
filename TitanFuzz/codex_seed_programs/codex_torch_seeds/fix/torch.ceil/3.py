'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
print('Ceil of input data: ', torch.ceil(input_data))
print('Ceil of input data: ', torch.ceil(input_data).dtype)
'\nTask 4: Call the API torch.ceil_\ntorch.ceil_(input, *, out=None)\n'
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
print('Ceil of input data: ', torch.ceil_(input_data))
print('Ceil of input data: ', torch.ceil_(input_data).dtype)
'\nTask 5: Call the API torch.clamp\ntorch.clamp(input, min, max, *, out=None)\n'
input_data = torch.randn(2, 3)
print('Input data: ', input_data)