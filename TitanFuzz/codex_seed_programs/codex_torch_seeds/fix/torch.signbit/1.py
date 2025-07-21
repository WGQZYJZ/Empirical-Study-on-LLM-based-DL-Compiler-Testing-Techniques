'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
input_data = torch.rand(3, 3)
output = torch.signbit(input_data)
print('Input data: ', input_data)
print('Output data: ', output)