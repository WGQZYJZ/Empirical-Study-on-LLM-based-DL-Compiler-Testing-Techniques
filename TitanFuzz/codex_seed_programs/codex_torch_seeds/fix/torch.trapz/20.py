'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trapz\ntorch.trapz(y, *, dx=1, dim=-1)\n'
import torch
x = torch.linspace(0, (2 * 3.14), steps=100)
y = torch.sin(x)
print(torch.trapz(y, dx=0.0314))