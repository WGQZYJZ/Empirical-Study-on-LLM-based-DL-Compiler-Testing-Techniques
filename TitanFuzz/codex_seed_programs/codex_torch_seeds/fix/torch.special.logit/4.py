'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
x = torch.randn(3, requires_grad=True)
print('x: ', x)
y = torch.special.logit(x)
print('y: ', y)