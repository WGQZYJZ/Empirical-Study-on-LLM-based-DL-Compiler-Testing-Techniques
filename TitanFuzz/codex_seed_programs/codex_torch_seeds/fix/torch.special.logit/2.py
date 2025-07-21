'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print(input)
output = torch.special.logit(input)
print(output)