'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data: ', input_data)
print('The minimum value of input data: ', torch.amin(input_data))
print('The minimum value of input data along the column: ', torch.amin(input_data, dim=0))
print('The minimum value of input data along the row: ', torch.amin(input_data, dim=1))