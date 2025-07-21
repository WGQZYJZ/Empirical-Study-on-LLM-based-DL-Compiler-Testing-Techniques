'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch._assert\ntorch._assert(condition, message)\n'
import torch
a = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
c = torch.randn(1)
torch._assert((a.shape == b.shape), 'a and b must have the same shape')
torch._assert((a.shape == c.shape), 'a and c must have the same shape')