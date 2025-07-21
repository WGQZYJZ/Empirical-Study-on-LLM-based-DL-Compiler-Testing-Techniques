'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccos\ntorch.arccos(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data is: ', input_data)
output = torch.arccos(input_data)
print('Output data is: ', output)
print('Shape of the output data is: ', output.shape)