'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trapz\ntorch.trapz(y, *, dx=1, dim=-1)\n'
import torch
x = torch.arange(1, 5, 0.1)
y = torch.sin(x)
z = torch.trapz(y, dx=0.1, dim=0)
print(z)