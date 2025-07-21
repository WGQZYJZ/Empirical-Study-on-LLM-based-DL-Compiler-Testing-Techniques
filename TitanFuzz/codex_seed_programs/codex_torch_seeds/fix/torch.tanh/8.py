'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tanh\ntorch.tanh(input, *, out=None)\n'
import torch
input = torch.randn(1, 3)
print('Input: ', input)
output = torch.tanh(input)
print('Output: ', output)