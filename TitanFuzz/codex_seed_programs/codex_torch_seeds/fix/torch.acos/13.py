'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acos\ntorch.acos(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.0, 1.0])
print('Input data: ', input_data)
output_data = torch.acos(input_data)
print('Output data: ', output_data)