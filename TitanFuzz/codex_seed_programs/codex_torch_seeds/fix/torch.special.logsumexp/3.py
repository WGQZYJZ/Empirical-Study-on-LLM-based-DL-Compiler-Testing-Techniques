'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(3, 5, requires_grad=True)
y = torch.special.logsumexp(x, dim=1, keepdim=True)
print(y)