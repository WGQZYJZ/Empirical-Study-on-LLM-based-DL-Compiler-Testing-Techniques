'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3, 5, 5)
print('Input data: ', input_data)
output = torch.rsqrt(input_data)
print('Output: ', output)