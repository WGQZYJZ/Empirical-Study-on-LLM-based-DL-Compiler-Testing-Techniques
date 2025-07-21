'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
print('Input data type: ', input_data.type())
ceil_data = torch.ceil(input_data)
print('Ceil data: ', ceil_data)
print('Ceil data type: ', ceil_data.type())