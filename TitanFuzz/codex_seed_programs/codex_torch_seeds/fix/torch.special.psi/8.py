'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.psi\ntorch.special.psi(input, *, out=None)\n'
import torch
input = torch.randn(1, 3, 3, requires_grad=True)
print(input)
print(torch.special.psi(input))