'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log2\ntorch.log2(input, *, out=None)\n'
import torch
input = torch.randn(1, 1, 3, 3)
print('Input: ', input)
output = torch.log2(input)
print('Output: ', output)