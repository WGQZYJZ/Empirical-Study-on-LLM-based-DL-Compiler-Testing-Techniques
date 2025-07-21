'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor_\ntorch.Tensor.logical_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
other = torch.tensor([[1, 0, 1], [0, 1, 1], [1, 1, 0]])
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('input_tensor:')
print(input_tensor)
print('other:')
print(other)
print('Task 3: Call the API torch.Tensor.logical_xor_')
print('torch.Tensor.logical_xor_(input_tensor, other)')
print(torch.Tensor.logical_xor_(input_tensor, other))