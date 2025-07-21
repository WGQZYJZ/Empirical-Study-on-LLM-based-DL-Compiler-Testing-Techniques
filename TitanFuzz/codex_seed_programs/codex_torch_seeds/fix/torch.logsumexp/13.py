'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logsumexp\ntorch.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(2, 3)
y = torch.logsumexp(x, dim=1, keepdim=True)
print(x)
print(y)