'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kron\ntorch.kron(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3)
other = torch.randn(4, 5)
print(torch.kron(input, other))
print(torch.kron(input, other).size())