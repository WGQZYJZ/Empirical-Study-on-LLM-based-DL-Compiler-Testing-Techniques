'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
in_data = torch.arange(1, 10, dtype=torch.float)
out = torch.special.digamma(in_data)
print(out)