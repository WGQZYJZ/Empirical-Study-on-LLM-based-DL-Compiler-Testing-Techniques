'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tanh\ntorch.tanh(input, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input is: ', input)
output = torch.tanh(input)
print('Output is: ', output)