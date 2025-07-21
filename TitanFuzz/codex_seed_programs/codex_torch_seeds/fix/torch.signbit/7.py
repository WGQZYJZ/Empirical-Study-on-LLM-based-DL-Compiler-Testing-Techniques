'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data is: ', input_data)
output = torch.signbit(input_data)
print('Output is: ', output)