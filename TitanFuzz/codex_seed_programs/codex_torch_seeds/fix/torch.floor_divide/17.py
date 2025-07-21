'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input_data = torch.arange(1, 10, dtype=torch.float32).reshape(3, 3)
other_data = torch.arange(1, 4, dtype=torch.float32).reshape(3, 1)
print('Input data: ', input_data)
print('Other data: ', other_data)
output_data = torch.floor_divide(input_data, other_data)
print('Output data: ', output_data)