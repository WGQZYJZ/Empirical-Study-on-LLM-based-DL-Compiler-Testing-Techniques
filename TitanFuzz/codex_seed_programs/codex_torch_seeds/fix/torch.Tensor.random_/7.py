'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.random_\ntorch.Tensor.random_(_input_tensor, from=0, to=None, *, generator=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.rand(2, 3)
print('Input tensor: ', input_tensor)
print('Task 3: Call the API torch.Tensor.random_')
output_tensor = torch.Tensor.random_(input_tensor, from_=1, to=10, generator=None)
print('Output tensor: ', output_tensor)