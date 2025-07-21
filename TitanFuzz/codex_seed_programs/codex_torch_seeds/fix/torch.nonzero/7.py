'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
input_data = torch.tensor([[1, 0, 0, 0], [0, 0, 0, 1], [1, 1, 0, 0]])
print(torch.nonzero(input_data))
print(torch.nonzero(input_data, as_tuple=True))