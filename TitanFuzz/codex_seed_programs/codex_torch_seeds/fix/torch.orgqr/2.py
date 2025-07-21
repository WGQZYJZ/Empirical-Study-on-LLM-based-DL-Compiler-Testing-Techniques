'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.orgqr\ntorch.orgqr(input, tau)\n'
import torch
input = torch.randn(2, 2)
tau = torch.randn(2)
(q, r) = torch.orgqr(input, tau)
print('input:', input)
print('tau:', tau)
print('q:', q)
print('r:', r)