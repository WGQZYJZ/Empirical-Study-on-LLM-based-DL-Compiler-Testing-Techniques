'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.outer\ntorch.outer(input, vec2, *, out=None)\n'
import torch
x = torch.arange(1, 6)
y = torch.arange(1, 5)
print(torch.outer(x, y))