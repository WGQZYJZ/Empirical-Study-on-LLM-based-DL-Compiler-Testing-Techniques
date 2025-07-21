'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
data = torch.randn(2, 3)
print(torch.special.logsumexp(data, dim=1))
print(torch.special.logsumexp(data, dim=0))
print(torch.special.logsumexp(data, dim=1, keepdim=True))
print(torch.special.logsumexp(data, dim=0, keepdim=True))
print(torch.special.logsumexp(data, dim=(- 1)))
print(torch.special.logsumexp(data, dim=(- 2)))