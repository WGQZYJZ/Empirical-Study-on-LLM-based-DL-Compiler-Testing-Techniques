'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(2, 3)
print(input)
print('Task 3: Call the API torch.special.logsumexp')
print(torch.special.logsumexp(input, dim=1))