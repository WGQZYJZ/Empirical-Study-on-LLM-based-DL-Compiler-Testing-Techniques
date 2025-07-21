'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccos\ntorch.arccos(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
output_data = torch.arccos(input_data)
print('The input data is: ', input_data)
print('The output data is: ', output_data)