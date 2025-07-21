'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kron\ntorch.kron(input, other, *, out=None)\n'
import torch
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
print(torch.kron(a, b))
print(torch.kron(a, b).shape)