'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trapz\ntorch.trapz(y, *, dx=1, dim=-1)\n'
import torch
y = torch.randn(1, 5)
trapz = torch.trapz(y)
print(trapz)