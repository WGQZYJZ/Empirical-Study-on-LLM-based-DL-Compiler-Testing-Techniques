'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
input_data = torch.rand(4, 4)
print('Input data:')
print(input_data)
output = torch.abs(input_data)
print('Output:')
print(output)