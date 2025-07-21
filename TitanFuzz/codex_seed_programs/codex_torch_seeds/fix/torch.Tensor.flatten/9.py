'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flatten\ntorch.Tensor.flatten(_input_tensor, start_dim=0, end_dim=-1)\n'
import torch
from torch.autograd import Variable
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor:')
print(input_tensor)
flatten_tensor = input_tensor.flatten()
print('flatten_tensor:')
print(flatten_tensor)
flatten_tensor = input_tensor.flatten(start_dim=1, end_dim=2)
print('flatten_tensor:')
print(flatten_tensor)
flatten_tensor = input_tensor.flatten(start_dim=1, end_dim=3)
print('flatten_tensor:')
print(flatten_tensor)