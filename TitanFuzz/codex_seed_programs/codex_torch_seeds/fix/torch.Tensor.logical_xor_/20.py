'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor_\ntorch.Tensor.logical_xor_(_input_tensor, other)\n'
import torch
_input_tensor = torch.Tensor([[1, 0, 1], [0, 1, 1]])
other = torch.Tensor([[0, 1, 1], [0, 1, 0]])
torch.Tensor.logical_xor_(_input_tensor, other)
print(_input_tensor)