'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
input_data = torch.rand(4, 4)
print('Input data: ', input_data)
output = torch.signbit(input_data)
print('Output: ', output)