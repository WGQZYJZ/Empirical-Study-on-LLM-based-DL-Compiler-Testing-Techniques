'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.outer\ntorch.outer(input, vec2, *, out=None)\n'
import torch
vec1 = torch.arange(1, 6)
vec2 = torch.arange(1, 4)
out = torch.outer(vec1, vec2)
print(out)