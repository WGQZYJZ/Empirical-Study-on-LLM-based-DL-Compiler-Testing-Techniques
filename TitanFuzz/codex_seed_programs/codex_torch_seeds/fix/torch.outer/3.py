'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.outer\ntorch.outer(input, vec2, *, out=None)\n'
import torch
a = torch.rand(4)
b = torch.rand(4)
print(torch.outer(a, b))