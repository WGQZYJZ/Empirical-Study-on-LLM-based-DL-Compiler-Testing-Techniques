'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logsumexp\ntorch.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
torch.logsumexp(input, dim=1, keepdim=True)