'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logit\ntorch.logit(input, eps=None, *, out=None)\n'
import torch
input = torch.randn(2, 2)
print(input)
output = torch.logit(input)
print(output)