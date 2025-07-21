'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
import torch
input = torch.randn(3, requires_grad=True)
torch.special.logit(input, eps=None, out=None)
print(input)