'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i1e\ntorch.special.i1e(input, *, out=None)\n'
import torch
import torch.special
x = torch.arange(1, 10, dtype=torch.float64)
y = torch.special.i1e(x)
print(y)