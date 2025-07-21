'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data:')
print(input_data)
output_data = torch.digamma(input_data)
print('Output data:')
print(output_data)