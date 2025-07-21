'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch._assert\ntorch._assert(condition, message)\n'
import torch
x = torch.randn(2, 3, requires_grad=True)
y = torch.randn(2, 3, requires_grad=True)
torch._assert((x.shape == y.shape), 'Shape mismatch')