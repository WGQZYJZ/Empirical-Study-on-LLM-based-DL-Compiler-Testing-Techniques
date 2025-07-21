'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polar\ntorch.polar(abs, angle, *, out=None)\n'
import torch
abs = torch.randn(2, 3)
angle = torch.randn(2, 3)
torch.polar(abs, angle)
print(torch.polar(abs, angle))