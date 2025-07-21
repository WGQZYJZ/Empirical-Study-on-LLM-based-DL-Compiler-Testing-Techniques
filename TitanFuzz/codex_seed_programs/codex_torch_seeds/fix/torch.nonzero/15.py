'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
input = torch.randint(0, 2, (3, 3), dtype=torch.long)
print(input)
print(torch.nonzero(input))
print(torch.nonzero(input, as_tuple=True))