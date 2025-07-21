'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
input = torch.randn(4, 8)
print('Input: ', input)
output = torch.narrow(input, 0, 1, 3)
print('Output: ', output)