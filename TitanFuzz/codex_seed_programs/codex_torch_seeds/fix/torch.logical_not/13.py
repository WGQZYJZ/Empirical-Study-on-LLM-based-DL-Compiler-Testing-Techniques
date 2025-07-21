'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_not\ntorch.logical_not(input, *, out=None)\n'
import torch
input_data = torch.tensor([[True, False], [False, True]], dtype=torch.bool)
print('Input data: ', input_data)
output_data = torch.logical_not(input_data)
print('Output data: ', output_data)