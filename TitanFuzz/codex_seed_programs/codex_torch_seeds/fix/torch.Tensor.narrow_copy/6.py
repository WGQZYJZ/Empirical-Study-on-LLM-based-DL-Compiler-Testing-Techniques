'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow_copy\ntorch.Tensor.narrow_copy(_input_tensor, dimension, start, length)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('PyTorch location: ', torch.__file__)
print('\nTask 2: Generate input data')
input_tensor = torch.rand(5, 3)
print('input_tensor: ', input_tensor)
print('\nTask 3: Call the API torch.Tensor.narrow_copy')
output_tensor = torch.Tensor.narrow_copy(input_tensor, 0, 1, 3)
print('output_tensor: ', output_tensor)