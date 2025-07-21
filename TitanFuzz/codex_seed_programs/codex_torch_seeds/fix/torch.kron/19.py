'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kron\ntorch.kron(input, other, *, out=None)\n'
import torch
a = torch.randn(2, 3)
b = torch.randn(3, 4)
print(a)
print(b)
print(torch.kron(a, b))
print(torch.kron(a, b).size())