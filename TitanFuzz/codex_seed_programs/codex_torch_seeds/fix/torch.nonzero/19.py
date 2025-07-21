'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
input = torch.tensor([[1, 2, 3], [0, 0, 0], [4, 5, 6], [0, 0, 0]])
result = torch.nonzero(input)
print(result)
result = torch.nonzero(input, as_tuple=True)
print(result)