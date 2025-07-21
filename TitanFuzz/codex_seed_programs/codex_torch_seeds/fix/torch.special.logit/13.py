'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
output = torch.special.logit(input)
print(output)