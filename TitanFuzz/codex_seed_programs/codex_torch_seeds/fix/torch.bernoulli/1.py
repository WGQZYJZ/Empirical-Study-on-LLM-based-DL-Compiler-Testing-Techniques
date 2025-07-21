'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bernoulli\ntorch.bernoulli(input, *, generator=None, out=None)\n'
import torch
input = torch.rand(4, 4)
output = torch.bernoulli(input)
print('Input:')
print(input)
print('Output:')
print(output)