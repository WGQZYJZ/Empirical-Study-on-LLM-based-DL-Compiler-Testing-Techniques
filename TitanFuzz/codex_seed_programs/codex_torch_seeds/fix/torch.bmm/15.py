'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, deterministic=False, out=None)\n'
import torch
import torch
x = torch.randn(16, 32, 32)
y = torch.randn(16, 32, 32)
torch.bmm(x, y)