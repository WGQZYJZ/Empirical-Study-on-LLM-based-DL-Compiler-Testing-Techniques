'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asinh\ntorch.asinh(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), 0, 1], dtype=torch.float)
print('Input data: ', input_data)
output_data = torch.asinh(input_data)
print('Output data: ', output_data)