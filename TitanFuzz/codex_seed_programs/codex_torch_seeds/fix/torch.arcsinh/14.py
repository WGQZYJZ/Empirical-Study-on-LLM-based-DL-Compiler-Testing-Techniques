'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsinh\ntorch.arcsinh(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print('Input data is: ', input_data)
output = torch.arcsinh(input_data)
print('Output is: ', output)