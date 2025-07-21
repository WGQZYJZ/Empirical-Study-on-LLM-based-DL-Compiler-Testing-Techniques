'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3)
dim = 0
keepdim = False
print(torch.special.logsumexp(input, dim, keepdim))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3)
dim = 1
keepdim = True
print(torch.special.logsumexp(input, dim, keepdim))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3)
dim = 1
keepdim = False