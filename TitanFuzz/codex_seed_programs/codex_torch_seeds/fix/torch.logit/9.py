'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logit\ntorch.logit(input, eps=None, *, out=None)\n'
import torch
import torch
x = torch.randn(5, 3)
torch.logit(x)
torch.logit(x, eps=1e-06)
y = torch.randn(5, 3)
torch.logit(x, out=y)
y
torch.logit(x, eps=1e-06, out=y)
y
torch.logit(x, out=y, eps=1e-06)
y