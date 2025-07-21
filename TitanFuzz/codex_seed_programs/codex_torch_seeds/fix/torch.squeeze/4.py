'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
input_data = torch.randn(2, 3, 5)
print('Input Data: ', input_data)
output_data = torch.squeeze(input_data)
print('Output Data: ', output_data)