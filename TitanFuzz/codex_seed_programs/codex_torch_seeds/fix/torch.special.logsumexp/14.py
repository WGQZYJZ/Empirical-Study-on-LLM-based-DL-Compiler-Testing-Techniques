'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print(torch.special.logsumexp(input, dim=0))
print(torch.special.logsumexp(input, dim=1))
print(torch.special.logsumexp(input, dim=1, keepdim=True))