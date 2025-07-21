'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
import torch
x = torch.rand(4, 4)
print(x)
y = torch.special.logit(x)
print(y)