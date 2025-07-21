'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch._assert\ntorch._assert(condition, message)\n'
import torch
x = torch.rand(4, 4)
y = torch.rand(4, 4)
torch._assert((x.shape == y.shape), 'shape mismatch')