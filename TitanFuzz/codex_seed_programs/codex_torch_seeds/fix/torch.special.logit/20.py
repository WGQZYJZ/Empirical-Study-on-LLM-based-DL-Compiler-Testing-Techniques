'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
input = torch.randn(1, requires_grad=True)
print('input = ', input)
output = torch.special.logit(input)
print('output = ', output)