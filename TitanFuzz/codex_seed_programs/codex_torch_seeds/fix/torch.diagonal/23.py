'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagonal\ntorch.diagonal(input, offset=0, dim1=0, dim2=1)\n'
import torch
input = torch.randn(3, 3)
print('input: ', input)
print('torch.diagonal(input): ', torch.diagonal(input))
print('torch.diagonal(input, 1): ', torch.diagonal(input, 1))
print('torch.diagonal(input, -1): ', torch.diagonal(input, (- 1)))
print('torch.diagonal(input, 1, 1, 0): ', torch.diagonal(input, 1, 1, 0))
print('torch.diagonal(input, -1, 0, 1): ', torch.diagonal(input, (- 1), 0, 1))