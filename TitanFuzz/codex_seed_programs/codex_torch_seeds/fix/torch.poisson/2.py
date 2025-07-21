'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.poisson\ntorch.poisson(input, generator=None)\n'
import torch
input = torch.rand(3, 3)
output = torch.poisson(input)
print('input: ', input)
print('output: ', output)