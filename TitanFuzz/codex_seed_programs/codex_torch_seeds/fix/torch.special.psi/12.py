'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.psi\ntorch.special.psi(input, *, out=None)\n'
import torch
input = torch.randn(2, 3, dtype=torch.float)
print(input)
print(torch.special.psi(input))