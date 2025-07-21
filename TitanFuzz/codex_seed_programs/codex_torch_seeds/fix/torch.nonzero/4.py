'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
a = torch.tensor([[1, 1, 1], [0, 1, 0], [1, 1, 1]])
print(a)
print(torch.nonzero(a))
print(torch.nonzero(a, as_tuple=True))