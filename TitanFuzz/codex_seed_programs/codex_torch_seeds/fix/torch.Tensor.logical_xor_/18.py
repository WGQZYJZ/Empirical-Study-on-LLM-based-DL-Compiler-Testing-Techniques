'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor_\ntorch.Tensor.logical_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, False], [True, False]])
other = torch.tensor([[True, False], [True, True]])
torch.Tensor.logical_xor_(input_tensor, other)
print('input_tensor: ', input_tensor)
print('other: ', other)