'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logcumsumexp\ntorch.logcumsumexp(input, dim, *, out=None)\n'
import torch
data = torch.randn(2, 3, 4)
torch.logcumsumexp(data, dim=1)
torch.logcumsumexp(data, dim=2)