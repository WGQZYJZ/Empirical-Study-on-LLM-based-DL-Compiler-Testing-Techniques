'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tanh\ntorch.tanh(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 1)
output_data = torch.tanh(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)