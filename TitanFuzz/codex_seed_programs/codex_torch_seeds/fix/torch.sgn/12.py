'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
input_data = torch.Tensor([(- 1), 0, 1])
output_data = torch.sgn(input_data)
print('Input data: ', input_data)
print('Output data: ', output_data)