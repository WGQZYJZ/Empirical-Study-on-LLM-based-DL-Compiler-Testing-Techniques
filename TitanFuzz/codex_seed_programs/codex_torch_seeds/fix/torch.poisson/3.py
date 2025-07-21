'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.poisson\ntorch.poisson(input, generator=None)\n'
import torch
input = torch.randn(1, 1)
print('Input: ', input)
output = torch.poisson(input)
print('Output: ', output)