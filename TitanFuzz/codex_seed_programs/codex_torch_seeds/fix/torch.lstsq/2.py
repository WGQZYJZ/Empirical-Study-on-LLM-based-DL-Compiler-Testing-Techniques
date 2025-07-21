'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
import torch
x = torch.randn(5, 3, dtype=torch.float)
y = torch.randn(5, 2, dtype=torch.float)
torch.lstsq(x, y)