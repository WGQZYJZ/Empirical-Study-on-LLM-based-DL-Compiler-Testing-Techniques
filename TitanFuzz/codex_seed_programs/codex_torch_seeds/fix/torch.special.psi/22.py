'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.psi\ntorch.special.psi(input, *, out=None)\n'
import torch
x = torch.randn(1, 5)
y = torch.special.psi(x)
print(y)