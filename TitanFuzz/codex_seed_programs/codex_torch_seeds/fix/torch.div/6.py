'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.div\ntorch.div(input, other, *, rounding_mode=None, out=None)\n'
import torch
a = torch.rand(3, 5)
b = torch.rand(3, 5)
c = torch.div(a, b)
print(c)