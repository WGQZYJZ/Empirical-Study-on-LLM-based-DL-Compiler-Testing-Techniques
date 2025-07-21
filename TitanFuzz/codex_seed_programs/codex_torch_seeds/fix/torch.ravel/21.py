'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
input = torch.randn(3, 2, 3)
output = torch.ravel(input)
print('Input: ', input)
print('Output: ', output)