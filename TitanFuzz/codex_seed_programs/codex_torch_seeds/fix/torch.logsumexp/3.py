'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logsumexp\ntorch.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
a = torch.randn(4, 4)
print(a)
print(torch.logsumexp(a, dim=1))
print(torch.logsumexp(a, dim=1, keepdim=True))
print(torch.logsumexp(a, dim=1, keepdim=True).shape)