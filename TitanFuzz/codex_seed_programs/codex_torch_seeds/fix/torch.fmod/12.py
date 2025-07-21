'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmod\ntorch.fmod(input, other, *, out=None)\n'
import torch
x = torch.randn(4)
y = torch.randn(4)
torch.fmod(x, y)
x = torch.randn(4, 4)
y = torch.randn(4, 4)
torch.fmod(x, y)
x = torch.randn(4, 4, 4)
y = torch.randn(4, 4, 4)
torch.fmod(x, y)