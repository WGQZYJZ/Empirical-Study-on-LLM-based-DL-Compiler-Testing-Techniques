'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
import torch
input_data = torch.tensor([2.0, 4.0, 8.0, 16.0])
print('input data: ', input_data)
output = torch.rsqrt(input_data)
print('output: ', output)