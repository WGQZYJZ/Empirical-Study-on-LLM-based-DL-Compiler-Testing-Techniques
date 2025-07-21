'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.renorm\ntorch.renorm(input, p, dim, maxnorm, *, out=None)\n'
import torch
import torch
input = torch.arange(1, 10, dtype=torch.float).reshape(3, 3)
print('Input:\n', input)
output = torch.renorm(input, p=1, dim=0, maxnorm=1)
print('Output:\n', output)