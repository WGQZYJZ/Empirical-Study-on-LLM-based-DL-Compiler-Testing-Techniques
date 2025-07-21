'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.normal_\ntorch.Tensor.normal_(_input_tensor, mean=0, std=1, *, generator=None)\n'
import torch
input_tensor = torch.Tensor(size=(2, 3))
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('Task 2: Generate input data')
print('Input tensor: {}'.format(input_tensor))
print('Task 3: Call the API torch.Tensor.normal_')
print('Output tensor: {}'.format(input_tensor.normal_()))