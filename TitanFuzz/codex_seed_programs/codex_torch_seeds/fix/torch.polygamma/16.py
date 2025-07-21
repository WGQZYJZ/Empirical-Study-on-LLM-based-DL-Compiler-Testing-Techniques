'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print('Input data: ', input_data)
output = torch.polygamma(3, input_data)
print('Output: ', output)