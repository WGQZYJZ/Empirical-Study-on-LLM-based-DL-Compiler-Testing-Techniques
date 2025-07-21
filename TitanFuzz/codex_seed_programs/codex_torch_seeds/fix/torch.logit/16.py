'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logit\ntorch.logit(input, eps=None, *, out=None)\n'
import torch
input = torch.randn(2, 3, requires_grad=True)
output = torch.logit(input)
print(input)
print(output)