'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('input_tensor = {}'.format(input_tensor))
torch.Tensor.pow_(input_tensor, 2)
print('input_tensor = {}'.format(input_tensor))