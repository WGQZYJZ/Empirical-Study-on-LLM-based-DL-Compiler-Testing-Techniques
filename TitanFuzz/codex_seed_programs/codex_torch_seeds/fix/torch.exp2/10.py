'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp2\ntorch.exp2(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3)
print('Input data: ', input_data)
print('Input data type: ', input_data.type())
output_data = torch.exp2(input_data)
print('Output data: ', output_data)
print('Output data type: ', output_data.type())