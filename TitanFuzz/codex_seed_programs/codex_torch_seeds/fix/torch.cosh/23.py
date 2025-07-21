'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cosh\ntorch.cosh(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), 0, 1])
output_data = torch.cosh(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)