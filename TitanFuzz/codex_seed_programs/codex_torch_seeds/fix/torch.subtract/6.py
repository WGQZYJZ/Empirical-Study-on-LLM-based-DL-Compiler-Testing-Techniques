'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.subtract\ntorch.subtract(input, other, *, alpha=1, out=None)\n'
import torch
x = torch.randn(3, 4)
y = torch.randn(3, 4)
torch.subtract(x, y)