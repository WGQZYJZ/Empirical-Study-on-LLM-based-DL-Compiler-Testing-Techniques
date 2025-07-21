'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch._assert\ntorch._assert(condition, message)\n'
import torch
a = torch.randn(2, 2)
b = torch.randn(2, 2)
torch._assert((a.shape == b.shape), 'a and b must have the same shape')