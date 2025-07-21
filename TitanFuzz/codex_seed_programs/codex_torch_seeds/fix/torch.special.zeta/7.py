'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.zeta\ntorch.special.zeta(input, other, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(4, 4)
other = torch.randn(4, 4)
print('Task 3: Call the API torch.special.zeta')
out = torch.special.zeta(input, other)
print('The result of torch.special.zeta is: {}'.format(out))