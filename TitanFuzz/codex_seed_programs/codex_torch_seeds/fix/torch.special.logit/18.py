'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
input = torch.rand(1, requires_grad=True)
print('Input: ', input)
print('Input type: ', input.type())
print('\nOutput: ', torch.special.logit(input))
print('Output type: ', torch.special.logit(input).type())