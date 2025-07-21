'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inner\ntorch.Tensor.inner(_input_tensor, other)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = _input_tensor.inner(other)
print('output: ', output)