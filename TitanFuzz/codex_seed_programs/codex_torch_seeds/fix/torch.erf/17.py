'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erf\ntorch.erf(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 5)
print('Input data: ', input_data)
print('Output data: ', torch.erf(input_data))