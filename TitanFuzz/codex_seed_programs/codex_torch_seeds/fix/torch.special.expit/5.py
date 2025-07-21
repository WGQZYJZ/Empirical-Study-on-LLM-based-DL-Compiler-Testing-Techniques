'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.expit\ntorch.special.expit(input, *, out=None)\n'
import torch
input = torch.randn(1, 3)
print('Input: ', input)
output = torch.special.expit(input)
print('Output: ', output)
output = torch.sigmoid(input)
print('Output: ', output)
output = torch.relu(input)
print('Output: ', output)