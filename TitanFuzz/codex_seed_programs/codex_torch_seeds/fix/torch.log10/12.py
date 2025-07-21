'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3, 3)
print('Input Data: ', input_data)
print('Output Data: ', torch.log10(input_data))