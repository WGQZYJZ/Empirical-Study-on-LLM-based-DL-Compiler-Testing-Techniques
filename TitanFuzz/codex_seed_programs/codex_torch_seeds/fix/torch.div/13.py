'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.div\ntorch.div(input, other, *, rounding_mode=None, out=None)\n'
import torch
a = torch.rand(2, 3)
b = torch.rand(2, 3)
torch.div(a, b)