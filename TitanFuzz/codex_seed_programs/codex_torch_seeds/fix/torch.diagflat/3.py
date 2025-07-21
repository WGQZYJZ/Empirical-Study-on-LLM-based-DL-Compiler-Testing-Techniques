'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagflat\ntorch.diagflat(input, offset=0)\n'
import torch
input = torch.randn(4, 4)
print('Input: ', input)
output = torch.diagflat(input, offset=0)
print('Output: ', output)