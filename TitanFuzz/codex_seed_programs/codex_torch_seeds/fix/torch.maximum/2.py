'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.maximum\ntorch.maximum(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
other = torch.randn(2, 3, 4)
torch.maximum(input, other, out=None)