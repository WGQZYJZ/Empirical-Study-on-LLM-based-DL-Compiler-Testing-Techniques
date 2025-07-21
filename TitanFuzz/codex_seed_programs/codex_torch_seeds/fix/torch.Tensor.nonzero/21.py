'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
input = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(input.nonzero())
print(input.nonzero(as_tuple=True))
'\nTask 4: Call the API torch.nonzero\ntorch.nonzero(_input_tensor, as_tuple=False)\n'
import torch
input = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(torch.nonzero(input))
print(torch.nonzero(input, as_tuple=True))