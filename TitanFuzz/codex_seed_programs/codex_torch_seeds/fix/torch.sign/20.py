'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print('Input data is: ', input_data)
output = torch.sign(input_data)
print('Output is: ', output)