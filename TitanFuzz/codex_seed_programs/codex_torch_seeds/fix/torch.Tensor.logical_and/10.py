'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and\ntorch.Tensor.logical_and(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]])
other = torch.tensor([1, 0, 1, 0])
print('Input Tensor:')
print(input_tensor)
print('Other:')
print(other)
print('Output:')
print(torch.Tensor.logical_and(input_tensor, other))