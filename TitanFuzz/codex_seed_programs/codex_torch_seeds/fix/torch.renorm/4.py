'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.renorm\ntorch.renorm(input, p, dim, maxnorm, *, out=None)\n'
import torch
input = torch.randn(2, 5)
print('Input: \n', input)
output = torch.renorm(input, p=2, dim=1, maxnorm=1)
print('Output: \n', output)