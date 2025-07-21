'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trunc\ntorch.trunc(input, *, out=None)\n'
import torch
import torch
input_data = torch.randn(2, 3, dtype=torch.float32)
output_data = torch.trunc(input_data)
print('Input data: \n', input_data)
print('Output data: \n', output_data)