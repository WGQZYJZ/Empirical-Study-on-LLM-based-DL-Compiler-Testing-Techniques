'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
output = torch.ceil(input_data)
print('input_data:')
print(input_data)
print('output:')
print(output)