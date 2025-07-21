'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_or_\ntorch.Tensor.logical_or_(_input_tensor, other)\n'
import torch
_input_tensor = torch.tensor([[0, 1, 0], [0, 0, 1]])
other = torch.tensor([[0, 0, 1], [0, 1, 0]])
torch.Tensor.logical_or_(_input_tensor, other)
print(_input_tensor)