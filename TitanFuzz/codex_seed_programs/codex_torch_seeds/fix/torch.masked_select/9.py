'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
import torch
x = torch.randn(3, 4)
torch.masked_select(x, (x > 0.5))