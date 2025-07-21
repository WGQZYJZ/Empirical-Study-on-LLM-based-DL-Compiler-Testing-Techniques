'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
output = torch.signbit(input_data)
print('input data = \n', input_data)
print('output = \n', output)